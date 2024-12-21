# P-adic Valuation Form

## To Do List

### Controller
- change "enter prime" to "choose a prime" (?)
  - enter a prime is better for now?

### Model
- add labels and default values to form elements (done)
- create a list of primes for user?
  - does this go into Form? No? It's just a data structure containing primes
  - suggest a link for user
- allow user to enter their own prime?
  - requires prime number validator (see below)

### View
- create full HTML page structure (done)
  - see https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
  - See Flask docs for more examples
  - Search for more examples
- Form structure? (done)
  - See docs for examples
    - revisit HTML form MDN docs for accessibility
    - WTForms/Flask-WTF form validation: https://flask.palletsprojects.com/en/stable/patterns/wtforms/
  - successful Jinja template (done)
    - macros for input fields (done)
    - can WTForms class output `<form>` element? (no)
    - next: put macros in their own file & import (done)
    - fieldset and legend
- update app interface
  - add labels to form input fields (done)
  - create vertical viewport dimensions (done)
  - create grid (done with flex)
  - add CSS (done)
    - fonts
    - spacing
    - borders
    - link hover
- notes/references section
- footer author info

### Compute Functions
- prime number validator?
  - can be bogged down with large number
  - valuation can be done for non-prime, but not useful (?)
    - see reference on zero divisor rings
- added highest_power function on compute branch
  - faster for integers
  - doesn't save time for rational numbers
- optional outputs:
  - float
  - valuation
- copy to clipboard button (done)

### Notes
- rational provided for you to compute floats to your own precision
- arithmetic expressions will work
- will work with composites, but not "useful" (?)
  - see reference on finite fields

### References
- https://math.stackexchange.com/questions/1919274/why-are-p-adic-numbers-and-p-adic-integers-only-defined-for-p-prime
- wolfram p-adic
- sagemath library
- other p-adic notes
- list of primes
- python operators: https://www.w3schools.com/python/python_operators.asp
- parse math: https://stackoverflow.com/questions/13055884/parsing-math-expression-in-python-and-solving-to-find-an-answer
- parse math with math.js: https://www.geeksforgeeks.org/how-to-parse-and-compile-expressions-using-mathjs/
- eval function: https://www.w3schools.com/python/ref_func_eval.asp