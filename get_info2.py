import requests
import json

def get_data(query):
    # api-endpoint
    URL = query

    # sending get request and saving the response as response object
    r = requests.get(url=URL)

    # extracting data in json format
    data = r.json()
    return data

################################################################################
#                       Get the Recipe IDs and URLs/Names
################################################################################

def get_random_recipe_urls(data):
    urls = data['recipes']

    lst = []
    for url in urls:
        lst.append(url['sourceUrl'])

    return lst

def get_random_recipe_ids(data):

    ids = data['recipes']

    lst = []
    for id in ids:
        lst.append(id['id'])

    return lst

def get_random_recipe_names(data):

    names = data['recipes']

    lst = []
    for name in names:
        lst.append(name['title'])

    return lst

################################################################################
#                       Get Prices for each Recipe
################################################################################

def get_price(query):

    data = get_data(query)
    json = data.json()
    ingredients = json["ingredients"]
    cost = json["totalCost"]
    #CostPerServing = json["totalCostPerServing"]

    return cost

################################################################################
#                     Get Ingredient List for each Recipe
################################################################################

def get_ingredients(query):

    dict = get_data(query)

    inner = dict['ingredients']
    accumulator = []
    for element in inner:
        name = element.get('name')
        amtabr = element.get('amount')
        usunit = amtabr.get('metric')
        measurement = str(usunit.get('value'))
        if usunit.get('unit') != '':
            measurement += ' ' + usunit.get('unit')
        total = name + ' (' + measurement + ')'
        accumulator.append(total)

    return(accumulator)
