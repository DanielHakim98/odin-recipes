from flask import render_template,redirect,url_for
from odin_recipes_app import app
from odin_recipes_app.recipes.recipes import *
# import os

# dirname = os.path.dirname(__file__)
# recipes_dir = os.path.join(dirname,"templates","recipes")
# list_recipes = [file.split(".")[0] for file in os.listdir(recipes_dir)]



@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",title="Home")

@app.route("/<recipe_name>")
def recipe(recipe_name):

    list_of_recipes = list(map(lambda x:x.lower(),recipe_dict.keys()))
    if recipe_name in list_of_recipes:
        return render_template(
            "recipe.html",
            title=recipe_dict[recipe_name]["name"],
            recipe=recipe_dict[recipe_name]
        )
    return redirect(url_for('/'))


