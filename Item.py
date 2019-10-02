class Item(object):
    id : int = 0

    def __init__(self, name : str = None):
        if name:
            self.name : str = f"{name.capitalize()}"
        self.id : int = Item.id+1 
        Item.id += 1
