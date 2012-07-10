from flaskext.script import Manager

from project_name import app, db

manager = Manager(app)

@manager.command
def syncdb():
    print "Running db.create_all()..."
    db.create_all()


if __name__ == "__main__":
    manager.run()
