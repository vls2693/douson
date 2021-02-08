from commom_calc.base import receiver
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    name1 = str(request.form['name1'])
    sum1 = int(request.form['sum1'])
    name2 = str(request.form['name2'])
    sum2 = int(request.form['sum2'])
    name3 = str(request.form['name3'])
    sum3 = int(request.form['sum3'])
    name4 = str(request.form['name4'])
    sum4 = int(request.form['sum4'])
    name5 = str(request.form['name5'])
    sum5 = int(request.form['sum5'])
    name6 = str(request.form['name6'])
    sum6 = int(request.form['sum6'])
    name7 = str(request.form['name7'])
    sum7 = int(request.form['sum7'])

    receiver(person1=name1, person2=name2, person3=name3, person4=name4,
             person5=name5, person6=name6, person7=name7, spent1=sum1, spent2=sum2,
             spent3=sum3, spent4=sum4, spent5=sum5, spent6=sum6, spent7=sum7)

    return redirect(url_for('results'))


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
