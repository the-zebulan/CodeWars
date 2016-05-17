def cakes(recipe, ingredients):
    return min(ingredients.get(k, 0) / v for k, v in recipe.iteritems())
