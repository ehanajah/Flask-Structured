from app.extensions import ma
from .model import Author


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        fields = ('id', 'name', 'email')


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
