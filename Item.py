class Item(object):
    id : int = 0

    def __init__(self, name : str = None):
        if name:
            self.name : str = f"{name.capitalize()}"
        self.id : int = Item.id+1 
        Item.id += 1
        self.state: str 
        self.quantity: int
        self.location: "location"
        
        def get_location():
            return self.location

        def get_state():
            return self.state

        def get_quantity():
            return self.quantity

        
