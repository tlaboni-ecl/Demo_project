import graphene
import graphql_jwt
import myapp.schema
import myapp.schema1


class AllQuery(myapp.schema.Query, graphene.ObjectType):
    pass


class Mutation(myapp.schema1.Mutation,myapp.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=AllQuery,mutation=Mutation)
