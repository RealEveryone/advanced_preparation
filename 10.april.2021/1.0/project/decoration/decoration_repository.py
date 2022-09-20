class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        self.decorations.remove(decoration)

    def find_by_type(self, decoration_type):
        for decoration in reversed(self.decorations):
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return 'None'

