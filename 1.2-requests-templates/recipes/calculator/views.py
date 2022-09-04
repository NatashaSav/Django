from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe(request, current_recept):
    serving_size = request.GET.get("servings", "")
    final_recipe = {}
    if serving_size:
        for key, value in DATA[current_recept].items():
            final_recipe[key] = value * int(serving_size)
            DATA[current_recept].update(final_recipe)
        context = {'recipe': DATA[current_recept]}
    else:
        context = {
            "recipe": DATA[current_recept]

        }
    return render(request, template_name="calculator/index.html", context=context)