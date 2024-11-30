# p-adic Absolute Value

This is a tiny [flask](https://flask.palletsprojects.com/en/stable/) application to calculate the p-adic absolute-value of a rational number.

`p_adic_compute` contains the computation functions.  `p_adic_abs` is the old version.

The function `p_adic_abs` takes a prime $p$ and a rational number $x$ as its arguments, and returns the 
p-adic absolute value $|x|_p$ as:
- an integer, when the answer is a whole number
- a string expressed as a ratio of integer a/b, when the answer is a float

Example:

    import p_adic_compute as p
    
    p.p_adic_abs(5, 1/200)
    25
    
    p.p_adic_abs(5, 200)
    '1/25'

Floats are converted to an integer ratio with the `fractions` package.  This is chosen to analyze the result for pedagogical rather than computational purposes.  This will be refactored so that either version can be chosen.

`p_adic_view.html` is the Jinja view template.
`p_adic_model.html` is a [WTForms](https://wtforms.readthedocs.io/en/3.2.x/) Form subclass.  This will be updated to a [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/) FlaskForm subclass to include CSRF protection.
`p_adic_controller.html` contains the app logic.
