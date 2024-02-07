from django.shortcuts import render
from .models import *
def form(request):
    if request.method=='POST':
        data= request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        # recipe_time= data.get('time')
        recipe_image=request.FILES.get('recipe_image')
        recipe_ingredients=data.get('recipe_ingredients')
        print(recipe_name)
        print(recipe_description)
        print(recipe_ingredients)
        # print(recipe_time)
        print(recipe_image)
        Recipe.objects.create(recipe_name=recipe_name, recipe_ingredients=recipe_ingredients, recipe_description=recipe_description, recipe_image=recipe_image)

    return render(request, 'form.html')