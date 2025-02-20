from flask import jsonify

from app.extensions import db
from .model import Author
from .schema import authors_schema, author_schema


def index():
    try:
        all_authors = Author.query.all()
        result = authors_schema.dump(all_authors)
        return jsonify({'status': 'success', 'authors': result}), 200
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500


def show(id):
    try:
        author = Author.query.get_or_404(id)
        result = author_schema.dump(author)
        return jsonify({'status': 'success', 'author': result}), 200
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500


def store(request):
    try:
        name = request.json.get('name')
        email = request.json.get('email')

        if not name or not email:
            return jsonify({'status': 'failed', 'message': 'Data tidak lengkap'}), 400

        new_author = Author(name=name, email=email)

        db.session.add(new_author)
        db.session.commit()

        result = author_schema.dump(new_author)
        return jsonify({'status': 'success', 'author': result}), 201
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500


def update(request, id):
    try:
        author = Author.query.get_or_404(id)
        name = request.json.get('name', author.name)
        email = request.json.get('email', author.email)

        author.name = name
        author.email = email

        db.session.commit()

        result = author_schema.dump(author)
        return jsonify({'status': 'success', 'author': result})
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500


def destroy(id):
    try:
        author = Author.query.get_or_404(id)
        db.session.delete(author)
        db.session.commit()

        return jsonify({'status': 'success', 'message': f'Author with id {id} deleted successfully'}), 200
    except Exception as e:
        return jsonify({'status': 'failed', 'message': str(e)}), 500
