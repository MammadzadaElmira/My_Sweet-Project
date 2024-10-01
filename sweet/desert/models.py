from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"
    
    def thumbnail_photo_url(self):
        image_url = self.images.first()
        if image_url:
            return image_url.img.url
        return ""

    
class Recipe(models.Model):
    LANGUAGES = (
        ("AZ", "AZ"),
        ("EN", "EN"),
        ("RU", "RU")
    )

    name = models.CharField(max_length=256, null=True, blank=True)
    instruction = models.TextField(max_length=1000, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ingredients = models.TextField(max_length=1000,  null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    language = models.CharField(max_length=4, choices=LANGUAGES,  null=True, blank=True)
    ingredient = models.TextField(max_length=1000, null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)
    views_count = models.PositiveIntegerField(default=0)
    
    
    def get_thumbnail_photo_url(self):
        photo_url = self.photos.first()
        if photo_url:
            return photo_url.pht.url
        return ""


    class Meta:
        verbose_name = "Resept"
        verbose_name_plural = "Resepts"

    def __str__(self) -> str:
        return f"{self.name}"
    


class Like(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()


class Comment(models.Model):
    LANGUAGES = (
        ("AZ", "AZ"),
        ("EN", "EN"),
        ("RU", "RU")
    )
    
    text = models.TextField(max_length=1000, null=True, blank=True)
    language = models.CharField(max_length=4, choices=LANGUAGES, null=True, blank=True)
    recipe = models.ForeignKey(Recipe, related_name='comments', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.recipe.name}'

    
    
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.PositiveSmallIntegerField()  

    def __str__(self):
        return f'Rating by {self.user.username} on {self.recipe.name}'



class CategoryPhoto(models.Model):
    image = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images")
    img = models.ImageField(upload_to="category_photos/%Y/%m/%d")

    class Meta:
        verbose_name = "Category Photo"
        verbose_name_plural = "Category Photos"

    
    def __str__(self) -> str:
        return f"{self.image.title}"


class RecipePhoto(models.Model):
    photo = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="photos")
    pht = models.ImageField(upload_to="recipes_photos/%Y/%m/%d")



class SpecialRecipe(models.Model):
    LANGUAGES = (
        ("AZ", "AZ"),
        ("EN", "EN"),
        ("RU", "RU")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    recipe_name = models.CharField(max_length=256, null=True, blank=True)   
    instruction = models.TextField(max_length=1000, null=True, blank=True)
    ingredients = models.TextField(max_length=1000,  null=True, blank=True)
    language = models.CharField(max_length=4, choices=LANGUAGES,  null=True, blank=True)
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)



   

