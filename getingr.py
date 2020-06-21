import sys
import json
import requests
#pip install requests==2.9.1 to get the requests library. 
#The sys and json libraries come with python.

AllIngredients = {}

def IncrementDict(dict,key,value,units):
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

def PrintList():
    print("Shopping list")
    for ingredient in AllIngredients:
        ResultLine = str(ingredient) + ":"
        for unit in AllIngredients[ingredient]:
            ResultLine = ResultLine + str(AllIngredients[ingredient][unit]) + " " +  str(unit) + ", "
        ResultLine = ResultLine[:-2]
        print(ResultLine)
        

def get_ingredients(recipe_id, apiKey):
    requestlink = 'https://api.spoonacular.com/recipes/' + str(recipe_id) + '/ingredientWidget.json?apiKey=' + str(apiKey)
    response = requests.get(requestlink)
    dict = response.json()


    inner = dict.get('ingredients')
    accumulator = []
    for element in inner:
        name = element["name"]
        metric = element["amount"]["metric"]
        value = metric["value"]
        unit = metric["unit"]
        IncrementDict(AllIngredients,name,value,unit)
        total = name + ': ' + str(unit) + ' ' + str(value)
        accumulator.append(total)

    print(accumulator)
    return(accumulator)

    

"""
sys.argv[1] is the list of recipe ID's. They should be large integers.

sys.argv[2] is the apiKey of the user. This is found by creating an account
at spoonacular.com and checking the user profile. This should be a string.
"""
