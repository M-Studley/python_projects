from coffee_shop_inventory import *

# ---------------- TESTING OBJECT ---------------- #

test_item = Item(
    name='Test Item',
    category='Test',
    price=999.99,
    weight=99,
    unit_of_measurement='test',
    purveyor='Test',
    month_ordered=13)

# ---------------- COFFEE BEANS ---------------- #

lavazza_dark_roast = Item(
    name='Lavazza Dark Roast',
    category='coffee beans',
    price=1690.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='Lazada',
    month_ordered=2,
    checked_in=47,
    checked_out=60)

lavazza_medium_roast = Item(
    name='Lavazza Medium Roast',
    category='coffee beans',
    price=1590.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='Lazada',
    month_ordered=2)

lavazza_light_roast = Item(
    name='Lavazza Light Roast',
    category='coffee beans',
    price=1490.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='Lazada',
    month_ordered=2,
    checked_in=47,
    checked_out=60)

ItemManager(lavazza_dark_roast).add_item()
ItemManager(lavazza_medium_roast).add_item()
ItemManager(lavazza_light_roast).add_item()

# ---------------- DAIRY ---------------- #

heavy_cream = Item(
    name='Heavy Cream',
    category='dairy',
    price=279.00,
    weight=1000,
    unit_of_measurement='ml',
    purveyor='Gourmet Market',
    month_ordered=2)

whole_milk = Item(
    name='Milk (Whole)',
    category='dairy',
    price=95.00,
    weight=1000,
    unit_of_measurement='ml',
    purveyor='Makro',
    month_ordered=2)

ItemManager(heavy_cream).add_item()
ItemManager(whole_milk).add_item()

# ---------------- DRY GOODS ---------------- #

white_sugar = Item(
    name='Sugar (White)',
    category='dry goods',
    price=38.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='Shopee',
    month_ordered=2)

brown_sugar = Item(
    name='Sugar (Brown)',
    category='dry goods',
    price=55.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='Shopee',
    month_ordered=2)

ItemManager(white_sugar).add_item()
ItemManager(brown_sugar).add_item()

# ---------------- PAPER GOODS ---------------- #

beverage_napkins = Item(
    name='Beverage Napkins (Black)',
    category='paper goods',
    price=59.00,
    weight=200,
    unit_of_measurement='piece',
    purveyor='Makro',
    month_ordered=2)

branded_napkins = Item(
    name='Branded Napkins (White)',
    category='paper goods',
    price=120.00,
    weight=100,
    unit_of_measurement='piece',
    purveyor='Fancy Napkin Co.',
    month_ordered=2)

ItemManager(beverage_napkins).add_item()
ItemManager(branded_napkins).add_item()

# ---------------- READY TO EAT ---------------- #

ham_cheese_toastie = Item(
    name='Ham & Cheese Toastie',
    category='ready to eat',
    price=1560.00,
    weight=40,
    unit_of_measurement='piece',
    purveyor='Lazada',
    month_ordered=2)

pumpkin_soup = Item(
    name='Soup (Pumpkin)',
    category='ready to eat',
    price=1160.00,
    weight=3785,
    unit_of_measurement='ml',
    purveyor='Makro',
    month_ordered=2)

egg_tart = Item(
    name='Tart (Egg)',
    category='ready to eat',
    price=960.00,
    weight=20,
    unit_of_measurement='piece',
    purveyor='Tops Supermarket',
    month_ordered=2)

ItemManager(ham_cheese_toastie).add_item()
ItemManager(pumpkin_soup).add_item()
ItemManager(egg_tart).add_item()

# ---------------- WATER ---------------- #

singha_water_750ml = Item(
    name='Singha Bottled Water (750ml)',
    category='water',
    price=89.00,
    weight=12,
    unit_of_measurement='piece',
    purveyor='Gourmet Market',
    month_ordered=2)

singha_water_1500ml = Item(
    name='Singha Bottled Water (1L)',
    category='water',
    price=55.00,
    weight=6,
    unit_of_measurement='piece',
    purveyor='Big C',
    month_ordered=2)

ItemManager(singha_water_750ml).add_item()
ItemManager(singha_water_1500ml).add_item()


# ---------------- TESTS ---------------- #


# '''ADD_ITEM() TESTING and GET_INVENTORY() TESTING...'''
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


# '''REMOVE_ITEM() TESTING...'''
#
# '''SUCCESSFUL'''
# print(get_inventory() + "\n")
# ItemManager(lavazza_dark_roast).remove_item()
# print("\n" + get_inventory())
#
# '''UNSUCCESSFUL'''
# print(get_inventory())
# print()
# ItemManager(test_item).remove_item()


# '''GET_CATEGORIES() TESTING...'''
#
# print()
# print(get_categories())


# '''GET_ALL_ITEMS() TESTING...'''
#
# print()
# print(get_all_items())


# '''NO CHECKED_IN OR CHECKED_OUT TESTING...'''
#
# print(lavazza_medium_roast)
# print()


# '''GET_ITEMS_IN_CATEGORY() TESTING...'''
#
# '''SUCCESSFUL'''
# print(get_inventory())
# print()
# print(get_items_in_category('water'))
# print()
#
# '''UNSUCCESSFUL'''
# print(get_inventory())
# print()
# print(get_items_in_category('test'))
# print()


# '''GET_ITEM_COUNT() TESTING'''
#
# print(get_item_count('Lavazza Dark Roast'))


# '''GET_FULL_INVENTORY_SUM() TESTING...'''
#
# print(get_full_inventory_sum())
