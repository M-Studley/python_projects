inventory = {'coffee beans': [],
             'dairy': [],
             'dry goods': [],
             'paper goods': [],
             'ready to eat': [],
             'water': []}


class Item:
    def __init__(self, *,
                 name: str,
                 category: str,
                 price: float,
                 weight: float,
                 unit_of_measurement: str,
                 purveyor: str,
                 month_ordered: int,
                 checked_in: int = None,
                 checked_out: int = None):
        self.name = name
        self.category = category
        self.price = price
        self.weight = weight
        self.unit_of_measurement = unit_of_measurement
        self.purveyor = purveyor
        self.month_ordered = month_ordered
        self.checked_in = checked_in
        self.checked_out = checked_out
        self.cost_by_weight: str = f"{round(self.weight / self.price, 2)} / {self.unit_of_measurement}"
        self.time_in_store: str

        # calculates the time in store if both checked_in and checked_out have values
        if (self.checked_in and self.checked_out) is not None:
            self.time_in_store = f"{self.checked_out - self.checked_in} days"
        elif self.checked_out is None:
            self.time_in_store = "Item has not been checked out..."

    def __repr__(self) -> str:
        # returns all information on an item
        return "\n".join([f"{key.capitalize()}: {value}" for key, value in self.__dict__.items()])


class ItemManager:
    def __init__(self, item_name: Item):
        self.item = item_name

    def __add_category(self) -> None:
        # adds a category if non-existing.  used in the add_item function exclusively
        inventory[self.item.category] = []

    def add_item(self) -> None:
        # checks if the items category exists. adds if non-existent otherwise moves on
        # adds the item to the inventory if non-existent, otherwise prints that it exists
        # prompts user if they would like to add another of the same item, if y it does
        if self.item.category not in inventory:
            self.__add_category()

        item_found = any(item[0] == self.item.name for item in inventory.get(self.item.category, []))

        if not item_found:
            inventory[self.item.category].append((self.item.name, self.item.price))
            print(f"'{self.item.name}' Added Successfully...")
        else:
            print(f"'{self.item.name}' Already in Inventory...")
            add_another = "Would you like to add another?\nPlease enter 'y' or 'n': "
            if get_bool(add_another):
                inventory[self.item.category].append((self.item.name, self.item.price))
                print(f"'{self.item.name}' Added Successfully...")
            else:
                print(f"'{self.item.name}' was NOT added to the inventory")

    def remove_item(self):
        # checks for item in the category and produce a message
        # if item in inventory{} it will remove it and print a status message
        for index, tup in enumerate(inventory.get(self.item.category)):
            if self.item.name in tup:
                item_location = index
                del inventory[self.item.category][item_location]
                print(f"'{self.item.name}' Removed Successfully...")
            else:
                print(f"'{self.item.name}' Not Found...")


def get_inventory() -> str:
    # returns an inventory in string form
    return "\n".join([f"{key.title()}: {value}" for key, value in inventory.items()])


def get_categories() -> str:
    # returns all categories in the inventory
    return "\n".join([f"{category.title()}" for category in inventory])


def get_all_items() -> str:
    # returns all the items in the inventory
    all_items = ""
    for values in inventory.values():
        for value in values:
            for item in value:
                print("Item:", item)
                if isinstance(item, str):
                    all_items += f"\n{item}"
    return all_items


def get_items_in_category(category: str) -> str:
    # returns the items inside a given category
    if category in inventory:
        print(f"Category: {category.upper()}")
        return "\n".join([item[0] for item in inventory.get(category, [])])
    else:
        return f"Category {category.upper()} not found...\n"


def get_item_count(inventory_item) -> int:
    # returns the count of an item passed in
    for values in inventory.values():
        for items in values:
            return items.count(inventory_item)


def get_full_inventory_sum() -> float:
    # returns the total sum of all items in the inventory
    total: float = 0.00
    for value in inventory.values():
        for name_price in value:
            total += name_price[-1]
    return total


def get_bool(bool_inquery) -> bool:
    # helper function that returns True for 'y' or False for 'n' otherwise will continue to loop
    user_input = input(bool_inquery).strip().lower()
    while user_input not in ['y', 'n']:
        user_input = input("Invalid input...\nPlease enter 'y' or 'n': ").strip().lower()
    if user_input == 'y':
        return True
