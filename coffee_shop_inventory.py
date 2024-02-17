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
        # checks to see if the items category exists and adds if it does not or moves on if it does exist
        # will add the item to the inventory if non-existent.  prints status for confirmation
        if self.item.category not in inventory:
            self.__add_category()

        if self.item.name not in inventory[self.item.category]:
            inventory[self.item.category].append(self.item.name)
            print(f"'{self.item.name}' Added Successfully...")
        else:
            print(f"'{self.item.name}' Already in Inventory...")

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


# # ADD_ITEM() TESTING and GET_INVENTORY() TESTING...
# lavazza_dark_roast = Item(
#     name='Lavazza Dark Roast',
#     category='Coffee Beans',
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
#     category='Coffee Beans',
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
