class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *args):
        added_players = []
        for current_player in args:
            if current_player not in self.players:
                self.players.append(current_player)
                added_players.append(current_player.name)
        return f'Successfully added: {", ".join(added_players)}'

    def find_last_supply_and_return_if_exists(self, given_type):
        for idx in range(len(self.supplies)-1, 0, -1):
            if type(self.supplies[idx]).__name__ == given_type:
                return self.supplies.pop(idx)
        return 0

    def find_player_by_name(self, given_name):
        for player in self.players:
            if player.name == given_name:
                return player
        return None

    def add_supply(self, *args):
        self.supplies.extend(list(args))

    def sustain(self, player_name, sustenance_type):
        player = self.find_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type not in ['Food', 'Drink']:
            return
        supply = self.find_last_supply_and_return_if_exists(sustenance_type)
        if supply == 0:
            raise Exception(f'There are no {sustenance_type.lower()} supplies left!')
        if player.need_sustenance is False:
            return f"{player_name} have enough stamina."     # Possible change which is first
        player.sustain_self(supply.energy)
        return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def players_status(*args):
        output = ''
        for player in args:
            if player.stamina == 0:
                output += f"Player {player.name} does not have enough stamina.\n"
        return output.strip()

    @staticmethod
    def determine_players_by_stamina(pl1, pl2):
        if pl1.stamina > pl2.stamina:
            return pl2, pl1
        return pl1, pl2

    def duel(self, first_player_name, second_player_name):
        current_player, other_player = self.find_player_by_name(first_player_name), \
                                       self.find_player_by_name(second_player_name)
        premature_termination = self.players_status(current_player, other_player)
        if len(premature_termination) > 0:
            return premature_termination
        current_player, other_player = self.determine_players_by_stamina(current_player, other_player)

        for _ in range(2):
            current_player_attack_damage = current_player.stamina / 2
            other_player.decrease_stamina(current_player_attack_damage)
            if other_player.stamina <= 0:
                return f"Winner: {current_player.name}"
            current_player, other_player = other_player, current_player

        loser, winner = self.determine_players_by_stamina(current_player, other_player)
        return f"Winner: {winner.name}"

    def next_day(self):
        for pl in self.players:
            pl.decrease_stamina(pl.age * 2)
            self.sustain(pl.name, 'Food')
            self.sustain(pl.name, 'Drink')

    def __str__(self):
        output = ''
        for player in self.players:
            output += (str(player)) + '\n'
        for supply in self.supplies:
            output += (supply.details()) + '\n'
        return output.strip()






