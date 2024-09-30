from django.urls import path 
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("log-in/", log_in, name="log_in" ),
    path("about_us/", about_us, name="about_us"),
    path("add_recipe/", add_recipe, name="add_recipe"),
    path("recipe/<int:recipe_id>/", recipe_detail, name="recipe_detail"),
    path("delete_recipe/<int:recipe_id>/", delete_recipe, name="delete_recipe"),
    path("log-in/page/", login_page, name="page"),
    path("category_home/<int:home_id>/", category_home, name="category_home"),
    path('recipe/<int:recipe_id>/like/', like_recipe, name='like_recipe'),
    path('recipe/<int:recipe_id>/add_comment/', add_comment, name='add_comment'),
    path('recipe/<int:recipe_id>/add_rating/', add_rating, name='add_rating'),
    path('contact_us/', contact_us, name="contact_us"),
    path('contact_us/success_mail/', mail_success, name="success_mail"),
    path('special_receipe/', special_receipes, name="special_receipes"),
    path('payment/', payment, name="payment"),
    path('payment/success_payment/', success_payment, name="success_payment")
]



