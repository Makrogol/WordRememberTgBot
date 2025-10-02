class UserIdentifierData:
    def __init__(self, id: int = None, name: str = None):
        if id is None:
            id = 0
        if name is None:
            name = ''
        self.name = name
        self.id = id

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }

    def __str__(self) -> str:
        return str(self.id) + ' ' + self.name

    def __eq__(self, other: 'UserIdentifierData') -> bool:
        return self.id == other.id and self.name == other.name
