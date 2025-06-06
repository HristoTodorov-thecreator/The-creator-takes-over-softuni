
class DecorationRepository:

    def __init__(self):
        self.decorations: list  = []

    def add(self,decoration):
        if decoration not in self.decorations:
            self.decorations.append(decoration)
    def remove(self,decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False


    def find_by_type(self,decoration_type: str):
        for d in self.decorations:
            if d.__class__.__name__ == decoration_type:
                return d

        return 'None'

