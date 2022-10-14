import graphene
from graphene import ObjectType


class Query(ObjectType):
    hello = graphene.String(default_value='HI!')
schema = graphene.Schema(query=Query)