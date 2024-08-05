from flask import Flask, render_template
from werkzeug.utils import redirect

from data import db_session
from data.data import Data
from form import Form

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nuBf3or5315147ty3436h56uGjHJVa534343568asYTYFct'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Начальная страница')


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/bootstrap.html')
def bootstrap():
    return render_template('/bootstrap.html', title='Bootstrap страница')


@app.route('/add.html', methods=['GET', 'POST'])
def add():
    f = Form()
    if f.validate_on_submit():
        db_session.global_init("db/database.sqlite")
        session = db_session.create_session()
        d = Data()
        d.name = f.name._value()
        d.text = f.data._value()
        session.add(d)
        session.commit()
        return redirect('/')
    return render_template('/add.html', title='Добавить', form=f)


@app.route('/get.html', methods=['GET'])
def get():
    db_session.global_init("db/database.sqlite")
    session = db_session.create_session()
    return render_template('/get.html', title='Просмотреть', data=session.query(Data).all())


def main():
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
