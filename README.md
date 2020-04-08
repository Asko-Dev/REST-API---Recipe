<h2> Recipe upload API (tags & ingredients, filtration)</h2>

- User Registration
- User Token Authentication
- User Details display (based on the token loaded)
- API root for Tag API, Ingredient Upload API, Recipe Upload API, Image File API
- Tag API -> create tags to assign to your recipe when POSTing recipe
    - Display detail of the tag and Update or Delete (if owner)
- Ingredient API -> create ingredients to assign to your recipe when POSTing recipe
    - Display detail of the ingredient and Update or Delete (if owner)
- Recipe API ->
    - Upload and name recipes
    - Add Tags & Ingredients to your recipes
    - Add description, time to cook, price
    - Add an Image of your recipe (upload a file)
    - Display detail of the recipe and Update or Delete (if owner)
- Public Recipe API ->
    - Recipes of all users displayed
    - Display detail of the recipe (only GET option)
- Filtering based on tags & ingredients for both Private and Public API

<h2>DEPLOYED TO HEROKU using Git</h2>

<b>ROOT URL: https://asko-recipeapp.herokuapp.com

URL Endpoints:</b>

-	/api/user/create/				
-	/api/user/token/					
-	/api/user/me/				
-	/api/recipe/				
-	/api/recipe/tags/					
-	/api/recipe/tags/pk/				
-	/api/recipe/ingredients/				
-	/api/recipe/ingredients/pk/				
-	/api/recipe/recipes/				
-	/api/recipe/recipes/pk/				
-	/api/recipe/recipes/pk/upload-image/		
-	/api/recipe/recipes/?tags=pk&ingredients=pk
-	/api/recipe/public-recipes/				
-	/api/recipe/public-recipes/pk/
-	/api/recipe/public-recipes/?tags=pk&ingredients=pk
