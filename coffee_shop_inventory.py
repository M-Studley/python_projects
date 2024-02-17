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
                 quantity: int,
                 price: float,
                 weight: float,
                 unit_of_measurement: str,
                 purveyor: str,
                 month_ordered: int,
                 checked_in: int = None,
                 checked_out: int = None):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.weight = weight
        self.unit_of_measurement = unit_of_measurement
        self.purveyor = purveyor
        self.month_ordered = month_ordered
        self.checked_in = checked_in
        self.checked_out = checked_out
        self.cost_by_weight: str = f"{self.weight / self.price}/{self.unit_of_measurement}"
        self.time_in_store: str

        # calculates the time in store if both checked_in and checked_out have values
        if (self.checked_in and self.checked_out) is not None:
            self.time_in_store = f"{self.checked_out - self.checked_in} days"
        elif self.checked_out is None:
            self.time_in_store = "Item has not been checked out..."

    # returns all information on an item
    def __repr__(self) -> str:
        return "\n".join([f"{key.capitalize()}: {value}" for key, value in self.__dict__.items()])


class ItemManager:
    def __init__(self, item_name: Item):
        self.item = item_name

    def get_items_in_category(self) -> str:
        # returns the category the item is listed in
        if self.item.name in inventory[self.item.category]:
            return "\n".join([item for item in inventory.get(self.item.category, [])])
        else:
            return f"'{self.item.name}' Not Found..."

    def __add_category(self) -> None:
        # adds a category if non-existing.  used in the add_item function exclusively
        if self.item.category not in inventory:
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
            else:
                print(f"'{self.item.name}' was NOT added to the inventory")

    def remove_item(self):
        # will check for item in the category and produce a message
        # if item in inventory{} it will remove it and print a status message
        if self.item.name not in inventory[self.item.category]:
            print(f"'{self.item.name}' Not Found...")
        else:
            inventory[self.item.category].remove(self.item.name)
            print(f"'{self.item.name}' Removed Successfully...")


def get_inventory() -> str:
    # returns an inventory in string form
    return "\n".join([f"{key.title()}: {value}" for key, value in inventory.items()])


def get_full_inventory_sum() -> float:
    # returns the total sum of all items in the inventory
    total: float = 0.0
    for value in inventory.values():
        for name_price in value:
            total += name_price[-1]
    return total


def get_bool(bool_inquery) -> bool:
    # helper function that returns True for 'y' or False for 'n' otherwise will continue to loop
    user_input = input(bool_inquery)
    while user_input not in ['y', 'n']:
        user_input = input("Invalid input...\nPlease enter 'y' or 'n': ").strip().lower()
    if user_input == 'y':
        return True


# # ADD_ITEM() TESTING and GET_INVENTORY() TESTING...
# lavazza_dark_roast = Item(
#     name='Lavazza Dark Roast',
#     category='coffee beans',
#     quantity=1,
#     price=1690.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2,
#     checked_in=47,
#     checked_out=60)
#
# lavazza_light_roast = Item(
#     name='Lavazza Light Roast',
#     category='coffee beans',
#     quantity=1,
#     price=1490.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2,
#     checked_in=47,
#     checked_out=60)
#
# ItemManager(lavazza_dark_roast).add_item()
# print(get_inventory())
# print()
# ItemManager(lavazza_light_roast).add_item()
# print(get_inventory())
# print()
# ItemManager(lavazza_light_roast).add_item()
# print(get_inventory())
# print()


# # NO CHECKED_IN OR CHECKED_OUT TESTING
# lavazza_breakfast_blend = Item(
#     name='Lavazza Breakfast Blend',
#     category='Coffee Beans',
#     quantity=1,
#     price=1390.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2)
#
# ItemManager(lavazza_breakfast_blend).add_item()
# print(lavazza_breakfast_blend)
# print()


# # GET_ITEMS_IN_CATEGORY() TESTING...
# lavazza_dark_roast = Item(
#     name='Lavazza Dark Roast',
#     category='coffee beans',
#     quantity=1,
#     price=1690.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2,
#     checked_in=47,
#     checked_out=60)
#
# lavazza_light_roast = Item(
#     name='Lavazza Light Roast',
#     category='coffee beans',
#     quantity=1,
#     price=1490.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2,
#     checked_in=47,
#     checked_out=60)
#
# # SUCCESSFUL
# ItemManager(lavazza_dark_roast).add_item()
# ItemManager(lavazza_light_roast).add_item()
# print(get_inventory())
# print(ItemManager(lavazza_dark_roast).get_items_in_category())
# print()
#
# # UNSUCCESSFUL
# ItemManager(lavazza_dark_roast).add_item()
# print(get_inventory())
# print(ItemManager(lavazza_light_roast).get_items_in_category())
# print()


# # REMOVE_ITEM() TESTING...
# lavazza_dark_roast = Item(
#     name='Lavazza Dark Roast',
#     category='coffee beans',
#     quantity=1,
#     price=1690.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2,
#     checked_in=47,
#     checked_out=60)
#
# lavazza_light_roast = Item(
#     name='Lavazza Light Roast',
#     category='coffee beans',
#     quantity=1,
#     price=1490.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2,
#     checked_in=47,
#     checked_out=60)
#
# SUCCESSFUL
# ItemManager(lavazza_dark_roast).add_item()
# ItemManager(lavazza_light_roast).add_item()
# ItemManager(lavazza_dark_roast).remove_item()
# print(get_inventory())
#
# UNSUCCESSFUL
# ItemManager(lavazza_dark_roast).add_item()
# ItemManager(lavazza_light_roast).remove_item()
# print(get_inventory())


# # GET_FULL_INVENTORY_SUM() TESTING...
# lavazza_dark_roast = Item(
#     name='Lavazza Dark Roast',
#     category='coffee beans',
#     quantity=1,
#     price=1690.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2,
#     checked_in=47,
#     checked_out=60)
#
# lavazza_light_roast = Item(
#     name='Lavazza Light Roast',
#     category='coffee beans',
#     quantity=1,
#     price=1490.00,
#     weight=1000,
#     unit_of_measurement='g',
#     purveyor='Lazada',
#     month_ordered=2,
#     checked_in=47,
#     checked_out=60)
#
# ItemManager(lavazza_dark_roast).add_item()
# ItemManager(lavazza_light_roast).add_item()
# print(get_full_inventory_sum())
# print()
