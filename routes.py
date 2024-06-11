# routes.py
# routes.py
from flask import Blueprint, jsonify, request
from models import db, BlogPost  # Import db and BlogPost from models.py

blog_posts_bp = Blueprint('blog_posts', __name__)

@blog_posts_bp.route('/posts', methods=['GET'])
def get_all_posts():
    posts = BlogPost.query.all()
    return jsonify([post.__dict__ for post in posts]), 200

@blog_posts_bp.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    post = BlogPost.query.get_or_404(id)
    return jsonify(post.__dict__), 200

@blog_posts_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    post = BlogPost(title=data['title'], content=data['content'])
    db.session.add(post)
    db.session.commit()
    return jsonify(post.__dict__), 201

@blog_posts_bp.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    post = BlogPost.query.get_or_404(id)
    data = request.json
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify(post.__dict__), 200

@blog_posts_bp.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return '', 204

