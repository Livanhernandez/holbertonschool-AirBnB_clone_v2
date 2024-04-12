from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
