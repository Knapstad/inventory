class Item(object):
    id : int = 0

    def __init__(self, name : str = None):
        if name:
            self.name : str = f"{name.capital()}"
        self.id : int = id+1 
        id += 1
    
    
