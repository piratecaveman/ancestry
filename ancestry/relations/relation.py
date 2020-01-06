class Relation(object):
    """
    A relationship
    """
    instances = dict()

    def __init__(self, first_person, relation, second_person):
        self.first_person = first_person
        self.second_person = second_person
        self.relation = relation
        Relation.instances[self.__hash__()] = self

    def __hash__(self) -> int:
        return hash((self.first_person, self.relation, self.second_person))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Relation):
            return False
        return self.digest == other.digest

    @property
    def digest(self) -> int:
        return self.__hash__()
