# p-adic Norm Calculator

This is a [Flask](https://flask.palletsprojects.com/en/stable/) application to calculate the [p-adic norm](https://mathworld.wolfram.com/p-adicNorm.html) of a rational number.

`p_adic_controller.py` contains the app logic.

`p_adic_view.html` is the Jinja view template.

`p_adic_model.py` is a [WTForms](https://wtforms.readthedocs.io/en/3.2.x/) Form subclass.

`p_adic_compute` contains the computation functions.  `p_adic_abs` is the old version.

The function `p_adic_abs` takes a prime $p$ and a rational number $x$ as its arguments, and returns a dictionary:

    { 
        'valuation': val,
        'float': abs,
        'fraction: to_fraction(abs)
    }

where:

- `val` is the p-adic valuation $val_p(x)$
- `abs` is the p-adic norm $|x|_p$ as a float
- `to_fraction(abs)` is a string expressed as a ratio of integers a/b, converted by the `fractions` package

The web app interface returns the valuation and the fractional representation of the norm by default, for pedagogical purposes.  The user can choose between float or fraction, and a copy to clipboard button is provided.  When `abs` is an integer (i.e. $val \le 0$), both it and `fraction` are converted to type `int`.

Example in terminal:

    import p_adic_compute as p
    
    p.p_adic_abs(5, 1/200)
    25
    
    p.p_adic_abs(5, 200)
    '1/25'

Next goals:
- update to a [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.2.x/) FlaskForm subclass to include CSRF protection
- light/dark toggle switch
- provide a [primality testing](https://github.com/ajaffary/prime-numbers) method
