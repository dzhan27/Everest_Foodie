import requests
from getingr import *


#This just tests the ingredient list on 3 random recipes

if __name__ == "__main__":
    idlist = [1471513,1471493,1470917]
    key = "562c33b320a24074a1859e19e2f47ffa"
    for id in idlist:
        get_ingredients(id,key)
    PrintList()



    
