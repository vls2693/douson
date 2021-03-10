from commom_calc.base import receiver
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    whole_dict = request.form
    receiver(whole_dict)
    # return redirect(url_for('results'))
    # return render_template('file.html')
    return render_template('result.html')


@app.route("/results")
def results():
    return render_template('file.html')


if __name__ == "__main__":
    app.run()


# http://thewebland.net/development/python/flask/mega-tutorial-part-1-hello-world/
# https://code.tutsplus.com/ru/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
'''
пример добавления строки в форму
http://www.html.by/threads/13985-Dobavlenie-polej-formy-po-nazhatiju-na-knopku
'''
