from dataclasses import dataclass

full_inventory = {}
item_cache: list = []


@dataclass
class Item:
    name: str
    category: str
    purveyor: str
    item_count: int
    price: float
    weight: float
    unit_of_measurement: str
    checked_in: int
    checked_out: int = None
    time_in_store: str = None
    cost_by_weight: str = None

    def __repr__(self) -> str:
        """returns all information on an item"""
        return "\n".join([f"{key.title()}: {str(value).title()}" for key, value in self.__dict__.items()])


def create_item() -> Item:
    """Creating a new item from user input with helper functions.
    Will also append the item into item_cache[] if an item inside does not share the same name and price."""

    attribute_list: list = ['name', 'category', 'item_count', 'price', 'weight', 'unit_of_measurement',
                            'purveyor', 'checked_in', 'checked_out']

    new_item_attributes: dict = {}

    while True:
        for attribute in attribute_list:
            if attribute in ['price', 'weight', 'item_count', 'checked_in']:
                new_item_attributes[attribute] = get_numeric_input(
                    f"{attribute.upper()}: ", int if attribute in ['item_count', 'checked_in'] else float)
            elif attribute == 'unit_of_measurement':
                new_item_attributes[attribute] = get_unit_of_measurement()
            elif attribute == 'checked_out':
                new_item_attributes[attribute] = get_numeric_or_none_input(f"{attribute.upper()}: ")
            else:
                new_item_attributes[attribute] = get_string_input(f"{attribute.upper()}: ", str)

        # Print all user's input for confirmation
        for key, value in new_item_attributes.items():
            print(f"{key}: {value}")

        if get_bool("Is all the information above correct [y, n]? "):
            break
        else:
            continue

    # Check for values to calculate time_in_store and cost_by_weight
    time_in_store = f"{new_item_attributes['checked_out'] - new_item_attributes['checked_in']} days" \
        if new_item_attributes['checked_out'] is not None else None
    cost_by_weight = (f"{round(new_item_attributes['price'] / new_item_attributes['weight'], 2)}"
                      f" / {new_item_attributes['unit_of_measurement']}")

    # Once confirmed, instantiate an Item
    new_item = Item(**new_item_attributes, cost_by_weight=cost_by_weight, time_in_store=time_in_store)

    # Check for duplicates in item_cache
    if not any(item.name == new_item.name and item.price == new_item.price for item in item_cache):
        item_cache.append(new_item)

    print(f"'{new_item.name.upper()}' created successfully!")

    return new_item


def add_item(item: Item) -> None:
    """ checks to see if the item being added is a duplicate (checked by item name) in full inventory
    if item exists it raises the counter of the original item """
    full_item_name = f'{item.name}, {item.weight}/{item.unit_of_measurement}'
    if full_item_name not in full_inventory:
        full_inventory.update({full_item_name: {
            'category': item.category,
            'item count': item.item_count,
            'price': item.price,
            'purveyor': item.purveyor,
            'checked in': item.checked_in,
            'checked out': item.checked_out,
            'time in store': item.time_in_store}})

        print(f"'{full_item_name.title()}' Added Successfully!")
    else:
        print(f"'{full_item_name.title()}' Already in Inventory...")
        if get_bool("Would you like to add another?\nPlease enter 'y' or 'n': "):
            update_count(full_item_name, '+')
            print(f"'{full_item_name.title()}' Added Successfully!")
        else:
            print(f"'{full_item_name.title()}' was NOT added to the inventory...")


def remove_item(item_name: str) -> None:
    """ if there is more than one item, it will decrement the count by one
    if there is only one item, it will remove it from full inventory """
    if item_name in full_inventory:
        if get_item_count(item_name) > 1:
            update_count(item_name, '-')
        else:
            del full_inventory[item_name]
    else:
        print(f"'{item_name}' Not Found...")


def _change_checked_in(item_name: str, day_of_year: int) -> None:
    """ changes the checked in day for the full inventory dict """
    current_day = full_inventory[item_name]['checked in']
    if get_bool(f"Are you sure you would like to change the checked in day of {current_day} [y, n]? "):
        if isinstance(day_of_year, int) and day_of_year in range(1, 367):
            full_inventory[item_name]['checked in'] = day_of_year
            print("Checked in day successfully updated!")
    else:
        print("Checked in day NOT CHANGED...")


def change_checked_out(item_name: str, day_of_year: int) -> None:
    """ changes the checked out day in the full inventory dict
    also updates the time_in_store in the full inventory dict """
    if isinstance(day_of_year, int) and day_of_year in range(1, 367):
        if day_of_year < full_inventory[item_name]['checked in']:
            print(f"{day_of_year} is before the check in date ({full_inventory[item_name]['checked in']})...")
        else:
            full_inventory[item_name]['checked out'] = day_of_year
            full_inventory[item_name]['time in store'] = (
                    full_inventory[item_name]['checked out'] - full_inventory[item_name]['checked in'])


def get_inventory() -> str:
    """ returns an inventory in string form """
    inventory = ""
    for key, value in full_inventory.items():
        inventory += f"{key.upper()}\n"
        for sub_key, sub_value in value.items():
            inventory += f"{sub_key.upper()}: {str(sub_value).title()}\n"
        inventory += "\n"

    return inventory


def get_categories() -> list:
    """ returns a sorted list of all categories in the inventory """
    category_set = set()
    for value in full_inventory.values():
        for sub_key, sub_value in value.items():
            if sub_key == 'category':
                category_set.add(sub_value)

    return sorted(category_set)


def get_purveyors() -> list:
    """ returns a sorted list of all purveyors in the inventory """
    category_set = set()
    for value in full_inventory.values():
        for sub_key, sub_value in value.items():
            if sub_key == 'purveyor':
                category_set.add(sub_value)

    return sorted(category_set)


def get_all_items() -> list:
    """ returns all the items in the inventory, sorted """
    all_items = []
    for item in full_inventory:
        [all_items.append(item) for _ in range(get_item_count(item))]

    return sorted(all_items)


def get_items_in_category(category: str) -> list:
    """ returns the items inside a given category, if no items [None] will be returned """
    items = []
    for key, value in full_inventory.items():
        for sub_value in value.values():
            if category == sub_value:
                [items.append(key) for _ in range(get_item_count(key))]
    if not items:
        items.append(None)
    return items


def get_items_by_purveyor(purveyor: str):
    """ returns the items inside a given purveyor, if no items [None] will be returned """
    items = []
    for key, value in full_inventory.items():
        for sub_value in value.values():
            if purveyor == sub_value:
                [items.append(key) for _ in range(get_item_count(key))]
    if not items:
        items.append(None)
    return items


def get_full_inventory_sum() -> float:
    """ returns the total sum of all items in the inventory """
    total: float = 0.00
    for item in full_inventory:
        total += (full_inventory[item]['price'] * get_item_count(item))

    return total


def get_all_category_sum() -> dict:
    """ returns a dictionary breakdown of all categories names and their sum """
    category_totals = {}
    [category_totals.update({category: 0}) for category in get_categories()]

    for key, values in full_inventory.items():
        for sub_value in values.values():
            for value in category_totals:
                if value == sub_value:
                    category_totals[value] += full_inventory[key]['price'] * full_inventory[key]['item count']

    return category_totals


def get_category_sum(category: str) -> float:
    """ returns the total amount in a specific category """
    category_sum: float = 0.00
    for key, value in full_inventory.items():
        for sub_value in value.values():
            if sub_value == category:
                category_sum += full_inventory[key]['price'] * full_inventory[key]['item count']

    return category_sum


def get_purveyor_sum(purveyor: str) -> float:
    """ returns the total amount in a specific purveyor """
    category_sum: float = 0.00
    for key, value in full_inventory.items():
        for sub_value in value.values():
            if sub_value == purveyor:
                category_sum += full_inventory[key]['price'] * full_inventory[key]['item count']

    return category_sum


'''---------------- HELPER FUNCTIONS ----------------'''


def get_bool(bool_inquery) -> bool:
    """ helper function that returns True for 'y' or False for 'n' otherwise will continue to loop """
    user_input = input(bool_inquery).strip().lower()
    while user_input not in ['y', 'n']:
        user_input = input("Invalid input...\nPlease enter 'y' or 'n': ").strip().lower()
    if user_input == 'y':
        return True


def get_item_count(item_name) -> int:
    """ helper function to get the current item count """
    if item_name in full_inventory:
        return full_inventory[item_name]['item count']
    else:
        return 0


def update_count(item_name, operator) -> None:
    """ helper function that pops the tuple out and inserts tuple with updated count """
    if operator == '+':
        full_inventory[item_name]['item count'] += 1
    else:
        full_inventory[item_name]['item count'] -= 1


def get_string_input(prompt: str, expected_type: type):
    """ prompts user for input and returns it with the specified type """
    while True:
        user_input = input(prompt).strip().lower()
        if len(user_input) > 0:
            return expected_type(user_input)
        print("Please enter a valid input...")


def get_numeric_input(prompt: str, expected_type: type) -> type:
    """ prompts user for numeric input and returns it with the specified type """
    while True:
        user_input = input(prompt).strip()
        if len(user_input) > 0 and round(float(user_input)).is_integer():
            if expected_type(float(user_input)):
                return expected_type(user_input)
        print("Invalid input. Please enter a valid numeric value.")


def get_numeric_or_none_input(prompt: str) -> int or None:
    """ prompts user for numeric input and returns it with the specified type """
    while True:
        user_input = input(prompt).strip()
        if len(user_input) == 0:
            return None
        elif user_input.isnumeric():
            return int(user_input)

        print("Invalid input. Please enter a valid numeric value.")


def get_unit_of_measurement() -> str:
    """ specific helper function for creating an items weight identifier """
    while True:
        user_input = input("UNIT_OF_MEASUREMENT [kg, g, L or ml]: ").strip().lower()
        if user_input in ['kg', 'g', 'l', 'ml']:
            return user_input
        print("Invalid input. Please enter a valid unit of measurement.")
