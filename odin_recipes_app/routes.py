from flask import render_template,redirect
from odin_recipes_app import app
from odin_recipes_app.recipes.recipes import boiled_chicken
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

    if recipe_name == boiled_chicken["name"].replace(" ","").lower():
        return render_template(
            "recipe.html",
            title=recipe_name,
            recipe=boiled_chicken
        )
    return redirect('/')


