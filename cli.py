import importlib
import os
from pathlib import Path

import click

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODULE_TEMPLATE = {
    "__init__.py": """from flask import Blueprint

{name}Blueprint = Blueprint('{name}', __name__)

    """,
    "route.py": """from flask import request
from . import {name}
from .service import get_{name}

    
@{name}Blueprint.route('/', methods=['GET'])
def index():
    return index()
        
    """,
    "model.py": "from app.extensions import db",
    "schema.py": "from app.extensions import ma",
    "service.py": """from flask import jsonify
    
    
def index():
    return


def show(id):
    return


def store():
    return


def update(id):
    return


def destroy(id):
    return

    """,
}


def load_models():
    blueprints_dir = Path("blueprints")
    for module_path in blueprints_dir.glob("*/model.py"):
        module_name = f"blueprints.{module_path.parent.name}.model"
        try:
            importlib.import_module(module_name)
            print(f"Loaded model from: {module_name}")
        except ImportError as e:
            print(f"Failed to load {module_name}: {e}")


@click.group()
def cli():
    """Command-line interface for managing the Flask app."""
    pass


@cli.command()
@click.argument("module_name")
def create_module(module_name):
    """Create a new feature module."""
    module_dir = os.path.join(BASE_DIR, "blueprints", module_name)

    if os.path.exists(module_dir):
        click.echo(f"Module '{module_name}' already exists!")
        return

    # Create the directory structure
    os.makedirs(module_dir)

    # Generate files from template
    for file_path, content in MODULE_TEMPLATE.items():
        file_full_path = os.path.join(module_dir, file_path)
        content = content.format(name=module_name)
        with open(file_full_path, "w") as file:
            file.write(content)

    click.echo(f"Module '{module_name}' created successfully at {module_dir}!")


@cli.command()
def create_tables():
    """Create all database tables based on SQLAlchemy models."""
    from dotenv import load_dotenv
    from app import create_app
    from app.extensions import db

    load_dotenv()

    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    load_models()

    with app.app_context():
        db.create_all()
        click.echo("All tables have been created successfully.")


@cli.command()
def drop_tables():
    """Drop all database tables."""
    from dotenv import load_dotenv
    from app import create_app
    from app.extensions import db

    load_dotenv()

    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    load_models()

    with app.app_context():
        db.drop_all()
        click.echo("All tables have been dropped successfully.")


if __name__ == "__main__":
    cli()
