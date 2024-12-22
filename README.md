# p-adic Absolute Value

This is a tiny [Flask](https://flask.palletsprojects.com/en/stable/) application to calculate the [p-adic norm](https://mathworld.wolfram.com/p-adicNorm.html) of a rational number.

1. Install the Flask, WTForms, and flask_wtf packages (see `requirements.txt`).
2. `python p_adic_controller.py` runs the application in a browser at http://127.0.0.1:5000/test.

`p_adic_controller.py` contains the app logic.

`p_adic_view.html` is the Jinja view template.

`p_adic_model.py` is a [WTForms](https://wtforms.readthedocs.io/en/3.2.x/) Form subclass.  This will be updated to a [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/) FlaskForm subclass to include CSRF protection.

`p_adic_compute` contains the computation functions.  `p_adic_abs` is the old version.

The function `p_adic_abs` takes a prime $p$ and a rational number $x$ as its arguments, and returns a dictionary:

    { 
        'valuation': val,
        'float': abs,
        'fraction: to_fraction(abs)
    }

where:

- `val` is the p-adic valuation $val_p(x)$
- `abs` is the p-adic norm $|x|_p$ a float
- `to_fraction(abs)` is a string expressed as a ratio of integer a/b

When `abs` is an integer, it has type `int`. Floats are converted to an integer ratio (with the `fractions` package).  This is for pedagogical rather than computational purposes.  

The web app interface returns the valuation and the fractional representation of the norm. The user can then choose between float or fraction.  A copy to the clipboard button is also provided.

Example in terminal:

    import p_adic_compute as p
    
    p.p_adic_abs(5, 1/200)
    25
    
    p.p_adic_abs(5, 200)
    '1/25'
