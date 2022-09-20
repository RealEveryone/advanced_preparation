from project.bakery import Bakery

bakery = Bakery('Sladkarnica')
print(bakery.add_food('Cake', 'Pasta', 10.50))
print(bakery.add_food('Cake', 'GolqmaPast', 14.50))
print(bakery.add_food('Bread', 'Sandvich', 6.50))
print(bakery.add_food('Bread', 'GolqmSandvich', 9))

print(bakery.add_drink('Water', 'StudenaVoda', 250, 'IceB'))
print(bakery.add_table('OutsideTable', 78, 12))
print(bakery.add_table('OutsideTable', 52, 8))
print(bakery.add_table('InsideTable', 12, 4))

print(bakery.reserve_table(10))
print(bakery.reserve_table(7))
print(bakery.reserve_table(4))

print(bakery.order_food(78, 'Pasta', 'GolqmaPast', 'GolqmSandvich', 'Pie', 'PileshkaSupa'))
print(bakery.order_drink(78, 'StudenaVoda', 'GaziranaVoda'))

print(bakery.order_food(52, 'Pasta', 'GolqmaPast'))
print(bakery.order_drink(52, 'StudenaVoda'))

print(bakery.leave_table(78))
print(bakery.leave_table(52))

print(bakery.get_free_tables_info())
print(bakery.get_total_income())
