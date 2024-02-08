from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
def form(request):
    if request.method=='POST':
        data= request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        recipe_ingredients=data.get('recipe_ingredients')
        print(recipe_name)
        print(recipe_description)
        print(recipe_ingredients)
        print(recipe_image)
        Recipe.objects.create(recipe_name=recipe_name, recipe_ingredients=recipe_ingredients, recipe_description=recipe_description, recipe_image=recipe_image)
        messages.success(request, "Recipe added successfully")

    return render(request, 'form.html')

def view_recipe(request):
    recipe=Recipe.objects.all()
    return render(request, 'view_recipes.html', {"recipes":recipe})

def delete_recipe(request, id):
    recipe=Recipe.objects.get(id=id)
    recipe.delete()
    return redirect('/recipe_app/view_recipes/')

def update_recipe(request, id):
    recipe=Recipe.objects.get(id=id)
    if request.method=='POST':
        data= request.POST
        recipe_name=data.get('recipe_name')
        recipe_description=data.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')
        recipe_ingredients=data.get('recipe_ingredients')
        recipe.recipe_name=recipe_name
        recipe.recipe_description=recipe_description
        recipe.recipe_ingredients=recipe_ingredients
        recipe.recipe_image=recipe_image
        recipe.save()
        return redirect('/recipe_app/view_recipes/')

    return render(request, 'update_recipe.html', {"recipes":recipe})