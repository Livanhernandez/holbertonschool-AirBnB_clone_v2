from flask import Flask, render_template

app = Flask(__name__)


# Route for '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


# Route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    return 'HBNB'


# Route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    # Replace underscore (_) with space in the text variable
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


# Route for '/python/<text>'
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    # Replace underscore (_) with space in the text variable
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


# Route for '/number/<n>'
@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f'{n} is a number'


# Route for '/number_template/<n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)
    else:
        return 'Not Found', 404


# Route for '/number_odd_or_even/<n>'
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    if isinstance(n, int):
        odd_or_even = 'odd' if n % 2 != 0 else 'even'
        return render_template('6-number_odd_or_even.html', n=n,
                               odd_or_even=odd_or_even)
    else:
        return 'Not Found', 404


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
