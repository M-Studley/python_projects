inventory = {}


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
        self.time_in_store: str = f"{self.checked_out - self.checked_in} days"
        self.cost_by_weight: str = f"{self.weight / self.price}/{self.unit_of_measurement}"

    def __repr__(self) -> str:
        return (f"Name: {self.name}\nCategory: {self.category}\nQuantity: {self.quantity}\nPrice: {self.price}\n"
                f"Weight: {self.weight}\nUnit of Measurement: {self.unit_of_measurement}\nPurveyor: {self.purveyor}\n"
                f"Month Ordered: {self.month_ordered}\nChecked In: {self.checked_in}\nChecked Out: {self.checked_out}\n"
                f"Time In Store: {self.time_in_store}\nCost By Weight: {self.cost_by_weight}")


class GetAddRemoveItem:
    def __init__(self, item_name: Item):
        self.item = item_name

    def get_item(self) -> str:
        return str(self.item.name)

    def get_items_in_category(self) -> str:
        return str(inventory[self.item.category])

    def add_category(self) -> None:
        if self.item.category not in inventory:
            inventory[self.item.category] = []

# TODO: not registering that the self.item.name is in inventory.values()....  FIX ME
    def add_item(self) -> None:
        if self.item.category not in inventory:
            self.add_category()

        if self.item.name not in inventory.values():
            inventory[self.item.category].append(self.item.name)
            print(f"{self.item.name} Added Successfully...")
        else:
            print(f"{self.item.name} already in inventory...")

    def remove_item(self) -> str:
        del self.item
        return f"{self.item.name} Removed Successfully..."


lavazza_dark_roast = Item(
    name='Lavazza Dark Roast',
    category='Coffee Beans',
    quantity=1,
    price=1690.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='Lazada',
    month_ordered=2,
    checked_in=47,
    checked_out=60
)

lavazza_light_roast = Item(
    name='Lavazza Light Roast',
    category='Coffee Beans',
    quantity=1,
    price=1490.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='Lazada',
    month_ordered=2,
    checked_in=47,
    checked_out=60
)

lavazza_light_roast2 = Item(
    name='Lavazza Light Roast',
    category='Coffee Beans',
    quantity=1,
    price=1490.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='Lazada',
    month_ordered=2,
    checked_in=47,
    checked_out=60
)

GetAddRemoveItem(lavazza_dark_roast).add_item()
print(inventory)
print(GetAddRemoveItem(lavazza_dark_roast).get_items_in_category())
print()
GetAddRemoveItem(lavazza_light_roast).add_item()
print(inventory)
print(GetAddRemoveItem(lavazza_light_roast).get_items_in_category())
print()
GetAddRemoveItem(lavazza_light_roast2).add_item()
print(inventory)
print(GetAddRemoveItem(lavazza_light_roast2).get_items_in_category())
