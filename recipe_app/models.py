from django.db import models

class Recipe(models.Model):
    recipe_name= models.CharField(max_length=30)
    recipe_description=models.TextField()
    recipe_ingredients=models.TextField()
    recipe_image=models.ImageField(upload_to='images/')
    # recipe_time= models.IntegerField(default=0)
