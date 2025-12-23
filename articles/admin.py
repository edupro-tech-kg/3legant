from django.contrib import admin
from .models import *


@admin.register(Article)
class AdminArticle(Article):
    pass
