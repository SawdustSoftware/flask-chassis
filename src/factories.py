from chassis.models import db
from chassis import models

from faker import Factory as Fake
from factory.alchemy import SQLAlchemyModelFactory
import factory

import logging

#Suppress factory-boy debug data
factory_log = logging.getLogger("factory")
factory_log.setLevel(logging.WARNING)

faker = Fake.create()


class Cat(SQLAlchemyModelFactory):
    FACTORY_FOR = models.Cat
    FACTORY_SESSION = db.session

    id = factory.LazyAttribute(lambda x: faker.unixTime())
    born_at = factory.LazyAttribute(lambda x: faker.unixTime())

    name = factory.LazyAttribute(lambda x: faker.firstName())
