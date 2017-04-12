# -*- coding: utf-8 -*-
"""The GraphQL Schema."""
import datetime as dt

import graphene as gql
from graphene.types.datetime import DateTime


class About(gql.ObjectType):
    first_name = gql.String()
    last_name = gql.String()

    birthday = DateTime()

    full_name = gql.String()
    age = gql.Int()

    def resolve_full_name(self, args, context, info):
        return '{} {}'.format(self.first_name, self.last_name)

    def resolve_age(self, args, context, info):
        now = dt.datetime.now()

        return now.year - self.birthday.year \
            - (tuple(now.timetuple())[1:]
               < tuple(self.birthday.timetuple())[1:])


class Query(gql.ObjectType):
    """GraphQL Query."""
    about = gql.Field(About)

    def resolve_about(self, args, context, info):
        return About(first_name='Myles', last_name='Braithwaite',
                     birthday=dt.datetime(1986, 9, 19, 8, 45))


schema = gql.Schema(query=Query)
