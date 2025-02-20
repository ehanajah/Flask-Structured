from app import create_app
from dotenv import load_dotenv

import blueprints

from app.config import Config
from app.extensions import db, ma

load_dotenv()

app = create_app()
app.config.from_object(Config)

db.init_app(app)
ma.init_app(app)
app.register_blueprint(blueprints.authors.authorsBlueprint, url_prefix='/api')
app.register_blueprint(blueprints.blogs.blogsBlueprint, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
