from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<users {self.id}>"


@app.route("/painting")
def p():
    return render_template("painting.html")


@app.route("/historic")
def h():
    return render_template("historic.html")


@app.route("/science")
def s():
    return render_template("science.html")


@app.route("/art")
def a():
    return render_template("art.html")


@app.route("/main_file")
def main_file():
    return render_template("main_file.html")


@app.route("/", methods=("POST", "GET"))
def index():
    if request.method == "POST":
        name = request.form["name"]
        psw = request.form["psw"]

        login = Users.query.filter_by(name=name, password=psw).first()
        if login is not None:
            return redirect(url_for("main_file"))
    print('Нет такого аккаунта')
    return render_template("login.html")


@app.route("/registration", methods=("POST", "GET"))
def register():
    if request.method == "POST":
        try:
            name = request.form['name']
            psw = request.form['psw']

            reg = Users(name=name, password=psw)
            db.session.add(reg)
            db.session.commit()
            print('Успешная регистрация')
            return redirect(url_for("main_file"))
        except:
            db.session.rollback()
            print('Уже есть такой аккаунт')

    return render_template("registration.html", title="Регистрация")


if __name__ == '__main__':
    app.run(debug=True)
