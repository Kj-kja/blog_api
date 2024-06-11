from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from auth import auth_bp
from routes import blog_posts_bp
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(blog_posts_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5001)
