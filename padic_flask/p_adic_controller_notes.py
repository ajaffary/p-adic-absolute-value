# Flask application to return numerical computation:
# http://hplgit.github.io/web4sciapps/doc/pub/._web4sa_solarized004.html

"""
The compute component is always in a separate file as we like to encapsulate the 
computations completely from user interfaces.

The view that the user sees is determined by HTML templates in a subdirectory 
templates, and consequently we name the template files view*.html. 

The model and other parts of the view concept are just parts of the 
controller.py file. The complete file is short and explained in detail below.

"""

from flask import Flask, render_template, request
from p_adic_compute import p_adic_abs
from p_adic_model import InputForm

"""
The web application is the app object of class Flask, and initialized as shown. 
"""
app = Flask(__name__)

"""
The view part of this Python code consists of a URL and a corresponding function
to call when the URL is invoked. 

The function name is here chosen to be index (inspired by the standard 
index.html page that is the main page of a web app). 

The decorator @app.route('/hw1', ...) maps the URL http://127.0.0.1:5000/hw1 to 
a call to index. The methods argument must be as shown to allow the user to 
communicate with the web page.
"""
# see https://youtu.be/9MHYHgh4jYc?si=k0OCWvki-qxbkPKx
# View
@app.route('/test', methods=['GET', 'POST'])
def index():
    """
    The index function first makes a form object based on the data in the model,
    here class InputForm. Then there are two possibilities: if the user has 
    given data, s is a float, otherwise s is None.

    In the former case, request.method equals 'POST' and we can extract the 
    numerical value of r from the form object, using form.r.data, call up 
    our mathematical computations.

    We use the same template for the input and the output page:
    """
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        prime = form.prime.data
        rational = form.rational.data
        result = p_adic_abs(prime, rational)
    else:
        result = None
    
    # result = '%.5f' % result
    
    return render_template("p_adic_view.html", form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)