from dataclasses import dataclass

full_inventory = {}
inventory_item_cache: list = []


# TODO: purveyor, month_ordered, checked_in, checked_out & time_in_store all need to be in a separate class
class Item:
    def __init__(self, *,
                 name: str,
                 category: str,
                 item_count: int,
                 price: float,
                 weight: float,
                 unit_of_measurement: str,
                 purveyor: str,
                 month_ordered: int,
                 checked_in: int = None,
                 checked_out: int = None,):
        self.name = name
        self.category = category
        self.item_count = item_count
        self.price = price
        self.weight = weight
        self.unit_of_measurement = unit_of_measurement
        self.purveyor = purveyor
        self.month_ordered = month_ordered
        self.checked_in = checked_in
        self.checked_out = checked_out
        self.cost_by_weight: str = f"{round(self.price / self.weight, 2)} / {self.unit_of_measurement}"
        self.time_in_store: str

        # calculates the time in store if both checked_in and checked_out have values
        if (self.checked_in and self.checked_out) is not None:
            self.time_in_store = f"{self.checked_out - self.checked_in} days"
        elif self.checked_out is None:
            self.time_in_store = "Item has not been checked out..."

    def __repr__(self) -> str:
        """returns all information on an item"""
        return "\n".join([f"{key.title()}: {str(value).title()}" for key, value in self.__dict__.items()])


# TODO - build a class for menu items and their cost
"""espresso = 10g of ground coffee = 30ml of liquid
   espresso, double = 20g of ground coffee = 60ml of liquid
   americano = 20g of ground coffee = 60ml of liquid
   latte = 20g of ground coffee = 60ml of liquid, 300ml of milk, steamed
   cappuccino = 20g of ground coffee = 60ml of liquid, 60ml of milk, steamed
   flat white = 20g of ground coffee = 60ml of liquid, 120ml of milk, steamed
   cafe noisette = 20g of ground coffee = 30ml of liquid, 120ml of milk, steamed
   this will take in the ingredients      menu_item_1 = {'latte': {'coffee beans': 20g*cost_by_weight,
                                                                       'milk (whole)': 300ml*cost_by_weight}}
                                          menu_item_2 = {'cappuccino': {'coffee beans': 10g*cost_by_weight}}
                                          menu_item_3 = {'espresso, single': {'coffee beans': 10g*cost_by_weight}}
                                          menu_item_4 = {'espresso, double': {'coffee beans': 20g*cost_by_weight}}"""


@dataclass
class ItemManager:

    @staticmethod
    def add_item(item: Item) -> None:
        """ Appends to the inventory cache if not already inside
        checks to see if the item being added is a duplicate (checked by item name) in full inventory
        if item exists it raises the counter of the original item """
        if item not in inventory_item_cache:
            inventory_item_cache.append(item)

        if item.name not in full_inventory:
            full_inventory.update(
                {item.name: [('category', item.category),
                             ('item count', item.item_count),
                             ('price', item.price),
                             ('weight', f'{item.weight} / {item.unit_of_measurement}'),
                             (f'cost per {item.unit_of_measurement}', item.cost_by_weight),
                             ('purveyor', item.purveyor),
                             ('month ordered', item.month_ordered),
                             ('checked in', item.checked_in),
                             ('checked out', item.checked_out),
                             ('time in store', item.time_in_store)]})

            print(f"'{item.name.title()}' Added Successfully!")
        else:
            print(f"'{item.name.title()}' Already in Inventory...")
            add_another = "Would you like to add another?\nPlease enter 'y' or 'n': "
            if get_bool(add_another):
                update_count(item.name, '+')
                print(f"'{item.name.title()}' Added Successfully!")
            else:
                print(f"'{item.name.title()}' was NOT added to the inventory...")

    @staticmethod
    def remove_item(item_name) -> None:
        """ if there is more than one item, it will decrement the count by one
        if there is only one item, it will remove it from full inventory """
        current_count = get_item_count(item_name)
        if item_name in full_inventory:
            if current_count > 1:
                update_count(item_name, '-')
            else:
                del full_inventory[item_name]
        else:
            print(f"'{item_name.title()}' Not Found...")

    @staticmethod
    def change_checked_in(item_name, day_of_year: int) -> None:
        """ changes the checked in day on both the object and the full inventory dict """
        if isinstance(day_of_year, int) and day_of_year in range(1, 367):
            full_inventory[item_name][7] = ('checked in', day_of_year)

    @staticmethod
    def change_checked_out(item_name, day_of_year: int) -> None:
        """ changes the checked out day in the full inventory dict
        also updates the time_in_store in the full inventory dict """
        if isinstance(day_of_year, int) and day_of_year in range(1, 367):
            full_inventory[item_name][8] = ('checked out', day_of_year)
            full_inventory[item_name][9] = ('time in store',
                                            full_inventory[item_name][8][1] - full_inventory[item_name][7][1])


def create_item() -> Item:
    """ creating a new item from user input with helper functions """
    item_info = {
        'name': None, 'category': None, 'item_count': None,
        'price': None, 'weight': None, 'unit_of_measurement': None,
        'purveyor': None, 'month_ordered': None}

    while True:
        for info in item_info:
            if info in ['price', 'weight', 'item_count', 'month_ordered']:
                item_info[info] = get_numeric_input(f"{info.upper()}: ",
                                                    int if info in ['item_count', 'month_ordered'] else float)
            elif info == 'unit_of_measurement':
                item_info[info] = get_unit_of_measurement()
            else:
                item_info[info] = input(f'{info.upper()}: ').strip().lower()
        # printing all users input for confirmation
        for key, value in item_info.items():
            print(f"{key}: {value}")

        if get_bool("Is all the information above correct [y, n]? "):
            break
        else:
            continue

    # once confirmed we will instantiate an Item
    new_item = Item(
        name=item_info['name'], category=item_info['category'], item_count=item_info['item_count'],
        price=item_info['price'], weight=item_info['weight'], unit_of_measurement=item_info['unit_of_measurement'],
        purveyor=item_info['purveyor'], month_ordered=item_info['month_ordered'])

    print(f"'{item_info['name'].upper()}' created successfully!")

    return new_item


# TODO create InventoryManager class
def get_inventory() -> str:
    """ returns an inventory in string form """
    inventory = ""
    for key, value in full_inventory.items():
        inventory += f"{key.upper()}\n"
        for tup in value:
            inventory += f"{tup[0].title()}: {str(tup[1]).title()}\n"
        inventory += '\n'

    return inventory


def get_categories() -> list:
    """ returns a sorted list of all categories in the inventory """
    category_set = set()
    for value in full_inventory.values():
        category_set.add(value[0][1])

    return sorted(category_set)


def get_purveyors() -> list:
    """ returns a sorted list of all purveyors in the inventory """
    category_set = set()
    for value in full_inventory.values():
        category_set.add(value[5][1])

    return sorted(category_set)


def get_all_items() -> list:
    """ returns all the items in the inventory, sorted """
    all_items = []
    for item in full_inventory:
        [all_items.append(item) for _ in range(get_item_count(item))]

    return sorted(all_items)


def get_items_in_category(category: str) -> list:
    """ returns the items inside a given category """
    items = []
    for key, values in full_inventory.items():
        for value in values:
            if category in value:
                [items.append(key) for _ in range(get_item_count(key))]

    return items


def get_items_by_purveyor(purveyor):
    """ returns the items inside a given purveyor """
    items = []
    for key, values in full_inventory.items():
        for value in values:
            if purveyor in value:
                [items.append(key) for _ in range(get_item_count(key))]

    return items


def get_items_by_order_month(order_month: int) -> list:
    """ returns the items for a given order month """
    items = []
    for key, values in full_inventory.items():
        for value in values:
            if order_month in value:
                [items.append(key) for _ in range(get_item_count(key))]

    return items


# TODO create InventoryCalculations class
def get_full_inventory_sum() -> float:
    """ returns the total sum of all items in the inventory """
    total: float = 0.00
    for item in full_inventory:
        total += (full_inventory[item][2][1]*get_item_count(item))

    return total


def get_all_category_sum() -> dict:
    """ returns a dictionary breakdown of all categories names and their sum """
    category_totals = {}
    [category_totals.update({category: 0}) for category in get_categories()]

    for values in full_inventory.values():
        category_totals[values[0][1]] += values[2][1]*values[1][1]

    return category_totals


def get_category_sum(category) -> float:
    """ returns the total amount in a specific category """
    category_sum: float = 0.00
    for values in full_inventory.values():
        if values[0][1] == category:
            print(values)
            category_sum += values[2][1]*values[1][1]

    return category_sum


def get_purveyor_sum(purveyor) -> float:
    """ returns the total amount in a specific purveyor """
    category_sum: float = 0.00
    for values in full_inventory.values():
        if values[5][1] == purveyor:
            print(values)
            category_sum += values[2][1]*values[1][1]

    return category_sum


def get_order_month_sum(order_month) -> float:
    """ returns the total amount in a specific order month """
    category_sum: float = 0.00
    for values in full_inventory.values():
        if values[6][1] == order_month:
            print(values)
            category_sum += values[2][1]*values[1][1]

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
        return full_inventory[item_name][1][1]
    else:
        return 0


def update_count(item_name, operator) -> None:
    """ helper function that pops the tuple out and inserts tuple with updated count """
    if operator == '+':
        new_count_set = ('item count', get_item_count(item_name) + 1)
        full_inventory[item_name].pop(1)
        full_inventory[item_name].insert(1, new_count_set)
    else:
        new_count_set = ('item count', get_item_count(item_name) - 1)
        full_inventory[item_name].pop(1)
        full_inventory[item_name].insert(1, new_count_set)


def get_numeric_input(prompt: str, expected_type: type) -> type:
    """ prompts user for numeric input and returns it with the specified type """
    while True:
        user_input = input(prompt).strip()
        if round(float(user_input)).is_integer():
            if expected_type(float(user_input)):
                return expected_type(user_input)
        print("Invalid input. Please enter a valid numeric value.")


def get_unit_of_measurement() -> str:
    """ specific helper function for creating an items weight identifier """
    while True:
        user_input = input("UNIT_OF_MEASUREMENT [kg, g, L or ml]: ").strip().lower()
        if user_input in ['kg', 'g', 'l', 'ml']:
            return user_input
        print("Invalid input. Please enter a valid unit of measurement.")
