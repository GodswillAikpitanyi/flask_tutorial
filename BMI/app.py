#python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_prog():
    bmi = ''
    name = ''
    if request.method == 'POST' and 'user_weight' in request.form:
        name = (request.form.get('username'))
        weight = float(request.form.get('user_weight'))
        height = float(request.form.get('user_height'))
        bmi = calc_bmi(weight, height)

    return render_template("index.html",
                           bmi=bmi,
                           name=name)

def calc_bmi(weight, height):
    height = ((height / 100) ** 2)
    return round((weight / height), 2)


app.run()

