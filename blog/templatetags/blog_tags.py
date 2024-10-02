from django import template
from ..models import Post

register = template.Library()
@register.simple_tag
def total_posts():
    return Post.published.count()    # Devolvemos el numero de publicaciones del blog