from flask import jsonify

from app.extensions import db
from .model import Blog
from .schema import blog_schema, blogs_schema
    
    
def index():
    try:
        blogs = Blog.query.all()
        result = blogs_schema.dump(blogs)
        return jsonify({'status': 'success', 'blogs': result}), 200
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500


def show(id):
    try:
        blog = Blog.query.get_or_404(id)
        result = blog_schema.dump(blog)
        return jsonify({'status': 'success', 'blog': result}), 200
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500


def store(request):
    try:
        title = request.json.get('title')
        content = request.json.get('content')
        author_id = request.json.get('author_id')

        if not title or not content or not author_id:
            return jsonify({'status': 'failed', 'message': 'Data tidak lengkap'}), 400

        new_blog = Blog(title=title, content=content, author_id=author_id)

        db.session.add(new_blog)
        db.session.commit()

        result = blog_schema.dump(new_blog)
        return jsonify({'status': 'success', 'blog': result}), 201
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500


def update(request, id):
    try:
        blog = Blog.query.get_or_404(id)

        title = request.json.get('title', blog.title)
        content = request.json.get('content', blog.content)
        author_id = request.json.get('author_id', blog.author_id)

        blog.title = title
        blog.content = content
        blog.author_id = author_id

        db.session.commit()

        result = blog_schema.dump(blog)
        return jsonify({'status': 'success', 'blog': result}), 200
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500


def destroy(id):
    try:
        blog = Blog.query.get_or_404(id)
        db.session.delete(blog)
        db.session.commit()

        return jsonify({'status': 'success', 'message': f'Blog with id {id} deleted successfully'}), 200
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500
