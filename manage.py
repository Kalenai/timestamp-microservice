from flask_script import Manager
from app import app


manager = Manager(app)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', debug=True)
    manager.run()
