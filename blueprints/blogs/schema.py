from app.extensions import ma
from .model import Blog


class BlogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'content', 'author_id')


blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)
