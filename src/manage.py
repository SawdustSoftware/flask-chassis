from chassis import create_app, models
import factories
from flask.ext.script import Manager, Shell

app = create_app()
manager = Manager(app)


def _make_context():
        return dict(app=app, db=models.db, models=models, factories=factories)

manager.add_command("shell", Shell(make_context=_make_context))


@manager.option("-n", help="Number of dummy things")
def dummy(n=10):
    """Generate dummy data."""
    if not app.debug:
        raise Exception("Unsafe to generate dummy data while not in DEBUG.")

    ids = []
    for x in xrange(0, int(n)):
        m = factories.Cat()
        ids.append(m.id)
    models.db.session.commit()

    print "Inserted these ids:"
    for x in ids:
        print x


if __name__ == "__main__":
    manager.run()
