from flask.ext.testing import TestCase

from chassis import create_app
from chassis.models import db
import factories


class ChassisTestCase(TestCase):
    """Base TestCase to add in convenience functions, defaults and custom
    asserts."""

    def create_app(self):
        return create_app()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCat(ChassisTestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://:memory:"

    def test_get_cat(self):
        """Test to see if you can get a message by ID."""

        cat = factories.Cat()
        db.session.commit()

        response = self.client.get("/cats/" + str(cat.id))
        self.assert_200(response)
        resp_json = response.json
        self.assertEquals(resp_json["id"], str(cat.id))
        self.assertEquals(resp_json["born_at"], cat.born_at)
        self.assertEquals(resp_json["name"], cat.name)
