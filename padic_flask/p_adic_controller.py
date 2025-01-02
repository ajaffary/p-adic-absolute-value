import os
from flask import Flask, request, url_for, render_template
from p_adic_compute import p_adic_abs
from p_adic_model import InputForm
from flask_wtf.csrf import CSRFProtect
# import gunicorn

# The web application is the app object of class Flask.
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
csrf = CSRFProtect(app) 

# route decorator
@app.route('/', methods=['GET', 'POST'])
def p_adic_view():
    input_form = InputForm(request.form)

    if request.method == 'POST' and input_form.validate():
        prime = input_form.prime.data
        rational = input_form.rational.data
        result = p_adic_abs(prime, rational)
    else:
        result = None
    
    return render_template("p_adic_view.html", form=input_form, result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    # app.run(debug=True)