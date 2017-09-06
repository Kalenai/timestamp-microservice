from flask_script import Manager
import unittest
from app import app

manager = Manager(app)


@manager.command
def test():
    tests = unittest.TestLoader().discover('tests', pattern='tests.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
