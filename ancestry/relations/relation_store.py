from ancestry.person.node import Node
from ancestry.relations.relation import Relation
from ancestry.relations.relation_map import RelationMapper


class RelationStore(object):
    def __init__(self, first_person: Node):
        self.owner = first_person
        self.mapper = RelationMapper()
        self.store = dict()

    def add_relation(self, relation: str, person: Node) -> bool:
        u_id = hash((self.owner, relation, person))
        if u_id in Relation.instances:
            relation = Relation.instances[u_id]
            if u_id not in self.store:
                self.store[u_id] = relation
        else:
            relation = Relation(self.owner, relation, person)
            self.store[relation.digest] = relation
        inverse_id = self.mapper.inverse_of(relation)
        return True
