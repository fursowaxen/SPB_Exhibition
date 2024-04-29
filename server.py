from flask import render_template, redirect, url_for, request
from users_class import Users, app, db


@app.route("/painting")
def paint():
    return render_template("painting.html")


@app.route("/historic")
def hist():
    return render_template("historic.html")


@app.route("/science")
def scien():
    return render_template("science.html")


@app.route("/art")
def art():
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
            print('Ошибка регистрации (скорее всего, такой аккаунт уже существует)')

    return render_template("registration.html", title="Регистрация")


if __name__ == '__main__':
    app.run(debug=True)
