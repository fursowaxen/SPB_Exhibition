from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<users {self.id}>"


@app.route("/painting", methods=("POST", "GET"))
def p():
    return render_template("painting.html")


@app.route("/historic", methods=("POST", "GET"))
def h():
    return render_template("hictoric.html")


@app.route("/science", methods=("POST", "GET"))
def s():
    return render_template("science.html")


@app.route("/art", methods=("POST", "GET"))
def a():
    return render_template("art.html")


@app.route("/main_file", methods=("POST", "GET"))
def main_page():
    return render_template("main_file.html")


@app.route("/", methods=("POST", "GET"))
def index():
    return render_template("login.html")

#
# @app.route("/register", methods=("POST", "GET"))
# def register():
#     if request.method == "POST":
#         # здесь должна быть проверка корректности введенных данных
#         try:
#             hash = generate_password_hash(request.form['password'])
#             u = Users(name=request.form['email'], password=hash)
#             db.session.add(u)
#             db.session.flush()
#             db.session.commit()
#         except:
#             db.session.rollback()
#             print("Ошибка добавления в БД")
#
#     return render_template("registration.html", title="Регистрация")



@app.route("/register", methods=("POST", "GET"))
def register():
    return render_template("registration.html", title="Регистрация")


if __name__ == "__main__":
    app.run(debug=True)

# from werkzeug.security import generate_password_hash
# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
#
# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(50), unique=True)
#     psw = db.Column(db.String(500), nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#
#     pr = db.relationship('Profiles', backref='users', uselist=False)
#
#     def __repr__(self):
#         return f"<users {self.id}>"
#
#
# class Profiles(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=True)
#     old = db.Column(db.Integer)
#     city = db.Column(db.String(100))
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     def __repr__(self):
#         return f"<profiles {self.id}>"
#
#
# @app.route("/painting", methods=("POST", "GET"))
# def p():
#     return render_template("painting.html")
#
#
# @app.route("/historic", methods=("POST", "GET"))
# def h():
#     return render_template("hictoric.html")
#
#
# @app.route("/science", methods=("POST", "GET"))
# def s():
#     return render_template("science.html")
#
#
# @app.route("/art", methods=("POST", "GET"))
# def a():
#     return render_template("art.html")
#
#
# @app.route("/main_file", methods=("POST", "GET"))
# def main_page():
#     return render_template("main_file.html")
#
#
# @app.route("/", methods=("POST", "GET"))
# def index():
#     return render_template("login.html")
#
#
# #
# # @app.route("/")
# # def index():
# #     info = []
# #     try:
# #         info = Users.query.all()
# #     except:
# #         print("Ошибка чтения из БД")
# #
# #     return render_template("index.html", title="Главная", list=info)
#
#
# @app.route("/register", methods=["POST", "GET"])
# def register():
#     if request.method == "POST":
#         # здесь должна быть проверка корректности введенных данных
#         try:
#             hash = generate_password_hash(request.form['psw'])
#             u = Users(email=request.form['email'], psw=hash)
#             db.session.add(u)
#             db.session.flush()
#
#             p = Profiles(name=request.form['name'], old=request.form['old'],
#                          city=request.form['city'], user_id=u.id)
#             db.session.add(p)
#             db.session.commit()
#         except:
#             db.session.rollback()
#             print("Ошибка добавления в БД")
#
#     return render_template("registration.html", title="Регистрация")
#
#
# if __name__ == "__main__":
#     app.run(debug=True)
