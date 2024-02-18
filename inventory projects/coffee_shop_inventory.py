full_inventory = {}


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
                 checked_out: int = None):
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
        # returns all information on an item
        return "\n".join([f"{key.title()}: {str(value).title()}" for key, value in self.__dict__.items()])


class ItemManager:
    # responsible for adding an item and category, removing, and changing checked in and out days
    def __init__(self, item_name: Item):
        self.item = item_name

    def add_item(self) -> None:
        # checks to see if the item being added is a duplicate (checked by item name)
        # if item exists it raises the counter of the original item

        if self.item.name not in full_inventory:
            full_inventory.update(
                {self.item.name: [('category', self.item.category),
                                  ('item count', self.item.item_count),
                                  ('price', self.item.price),
                                  ('weight', f'{self.item.weight} / {self.item.unit_of_measurement}'),
                                  (f'cost per {self.item.unit_of_measurement}', self.item.cost_by_weight),
                                  ('purveyor', self.item.purveyor),
                                  ('month ordered', self.item.month_ordered),
                                  ('checked in', self.item.checked_in),
                                  ('checked out', self.item.checked_out),
                                  ('time in store', self.item.time_in_store)]})

            print(f"'{self.item.name.title()}' Added Successfully...")
        else:
            print(f"'{self.item.name.title()}' Already in Inventory...")
            add_another = "Would you like to add another?\nPlease enter 'y' or 'n': "
            if get_bool(add_another):
                update_count(self.item.name, '+')
            else:
                print(f"'{self.item.name.title()}' was NOT added to the inventory")

    def remove_item(self) -> None:
        # if there is more than one item, it will decrement the count by one
        # if there is only one item, it will remove it from full inventory
        current_count = get_current_count(self.item.name)
        if self.item.name in full_inventory:
            if current_count > 1:
                update_count(self.item.name, '-')
            else:
                del full_inventory[self.item.name]
        else:
            print(f"'{self.item.name.title()}' Not Found...")

    def change_checked_in(self, day_of_year: int) -> None:
        # changes the checked in day
        if isinstance(day_of_year, int) and day_of_year in range(1, 367):
            self.item.checked_in = day_of_year

    def change_checked_out(self, day_of_year: int) -> None:
        # changes the checked out day along with time in store
        if isinstance(day_of_year, int) and day_of_year in range(1, 367):
            self.item.checked_out = day_of_year
            self.item.time_in_store = f"{self.item.checked_out - self.item.checked_in} days"


def get_inventory() -> str:
    # returns an inventory in string form
    return "\n".join([f"{key.title()}: {value}" for key, value in full_inventory.items()])


def get_categories() -> str:
    # returns all categories in the inventory
    return "\n".join([f"{category.title()}" for category in full_inventory])


def get_all_items() -> str:
    # returns all the items in the inventory
    all_items = ""
    for values in full_inventory.values():
        for value in values:
            for item in value:
                if isinstance(item, str):
                    all_items += f"\n{item}"
    return all_items


def get_items_in_category(category: str) -> str:
    # returns the items inside a given category
    if category in full_inventory:
        print(f"Category: {category.upper()}")
        return "\n".join([item[0] for item in full_inventory.get(category, [])])
    else:
        return f"Category {category.upper()} not found...\n"


def get_item_count(inventory_item) -> int:
    # returns the count of an item passed in
    for values in full_inventory.values():
        for items in values:
            return items.count(inventory_item)


def get_full_inventory_sum() -> float:
    # returns the total sum of all items in the inventory
    total: float = 0.00
    for value in full_inventory.values():
        for name_price in value:
            total += name_price[-1]
    return total


def get_all_category_sum() -> str:
    # returns a breakdown of all categories sum
    category_breakdown = ""
    for category in full_inventory:
        category_sum = [sum(item[1] for item in full_inventory.get(category, []))]
        category_breakdown += f"\n{category.title()}: {category_sum[0]}"
    return category_breakdown


def get_category_sum(category) -> float:
    # returns the total amount in a specific category
    if category in full_inventory:
        category_sum = [sum(item[1] for item in full_inventory.get(category, []))]
        print(category.title())
        return category_sum[0]
    else:
        print(f"{category.title()} not found...")
        return 0


def get_bool(bool_inquery) -> bool:
    # helper function that returns True for 'y' or False for 'n' otherwise will continue to loop
    user_input = input(bool_inquery).strip().lower()
    while user_input not in ['y', 'n']:
        user_input = input("Invalid input...\nPlease enter 'y' or 'n': ").strip().lower()
    if user_input == 'y':
        return True


def get_current_count(item_name) -> int:
    # helper function to get the current item count
    if item_name in full_inventory:
        return full_inventory[item_name][1][1]
    else:
        return 0


def update_count(item_name, operator):
    # helper function that pops the tuple out and inserts tuple with updated count
    if operator == '+':
        new_count_set = ('item count', get_current_count(item_name) + 1)
        full_inventory[item_name].pop(1)
        full_inventory[item_name].insert(1, new_count_set)
    else:
        new_count_set = ('item count', get_current_count(item_name) - 1)
        full_inventory[item_name].pop(1)
        full_inventory[item_name].insert(1, new_count_set)