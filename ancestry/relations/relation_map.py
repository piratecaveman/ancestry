from ancestry.relations.relation import Relation


class RelationMap(object):
    """
    A static relation map
    """
    def __init__(self):
        self._relations = dict()

    def add_relation(self, first_person, relation, second_person):
        u_id = hash((first_person, relation, second_person))
        if u_id in Relation.instances:
            if u_id not in self._relations:
                self._relations[u_id] = Relation.instances[u_id]
            else:
                pass
        else:
            self._relations[u_id] = Relation(first_person, relation, second_person)
