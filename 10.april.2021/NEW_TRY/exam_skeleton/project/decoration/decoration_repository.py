class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        self.decorations.remove(decoration)

    def find_by_type(self, decoration_type):
        for decoration in reversed(self.decorations):
            if decoration.type == decoration_type:
                self.decorations.remove(decoration)
                return decoration
        return 'None'
