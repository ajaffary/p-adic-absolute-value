# P-adic Valuation Form

## To Do List

### Controller
- change "enter prime" to "choose a prime"
  - include a list of primes?

### Model
- add labels and default values to form elements
- need a list of primes
  - does this go into Form? No? It's just a data structure containing primes
- allow user to enter their own prime?
  - requires prime number validator

### View
- create full HTML page structure
  - see https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates
  - See Flask docs for more examples
  - Search for more examples
- Form structure?
  - See docs for examples
  - revisit HTML form MDN docs for accessibility
  - WTForms templates:https://flask.palletsprojects.com/en/stable/patterns/wtforms/
  - 
    - 
- update app interface
  - add labels to form input fields
  - add CSS

### Compute Functions
- prime number validator?
  - can be bogged down with large number
  - valuation can be done for non-prime, but not useful (?)

### References
- https://math.stackexchange.com/questions/1919274/why-are-p-adic-numbers-and-p-adic-integers-only-defined-for-p-prime
- wolfram p-adic
- other p-adic notes
- 
- python operators: https://www.w3schools.com/python/python_operators.asp
- parse math: https://stackoverflow.com/questions/13055884/parsing-math-expression-in-python-and-solving-to-find-an-answer
- parse math with math.js: https://www.geeksforgeeks.org/how-to-parse-and-compile-expressions-using-mathjs/
- eval function: https://www.w3schools.com/python/ref_func_eval.asp