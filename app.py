# Import Statements
from flask import Flask, render_template
from blueprints.loops import loops_blueprint
from blueprints.operators import operators_blueprint

# Declare flask app instance
app = Flask(__name__)

# Home Page Route
@app.route('/')
def home():
    return render_template('home.html')

# Blueprints
app.register_blueprint(loops_blueprint)
app.register_blueprint(operators_blueprint)

# Listen on Port 5000
if __name__ == '__main__':
    app.run()