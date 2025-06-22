from flask import Flask
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance 
from routes import episodes_bp

# Initialize app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False  # Format JSON nicely

# Initialize db and migrations
db.init_app(app)
migrate = Migrate(app, db)

# Basic root route
@app.route('/')
def index():
    return '<h1>Late Show API is running!</h1>'

app.register_blueprint(episodes_bp) 

if __name__ == '__main__':
    app.run(port=5555, debug=True)
