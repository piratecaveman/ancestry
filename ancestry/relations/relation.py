from ancestry.person.node import Node


class Relation(object):
    """
    A relationship
    """
    instances = dict()

    def __init__(self, first_person: Node, relation: str, second_person: Node, paternal: bool = True):
        self.first_person = first_person
        self.second_person = second_person
        self._relation = relation.lower()
        self.paternal = paternal
        Relation.instances[self.__hash__()] = self

    @property
    def relation(self):
        if self._relation in ('uncle', 'aunt', 'grandfather', 'grandmother'):
            if self.paternal:
                self._relation = f'paternal {self._relation}'
            else:
                self._relation = f'maternal {self._relation}'
        string = self._relation.replace(' ', '_')
        return string

    def __hash__(self) -> int:
        return hash((self.first_person, self.relation, self.second_person))

    def __eq__(self, other) -> bool:
        if not isinstance(other, Relation):
            return False
        return self.digest == other.digest

    @property
    def digest(self) -> int:
        return self.__hash__()

    @staticmethod
    def _repr_string(string: str) -> str:
        static = string.replace('_', ' ')
        return static

    def __repr__(self):
        return f'{self.first_person.name} is the {self._repr_string(self.relation)} of {self.second_person.name}'

    @property
    def is_recognized(self) -> bool:
        static = (
            'husband',
            'wife',
            'brother',
            'sister',
            'paternal_grandfather',
            'maternal_grandfather',
            'paternal_grandmother',
            'maternal_grandmother',
            'son',
            'daughter',
            'grandson',
            'granddaughter',
            'cousin',
            'paternal_uncle',
            'maternal_uncle',
            'paternal_aunt',
            'maternal_aunt',
            'nephew',
            'niece',
            'son-in-law',
            'daughter-in-law',
            'father-in-law',
            'mother-in-law'
            'brother-in-law',
            'sister-in-law',
        )
        if self.relation in static:
            return True
        else:
            raise ValueError(f'The relation {self._repr_string(self.relation)} is not recognized')
