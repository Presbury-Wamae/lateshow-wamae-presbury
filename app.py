from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False  # Format JSON nicely

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Basic root route to confirm it's running
@app.route('/')
def index():
    return '<h1>Late Show API is running!</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
