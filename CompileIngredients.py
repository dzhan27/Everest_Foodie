import requests

AllIngredients = {}

ConversionTables = {}

def ConvertUnits(old,new,value):
    print("todo")
    

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
        

def AddIngredients(ingredients):
    for item in ingredients:
        name = item["name"]
        metric = item["measures"]["metric"]
        amount = metric["amount"]
        unit = metric["unitShort"]
        IncrementDict(AllIngredients,name,amount,unit)
        


def CheckAllIds(ids,APIkey):
    for ID in ids:
        RequestString = "https://api.spoonacular.com/recipes/" + str(ID) + "/information?apiKey=" + APIkey
        response = requests.get(RequestString)
        data = response.json()
        ingredients = data['extendedIngredients']
        AddIngredients(ingredients)
    print("Shopping list")
    for ingredient in AllIngredients:
        ResultLine = str(ingredient) + ":"
        for unit in AllIngredients[ingredient]:
            ResultLine = ResultLine + str(AllIngredients[ingredient][unit]) + " " +  str(unit) + ", "
        ResultLine = ResultLine[:-2]
        print(ResultLine)
            
        

if __name__ == "__main__":
    idlist = [1471513,1471493,1470917]
    key = "562c33b320a24074a1859e19e2f47ffa"
    CheckAllIds(idlist,key)





    
