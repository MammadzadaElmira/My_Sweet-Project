from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(CategoryPhoto)
admin.site.register(RecipePhoto)
admin.site.register(Rating)
admin.site.register(SpecialRecipe)

