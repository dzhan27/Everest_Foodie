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

AllIngredients = {}

def increment_dict(dict,key,value,units):
    if key in dict:
        if units in dict[key]:
            dict[key][units] = dict[key][units] + value
        else:
            #print("unit mismatch")
            #Ignores unit conversion, stores multiple units in list
            dict[key][units] = value
    else:
        dict[key]= {}
        dict[key][units] = value

def get_ingredients(query):

    dict = get_data(query)

    inner = dict['ingredients']
    accumulator = []
    for element in inner:
        name = element["name"]
        metric = element["amount"]["metric"]
        value = metric["value"]
        unit = metric["unit"]
        increment_dict(AllIngredients,name,value,unit)
        total = name + ': ' + str(unit) + ' ' + str(value)
        accumulator.append(total)

    return(accumulator)
