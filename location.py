class Location(object):
    def __init__(self):
        self.inventory: list = []
        self.name: str = "not set"

    def __len__(self):
        return len(self.inventory)

    def __getitem__(self, position):
        return self.inventory[position]

    def __reversed__(self):
        return self[::-1]

    def add_item(self, item):
        self.inventory.append(item)
    
    def remove_item(self, item):
        try:
            self.inventory.remove(item)
        except ValueError as e:
            print(f"{item} er ikke i {self.name}")
            
    