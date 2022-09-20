from project.controller import Controller

controller = Controller()
print(controller.add_aquarium('FreshwaterAquarium', 'Name'))
print(controller.add_aquarium('FreshAquarium', 'Name'))
print(controller.add_decoration('Ornament'))
print(controller.add_decoration('Decor'))
print(controller.insert_decoration('Name', 'Ornament'))
print(controller.insert_decoration('Name', 'decor'))
print(controller.insert_decoration('Name', 'Decor'))
print(controller.add_fish('Name', 'FreshwaterFish', 'Fish', 'BigFish', 200))
print(controller.add_fish('Name', 'SaltwaterFish', 'Fish', 'BigFish', 200))
for _ in range(49):
    controller.add_fish('Name', 'FreshwaterFish', 'Fish', 'BigFish', 200)
print(controller.add_fish('Name', 'FreshwaterFish', 'Fish', 'BigFish', 200))
print(controller.feed_fish('Name'))
print(controller.calculate_value('Name'))
print(controller.report())
