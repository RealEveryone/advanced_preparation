from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result = 0
        for room in self.rooms:
            result += room.total_expenses()
        return f'Monthly consumption: {result:.2f}$.'

    def pay(self):
        result = []
        for room in self.rooms:
            budget = room.budget
            cost = room.total_expenses()
            if cost > budget:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
            elif cost <= budget:
                room.budget -= cost
                result.append(f"{room.family_name} paid {cost:.2f}$ and have {room.budget:.2f}$ left.")
        return '\n'.join(result)

    def total_population(self):
        result = 0
        for room in self.rooms:
            increment = room.total_members_count()
            result += increment
        return result

    def status(self):
        output = f'Total population: {self.total_population()}\n'
        for room in self.rooms:
            output += f'{room.family_name} with {room.total_members_count()} members. ' \
                      f'Budget: {room.budget:.2f}$, Expenses: {(room.total_expenses() - room.room_cost):.2f}$\n'
            if room.children:
                for idx, child in enumerate(room.children):
                    output += f'--- Child {idx + 1} monthly cost: {child.get_monthly_expense():.2f}$\n'
            room_appliances = [appliance.get_monthly_expense() for appliance in room.appliances]
            output += f'--- Appliances monthly cost: {sum(room_appliances):.2f}$\n'
        return output.strip()
