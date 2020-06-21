import requests
import sys

'''
Input: ID of recipe
Returns list of [IDs of ingredients] needed to make the recipe
'''


def get_recipe_information(id):

    # api-endpoint
    URL = "https://api.spoonacular.com/recipes/" + \
        str(id) + "/information?apiKey=59a7e6b428ec452aae2df21ac02729b1"

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()
    ingredients = data['extendedIngredients']

    # list of ingredient ID's
    lst = []
    for item in ingredients:
        lst.append(item['id'])

    print(lst)
    return lst


'''
API: Get random recipe
Returns link of recipe 
'''


def get_random_recipe_link():

    # api-endpoint
    URL = "https://api.spoonacular.com/recipes/random/?apiKey=59a7e6b428ec452aae2df21ac02729b1"

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()
    recipe_link = data['recipes'][0]['spoonacularSourceUrl']

    print(recipe_link)
    return recipe_link


if __name__ == "__main__":
    get_recipe_information(sys.argv[1])
    get_random_recipe_link()
