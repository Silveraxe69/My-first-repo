from sets_categories_data import (VEGAN, VEGETARIAN, KETO, PALEO, OMNIVORE, ALCOHOLS, SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return (dish_name, set(dish_ingredients))

def check_drinks(drink_name, drink_ingredients):
    drink_set = set(drink_ingredients)
    if drink_set.isdisjoint(ALCOHOLS):
        return f"{drink_name} Mocktail"
    return f"{drink_name} Cocktail"

def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    if dish_ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    if dish_ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    if dish_ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    return f"{dish_name}: OMNIVORE"

def tag_special_ingredients(dish):
    dish_name, ingredients = dish
    ingredients_set = set(ingredients)
    special = ingredients_set.intersection(SPECIAL_INGREDIENTS)
    return (dish_name, special)

def compile_ingredients(dishes):
    return set().union(*dishes)

def separate_appetizers(dishes, appetizers):
    dishes_set = set(dishes)
    appetizers_set = set(appetizers)
    return list(dishes_set - appetizers_set)

def singleton_ingredients(dishes, intersection):
    all_ingredients = set().union(*dishes)
    return all_ingredients - intersection
