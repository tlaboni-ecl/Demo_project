from graphql import GraphQLError
from .models import Event, Location, EventMember
from .schema1 import UserType
import graphene
from graphene_django import DjangoObjectType


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class LocationType(DjangoObjectType):
    class Meta:
        model = Location


class EventMemberType(DjangoObjectType):
    class Meta:
        model = EventMember


class Query(graphene.ObjectType):
    locations = graphene.List(LocationType)
    events = graphene.List(EventType)
    event_members = graphene.List(EventMemberType)
    event_member = graphene.Field(EventMemberType, id=graphene.Int())

    def resolve_locations(self, info):
        return Location.objects.all()

    def resolve_events(self, info, **kwargs):
        return Event.objects.all()

    def resolve_event_members(self, info, **kwargs):
        return EventMember.objects.all()

    def resolve_event_member(self, info, **kwargs):
        id = kwargs.get('id')
        user = kwargs.get('user')
        if id is not None:
            return EventMember.objects.get(id=id)
        return None


class CreateEventMember(graphene.Mutation):
    user = graphene.Field(UserType)
    event = graphene.Field(EventType)

    class Arguments:
        event_id = graphene.ID(required=True)

    def mutate(self, info, event_id):
        user = info.context.user

        if user.is_anonymous:
            raise GraphQLError("Need to Log in")
        event = Event.objects.get(id=event_id)
        if not event:
            raise GraphQLError('Cannot find event with given event id')
        EventMember.objects.create(
            user=user,
            event=event
        )
        return CreateEventMember(user=user, event=event)


class UpdateLocation(graphene.Mutation):
    location = graphene.Field(LocationType)

    class Arguments:
        location_id = graphene.Int(required=True)
        latitude = graphene.Float()
        altitude = graphene.Float()

    def mutate(self, info, location_id, latitude, altitude):
        location = Location.objects.get(id=location_id)
        location.latitude = latitude
        location.altitude = altitude
        location.save()
        return UpdateLocation(location=location)


class DeleteEvent(graphene.Mutation):
    event_id = graphene.Int()

    class Arguments:
        event_id = graphene.Int(required=True)

    def mutate(self, info, event_id):
        event = Event.objects.get(id=event_id)
        event.delete()
        return DeleteEvent(event_id=event_id)


class Mutation(graphene.ObjectType):
    update_location = UpdateLocation.Field()
    delete_event = DeleteEvent.Field()
    create_event_member = CreateEventMember.Field()
