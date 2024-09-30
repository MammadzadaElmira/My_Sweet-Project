from django.shortcuts import render
from django.http import HttpResponse, Http404
from.models import Category,Recipe, RecipePhoto, Comment, Rating, SpecialRecipe
from django.shortcuts import redirect
from django.views.generic import ListView
from django import forms
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q  
from django.http import JsonResponse
from django.db.models import Avg 



def log_in(request):
    return render(request, "log_in.html")

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    if request.method == "POST":
        data = request.POST
        to_mail = data.get("email")
        body = data.get("message")
        name = data.get("name")
       
        send_mail(
            name,
            body,
            settings.EMAIL_HOST_USER,
            [to_mail],
            fail_silently=True,
        )
        
    return render(request, "contact_us.html")



def add_recipe(request):
    if request.method == "POST":
        data = request.POST
        images = request.FILES.getlist("images")  
        name = data.get("recipe-name")
        instruction = data.get("instructions")
        language = data.get("language")
        ingredient = data.get("ingredients")
        category_id = data.get("category")

        category = Category.objects.get(id=category_id)

        
        recipe = Recipe.objects.create(
            name=name,
            instruction=instruction,
            language=language,
            ingredient=ingredient,
            category=category
        )

        
        if images:
            for image in images:
                RecipePhoto.objects.create(
                    photo=recipe,
                    pht=image
                )

        return redirect("/")

    categories = Category.objects.all()
    context = {
        "categories": categories
    }

    return render(request, "add_recipe.html", context)



def home(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.order_by("-created_at")[:6]  
    recipes = recipes.annotate(average_rating=Avg("ratings__rating")) 
    query = request.GET.get("q")  


    if query:
        recipes = Recipe.objects.filter(
            Q(name__icontains=query) | 
            Q(ingredient__icontains=query) |
            Q(instruction__icontains=query)
        )

    context = {
        "categories": categories,
        "recipes": recipes,
        "query": query,
        
    }
    
    return render(request, "home.html", context)




def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    
    if not request.session.get(f"viewed_recipe_{recipe_id}", False):
        recipe.views_count += 1
        recipe.save()
        request.session[f"viewed_recipe_{recipe_id}"] = True
    
    context = {
        "recipe": recipe
    }
    return render(request, "recipe_details.html", context)



def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    recipe.delete()
    return redirect("/")
    

def login_page(request):
    return render(request, "login_page.html")


def success_payment(request):
    return render(request, "success_payment.html")
    

def mail_success(request):
    return render(request, "mail_success.html")


def special_receipes(request):
    context = {
        "special_recipes": SpecialRecipe.objects.all()
    }
    return render(request, "special_receipes.html", context)


def category_home(request, home_id):
    context = {
        "kateqoriya": Category.objects.get(id=home_id),
        "reseptler": Recipe.objects.filter(category=home_id)
    }
    return render(request, "category_home.html", context)


def payment(request):
    return render(request, "payment.html")


def like_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    if request.user in recipe.likes.all():
        recipe.likes.remove(request.user)
    else:
        recipe.likes.add(request.user)
    return redirect("recipe_detail", recipe_id=recipe.id)



@login_required
def add_comment(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == "POST":
        comment_text = request.POST.get("comment")
        if comment_text:
            Comment.objects.create(
                recipe=recipe,
                user=request.user, 
                text=comment_text  
            )
            return redirect("recipe_detail", recipe_id=recipe_id)

    return render(request, "add_comment.html", {"recipe": recipe})



@login_required
def add_rating(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)

    if request.method == "POST":
        score = request.POST.get("rating")  
        if score:
            rating, created = Rating.objects.update_or_create(
                recipe=recipe,
                user=request.user,
                defaults={"rating": score}
            )

            new_average_rating = recipe.ratings.aggregate(Avg("rating"))["rating__avg"] or 0
            return JsonResponse({'new_average_rating': new_average_rating})

    return redirect('recipe_detail', recipe_id=recipe.id)



