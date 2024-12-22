from flask_wtf import FlaskForm
from wtforms import Form, IntegerField, FloatField, StringField, SubmitField, validators
from markupsafe import Markup

# see https://wtforms.readthedocs.io/en/3.1.x/crash_course/

"""
- The model is a special Flask class derived from Form
- the form fields are defined through class variables
- these form field objects correspond to HTML forms in the input page
""" 

class InputForm(Form):
    """
    - the prime variable is an IntegerField since it is an integer variable
    - a default validator checks that the user supplies an integer
    - another validator, InputRequired, which requires a user to enter
    input before submitting
    """
    link = '<a href="#prime_note">[1]</a>'
    prime_label = f'Enter a prime number<sup id="prime_footnote_marker">{link}</sup>:'
    prime = IntegerField(label=Markup(prime_label), 
                         validators=[validators.InputRequired()],
                         id='prime',
                         default=3,
                         render_kw={'aria_label': 'prime', 'min': 2})
    
    """
    - the number variable is a FloatField since it is a floating-point variable
    - a default validator checks that the user supplies a real number
    - again, the InputRequired validator is called
    """
    rational = StringField(label='Enter a rational number:', 
                          validators=[validators.InputRequired()],
                          id='rational',
                          default=75/9,
                          render_kw={'aria_label': 'rational'})
    
    # how does WTForms render value=?
    submit = SubmitField(label='Submit',
                         id='submit',
                         render_kw={'aria_label': 'submit', 'class': 'reverse'})