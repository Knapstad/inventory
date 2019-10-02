class Item(object):
    id: int = 0

    def __init__(
        self,
        name: str = None,
        state: str = None,
        id: int = None,
        quantity: int = None,
        location: "location" = None,
    ):
        if name:
            self.name: str = f"{name.capitalize()}"
        else:
            self.name = name
        if id:
            self.id: int = id
        else:
            self.id: int = Item.id + 1
            Item.id += 1
        self.state: str = state
        self.quantity: int = quantity
        self.location: "location" = location

    def get_location():
        return self.location

    def get_state():
        return self.state

    def get_quantity():
        return self.quantity

    @classmethod
    def from_dict(cls, dict):
        return cls(
            name=dict["name"],
            state=dict["state"],
            id=dict["id"],
            quantity=dict["quantity"],
            location=dict["location"],
        )

    def to_dict(self):
        return self.__dict__
