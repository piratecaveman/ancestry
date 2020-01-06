class Node(object):
    """
    Base for a person class
    """
    instances = dict()

    def __init__(self, name: str, gender: str):
        self.name = name
        self.__assigned_gender = gender.lower()
        self.gender = gender.lower()
        Node.instances[self.__hash__()] = self

    def __hash__(self) -> int:
        return hash((self.name, self.__assigned_gender))

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.name == other.name and self.gender == other.gender

    def change_gender(self, gender: str) -> bool:
        if gender.lower() in ('male', 'female'):
            self.gender = gender.lower()
            return True
        return False

    @property
    def digest(self) -> int:
        return self.__hash__()

    @property
    def gender_at_init(self) -> str:
        return self.__assigned_gender
