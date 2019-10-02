class Location(object):
    def __init__(self):
        self.inventory: list = []
        self.name: str = "not set"

    def __len__(self):
        return len(self.inventory)


    
    def add_item(item):
        self.inventory.append(item)
    
    def remove_item(item):
        try:
            self.inventory.remove(item)
        except ValueError as e:
            print(f"{item} er ikke i {self.name}")
            
    