from commom_calc.base import receiver
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    name1 = str(request.form['name1'])
    summ1 = int(request.form['summ1'])
    name2 = str(request.form['name2'])
    summ2 = int(request.form['summ2'])
    name3 = str(request.form['name3'])
    summ3 = int(request.form['summ3'])
    name4 = str(request.form['name4'])
    summ4 = int(request.form['summ4'])
    name5 = str(request.form['name5'])
    summ5 = int(request.form['summ5'])
    name6 = str(request.form['name6'])
    summ6 = int(request.form['summ6'])
    name7 = str(request.form['name7'])
    summ7 = int(request.form['summ7'])

    receiver(person1=name1, person2=name2, person3=name3, person4=name4,
             person5=name5, person6=name6, person7=name7, spent1=summ1, spent2=summ2,
             spent3=summ3, spent4=summ4, spent5=summ5, spent6=summ6, spent7=summ7)

if __name__ == "__main__":
    app.run()






#http://thewebland.net/development/python/flask/mega-tutorial-part-1-hello-world/
#https://code.tutsplus.com/ru/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
'''
пример добавления строки в форму
http://www.html.by/threads/13985-Dobavlenie-polej-formy-po-nazhatiju-na-knopku
'''