import typing


from ancestry.relations.relation import Relation


class RelationMapper(object):
    """
    A static relation map
    """
    def __init__(self):
        pass

    @staticmethod
    def find_inverse_of(relation: Relation, paternal: bool = True) -> typing.Union[str, tuple]:
        static = {
            'husband': ('wife',),
            'wife': ('husband',),
            'son': ('father', 'mother'),
            'daughter': ('father', 'mother'),
            'father': ('son', 'daughter'),
            'mother': ('son', 'daughter'),
            'brother': ('brother', 'sister'),
            'sister': ('brother', 'sister'),
            'cousin': ('cousin',),
            'paternal_grandfather': ('grandson', 'granddaughter'),
            'maternal_grandfather': ('grandson', 'granddaughter'),
            'paternal_grandmother': ('grandson', 'granddaughter'),
            'maternal_grandmother': ('grandson', 'granddaughter'),
            'grandson': (
                'paternal_grandfather',
                'maternal_grandfather',
                'paternal_grandmother',
                'maternal_grandmother'
            ),
            'granddaughter': (
                'paternal_grandfather',
                'maternal_grandfather',
                'paternal_grandmother',
                'maternal_grandmother'
            ),
            'paternal_uncle': ('nephew', 'niece'),
            'maternal_uncle': ('nephew', 'niece'),
            'paternal_aunt': ('nephew', 'niece'),
            'maternal_aunt': ('nephew', 'niece'),
            'nephew': ('paternal_uncle', 'maternal_uncle', 'paternal_aunt', 'maternal_aunt'),
            'niece': ('paternal_uncle', 'maternal_uncle', 'paternal_aunt', 'maternal_aunt'),
            'father-in-law': ('son-in-law', 'daughter-in-law'),
            'mother-in-law': ('son-in-law', 'daughter-in-law'),
            'son-in-law': ('father-in-law', 'mother-in-law'),
            'daughter-in-law': ('father-in-law', 'mother-in-law'),
            'brother-in-law': ('brother-in-law', 'sister-in-law'),
            'sister-in-law': ('brother-in-law', 'sister-in-law')
        }
        gender = relation.second_person.gender
        paternal = paternal if paternal else relation.paternal
        if gender == 'male':
            if len(static[relation.relation]) > 2:
                if paternal:
                    return static[relation.relation][0]
                else:
                    return static[relation.relation][1]
            elif len(static[relation.relation]) == 2:
                return static[relation.relation][0]
            else:
                return static[relation.relation][0]
        elif gender == 'female':
            if len(static[relation.relation]) > 2:
                if paternal:
                    return static[relation.relation][2]
                else:
                    return static[relation.relation][3]
            elif len(static[relation.relation]) == 2:
                return static[relation.relation][1]
            else:
                return static[relation.relation][0]
        else:
            return static[relation.relation]

    def inverse_of(self, relation: Relation, paternal: bool = True) -> typing.Union[Relation, tuple]:
        inverse = self.find_inverse_of(relation, paternal)
        if relation.second_person.gender == 'unknown':
            return inverse
        u_id = hash((relation.second_person, inverse, relation.first_person))
        if u_id in Relation.instances:
            return Relation.instances[u_id]
        else:
            relation = Relation(relation.second_person, inverse, relation.first_person, paternal)
            return relation
