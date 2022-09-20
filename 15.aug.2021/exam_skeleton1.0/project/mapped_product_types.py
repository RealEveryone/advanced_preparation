from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable

food_dict = {
    'Bread': Bread,
    'Cake': Cake
}
drink_dict = {
    'Tea': Tea,
    'Water': Water
}
table_dict = {
    'InsideTable': InsideTable,
    'OutsideTable': OutsideTable
}
