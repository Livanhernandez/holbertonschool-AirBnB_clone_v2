from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
import sys
sys.path.append('/home/livanhernandez/holbertonschool-AirBnB_clone_v2 \
                /holbertonschool-AirBnB_clone_v2')


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
        return render_template('6-number_odd_or_even.html',
                               n=n, odd_or_even=odd_or_even)
    else:
        return 'Not Found', 404


# Route for '/states_list'
@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """Route to display a list of states."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


# Route for '/cities_by_states'
@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """Route to display a list of cities."""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


# Route for '/states'
@app.route('/states', strict_slashes=False)
def list_states():
    """ Display a HTML page with a list of all State objects """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def show_state_cities(state_id=None):
    """ Display a HTML page with cities of a specific State """
    states = storage.all(State)
    if state_id:
        key = "State." + state_id
        if key in states:
            state = states[key]
            return render_template('9-states.html', state=state)
        print("Error id not found")


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
