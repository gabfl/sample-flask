from flask_api import FlaskAPI
from models.users import User

app = FlaskAPI(__name__)


@app.route('/users', methods=['GET'])
def users():
    u = User()
    return u.getUsers()


@app.route('/user/<int:user_id>')
def user(user_id):
    u = User()
    return u.getUser(user_id)


if __name__ == '__main__':
    app.run()
