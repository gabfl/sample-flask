from flask import Flask, render_template
from models.users import User

app = Flask(__name__)


@app.route('/')
def hp():
    """Basic route with no template"""
    return """
        <ul>
            <li><a href="/hello">Hello<a></li>
            <li><a href="/world">world<a></li>
            <li><a href="/users">list of users</a></li>
            <li><a href="/user/0">Get one user</a> or <a href="/user/1">Another one</a></li>
        </ul>
    """


@app.route('/hello')
def hello():
    """Basic route with a template"""
    return render_template('hello.html')


@app.route('/world')
def world():
    """Basic route with a template"""
    return render_template('world.html')


@app.route('/users')
def users():
    u = User()
    return render_template('users.html', users=u.getUsers())


@app.route('/user/<int:user_id>')
def user(user_id):
    u = User()
    return render_template('user.html', user=u.getUser(user_id))


if __name__ == '__main__':
    app.run()
