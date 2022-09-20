class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration: object):
        self.decorations.append(decoration)

    def remove(self, decoration: object):
        if decoration not in self.decorations:
            return False
        self.decorations.remove(decoration)
        return True

    def find_by_type(self, decoration_type: str):
        for decoration in reversed(self.decorations):
            if type(decoration).__name__ == decoration_type:
                return decoration
        return 'None'

