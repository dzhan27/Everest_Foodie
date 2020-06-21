import requests


def getPrice(RecipeID,Key):

    ID = "1003464"
    APIKey = "562c33b320a24074a1859e19e2f47ffa"

    TotalCost = ""
    CostPerServing = ""

    RequestString = "https://api.spoonacular.com/recipes/" + ID + "/priceBreakdownWidget.json?&apiKey=" + APIKey


    response = requests.get(RequestString)
    if response.status_code == 404:
        print("Error, invalid ID")

    text = response.text
    json = response.json()
    ingredients = json["ingredients"]
    TotalCost = json["totalCost"]
    CostPerServing = json["totalCostPerServing"]

    print(TotalCost)
    print(CostPerServing)


if __name__ == "__main__":
    RecipeID = "1003464"
    ApiKey = "562c33b320a24074a1859e19e2f47ffa"
    getPrice(RecipeID,ApiKey)
