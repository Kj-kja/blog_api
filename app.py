# app.py
# app.py
from flask import Flask
from config import Config  # Import Config from config.py
from models import db  # Import db from models.py
from routes import blog_posts_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    app.register_blueprint(blog_posts_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
