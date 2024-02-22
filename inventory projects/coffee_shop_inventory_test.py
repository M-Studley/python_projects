from coffee_shop_inventory import *

# ---------------- TESTING OBJECT ---------------- #

test_item = Item(
    name='test item',
    category='test category',
    item_count=1,
    price=999.99,
    weight=99,
    unit_of_measurement='test unit',
    purveyor='test purveyor',
    month_ordered=13)

# ItemManager.add_item(test_item)

# ---------------- COFFEE BEANS ---------------- #

lavazza_dark_roast = Item(
    name='lavazza dark roast',
    category='coffee beans',
    item_count=1,
    price=1690.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='lazada',
    month_ordered=2,
    checked_in=47,
    checked_out=60)

lavazza_medium_roast = Item(
    name='lavazza medium roast',
    category='coffee beans',
    item_count=1,
    price=1590.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='lazada',
    month_ordered=2)

lavazza_light_roast = Item(
    name='lavazza light roast',
    category='coffee beans',
    item_count=1,
    price=1490.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='lazada',
    month_ordered=2,
    checked_in=47,
    checked_out=60)

ItemManager.add_item(lavazza_dark_roast)
ItemManager.add_item(lavazza_medium_roast)
ItemManager.add_item(lavazza_light_roast)

# ---------------- DAIRY ---------------- #

heavy_cream = Item(
    name='heavy cream',
    category='dairy',
    item_count=1,
    price=279.00,
    weight=1000,
    unit_of_measurement='ml',
    purveyor='makro',
    month_ordered=2)

whole_milk = Item(
    name='milk (whole)',
    category='dairy',
    item_count=1,
    price=95.00,
    weight=1000,
    unit_of_measurement='ml',
    purveyor='makro',
    month_ordered=2)

ItemManager.add_item(heavy_cream)
ItemManager.add_item(whole_milk)

# ---------------- DRY GOODS ---------------- #

white_sugar = Item(
    name='sugar (white)',
    category='dry goods',
    item_count=1,
    price=38.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='shopee',
    month_ordered=2)

brown_sugar = Item(
    name='sugar (brown)',
    category='dry goods',
    item_count=1,
    price=55.00,
    weight=1000,
    unit_of_measurement='g',
    purveyor='shopee',
    month_ordered=2)

ItemManager.add_item(white_sugar)
ItemManager.add_item(brown_sugar)

# ---------------- PAPER GOODS ---------------- #

beverage_napkins = Item(
    name='beverage napkins (black)',
    category='paper goods',
    item_count=1,
    price=59.00,
    weight=200,
    unit_of_measurement='piece',
    purveyor='makro',
    month_ordered=2)

branded_napkins = Item(
    name='branded napkins (white)',
    category='paper goods',
    item_count=1,
    price=120.00,
    weight=100,
    unit_of_measurement='piece',
    purveyor='fancy napkin co.',
    month_ordered=2)

ItemManager.add_item(beverage_napkins)
ItemManager.add_item(branded_napkins)

# ---------------- READY TO EAT ---------------- #

ham_cheese_toastie = Item(
    name='ham & cheese toastie',
    category='ready to eat',
    item_count=1,
    price=1560.00,
    weight=40,
    unit_of_measurement='piece',
    purveyor='makro',
    month_ordered=2)

pumpkin_soup = Item(
    name='soup (pumpkin)',
    category='ready to eat',
    item_count=1,
    price=1160.00,
    weight=3785,
    unit_of_measurement='ml',
    purveyor='makro',
    month_ordered=2)

egg_tart = Item(
    name='tart (egg)',
    category='ready to eat',
    item_count=1,
    price=960.00,
    weight=20,
    unit_of_measurement='piece',
    purveyor='tops supermarket',
    month_ordered=2)

ItemManager.add_item(ham_cheese_toastie)
ItemManager.add_item(pumpkin_soup)
ItemManager.add_item(egg_tart)

# ---------------- WATER ---------------- #

singha_water_750ml = Item(
    name='singha bottled water (750ml)',
    category='water',
    item_count=1,
    price=89.00,
    weight=12,
    unit_of_measurement='piece',
    purveyor='big c',
    month_ordered=2)

singha_water_1000ml = Item(
    name='singha bottled water (1L)',
    category='water',
    item_count=1,
    price=55.00,
    weight=6,
    unit_of_measurement='piece',
    purveyor='big c',
    month_ordered=2)

ItemManager.add_item(singha_water_750ml)
ItemManager.add_item(singha_water_1000ml)


'''-------------------------------- TESTS --------------------------------'''


'''ADD_ITEM() TESTING...'''
#
# print()
# print(full_inventory)
# print()
# ItemManager.add_item(lavazza_dark_roast)
# print(full_inventory['lavazza dark roast'])


'''REMOVE_ITEM() TESTING...'''
#
'''SUCCESSFUL'''
# print()
# print(full_inventory['lavazza dark roast'])
# print()
# ItemManager.remove_item('lavazza dark roast')
# print(full_inventory['lavazza dark roast'])
# print()
# print("\n" + InventoryManager.get_inventory())
#
'''UNSUCCESSFUL'''
# print()
# ItemManager().remove_item('test_item')


'''NO CHECKED_IN OR CHECKED_OUT TESTING...'''
#
# print()
# print(lavazza_medium_roast)


'''CHANGE_CHECKED_IN TESTING...'''
#
# print()
# print("singha 1000:", singha_water_1000ml)
# print()
# print("full inventory:", full_inventory)
# print()
# ItemManager.change_checked_in('singha bottled water (1L)', 49)
# print("singha 1000:", singha_water_1000ml)
# print()
# print("full inventory:", full_inventory)


'''CHANGE_CHECKED_OUT TESTING...'''
#
# print()
# print("singha 1000:", singha_water_1000ml)
# print()
# print("full inventory:", full_inventory)
# print()
# ItemManager.change_checked_out('singha bottled water (1L)', 59)
# print("singha 1000:", singha_water_1000ml)
# print()
# print("full inventory:", full_inventory)


'''GET_INVENTORY() TESTING...'''

# print()
# print(InventoryManager.get_inventory())


'''GET_CATEGORIES() TESTING...'''
#
# print()
# print(InventoryManager.get_categories())


'''GET_PURVEYORS() TESTING...'''
#
# print()
# print(InventoryManager.get_purveyors())


'''GET_ALL_ITEMS() TESTING...'''
#
# print()
# print(InventoryManager.get_all_items())
# print(len(InventoryManager.get_all_items()))\


'''GET_ITEMS_IN_CATEGORY() TESTING...'''
#
'''SUCCESSFUL'''
# print()
# print(InventoryManager.get_items_in_category('coffee beans'))

'''UNSUCCESSFUL'''
# print()
# print(InventoryManager.get_items_in_category('test category'))


'''GET_ITEMS_BY_PURVEYOR() TESTING...'''
#
'''SUCCESSFUL'''
# print()
# print(get_items_in_category('lazada'))

'''UNSUCCESSFUL'''
# print()
# print(get_items_in_category('test category'))


'''GET_ITEM_COUNT() TESTING'''
#
# print()
# print(get_item_count('lavazza dark roast'))


'''GET_FULL_INVENTORY_SUM() TESTING...'''
#
# print()
# print(get_full_inventory_sum())


'''GET_ALL_CATEGORY_SUM() TESTING'''
#
# print()
# print(get_all_category_sum())


'''GET_CATEGORY_SUM() TESTING...'''
#
# print()
# print(get_category_sum('coffee beans'))


'''GET_PURVEYOR_SUM() TESTING...'''
#
# print()
# print(get_purveyor_sum('makro'))


'''GET_ORDER_MONTH_SUM() TESTING...'''
#
# print()
# print(get_order_month_sum(2))
