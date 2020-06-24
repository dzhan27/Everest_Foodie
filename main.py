"""
Things that could be improved:

- Get pictures of the recipes in the recipe roller frame
- Fix sizing to scale to data in ingredient and shopping lists
- Have the application email the final shopping list to the user
- Get a nice background picture
- Fix links on the recipe page (they all point to the last recipe)
- Fix ingredient and shopping lists to alternate their y values so as to counter extremely long ingredients
- Combine preferences and second frame
- Other aesthethic improvements?
- Add about page.

from api:
- minimum review for each recipe
- ingredients to not include
- preparation time for each recipe
- price of ingredient totals of each recipe

not from api:
- where to shop for ingredients
- internal review system
- saving recipes for later
- favorites
- add your own recipe to the shopping list
- add your own ingredients to the shopping list

"""



from tkinter import *
from tkinter.ttk import *
import requests
import json
import webbrowser
import time

from get_info import get_data
from get_info import get_ingredients
from get_info import get_random_recipe_urls
from get_info import get_random_recipe_ids
from get_info import get_random_recipe_names

class Window(Frame):

    #These default values take the place of user input if the input is blank.
    default_name = 'New User'
    default_apikey = '74384699376e430daeedabdc69e3e48e'
    number_of_requested_recipes = 1

    #the state_of_ingredient_list shows which ingredients the user already has. 
    #Ingredients that he DOES NOT have have a value 2 while ingredients he does have take the value 1.
    list_of_necessary_ingredients = []
    state_of_ingredient_list = []

    data = {}
    ids = []

    query = ''

    #timemessage displays a welcoming message to the user based on the time of day.
    t = time.localtime()
    current_time = int(time.strftime("%H", t))
    if current_time <= 4 or current_time >= 18:
        timemessage = "Good evening, "
    elif current_time >= 5 and current_time <= 11:
        timemessage = "Good morning, "
    else:
        timemessage = "Good afternoon, "

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        
        self.some_frame = None
        self.init_window()

    def init_window(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()

        self.master.title("Foodie!")


        window_width = 800
        window_height = 600
        root.geometry(str(window_width) + 'x' + str(window_height))
    
        canvas0 = Canvas(self.some_frame, width=window_width, height=window_height)
        canvas0.pack()

        txt1 = Label(self.some_frame, text="\nWelcome to Foodie!", font=("Garamond", 35))
        canvas0.create_window(400,90, window=txt1)

        spoontxt = Label(self.some_frame, text="Powered by spoonacular.com's API.", font=("Courier New", 9))
        canvas0.create_window(3,590, window=spoontxt, anchor=W)

        longtext1 = 'An application that helps you explore \n   and prepare to try new recipes.'
        txt2 = Label(self.some_frame, text=longtext1, font=('Courier New', 11))
        canvas0.create_window(400,180, window=txt2)

        txt3 = Label(self.some_frame, text='\n\n\n\nLet\'s begin by logging in:', font=('Courier New', 11))
        canvas0.create_window(400,240, window=txt3)

        txt4 = Label(self.some_frame, text='Please leave this blank unless you \nhave a spoonacular.com API key.', font=('Courier New', 8))
        canvas0.create_window(620,360, window=txt4)

        nametxt = Label(self.some_frame, text='Your Name', font=('Courier New', 11))
        canvas0.create_window(285,320, window=nametxt)
        apitxt = Label(self.some_frame, text='API key', font=('Courier New', 11))
        canvas0.create_window(290,360, window=apitxt)
        
        entry1 = Entry(self.some_frame)
        entry2 = Entry(self.some_frame)
        canvas0.create_window(410, 320, window=entry1)
        canvas0.create_window(410, 360, window=entry2)

        def checkcreds():
            if entry1.get() != '':
                self.default_name = entry1.get()
            if entry2.get() != '':
                self.default_apikey = entry2.get()

            link = 'https://api.spoonacular.com/recipes/635447/ingredientWidget.json?apiKey=' + self.default_apikey
            response = requests.get(link)
            if response.ok:
                self.some_frame.destroy()
                self.some_frame = None
                self.recipe_roll()
            else:
                errtxt = Label(self.some_frame, text='An error occurred with your API key. \n         Please try again.', font=('Courier New', 11))
                errtxt.place(x=245, y=500)
                canvas0.create_window(410, 500, window=errtxt)

        submitButton = Button(self.some_frame, text="Let's Go!", style = 'W.TButton', command = checkcreds)
        submitButton.place(x=365, y=430)

    def recipe_roll(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()
        
        window_width = 800
        window_height = 600
        root.geometry(str(window_width) + 'x' + str(window_height))

        canvas0 = Canvas(self.some_frame, width=window_width, height=window_height)
        canvas0.pack()

        timemsg = Label(self.some_frame, text=self.timemessage + self.default_name + '.', font=("Courier New", 10))
        canvas0.create_window(10,15, window=timemsg, anchor=W)

        longtxt2 = '         Let\'s try some new recipes this week! \nHow many random recipes would you like to try?'
        txt2 = Label(self.some_frame, text=longtxt2, font=("Garamond", 20))
        canvas0.create_window(415,150, window=txt2)

        longtxt3 = 'Please limit yourself to 5.'
        txt3 = Label(self.some_frame, text=longtxt3, font=("Courier New", 10))
        canvas0.create_window(415,200, window=txt3)

        entry1 = Entry(self.some_frame)
        canvas0.create_window(400, 280, window=entry1)

        def check():
            num = entry1.get()
            if num == '':
                num = '1'
            try:
                intnum = int(num)
                assert intnum < 6 and intnum > 0
                self.number_of_requested_recipes = intnum
                self.some_frame.destroy()
                self.some_frame = None
                self.get_preferences()
            except:
                longtxt4 = 'An error occurred with your input. Please try again.'
                txt4 = Label(self.some_frame, text=longtxt4, font=("Courier New", 10))
                canvas0.create_window(415,370, window=txt4)

        submitButton = Button(self.some_frame, text="Roll Recipes!", style = 'W.TButton', command=check)
        canvas0.create_window(400, 320, window=submitButton)

    def get_preferences(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()
        
        window_width = 800
        window_height = 600
        root.geometry(str(window_width) + 'x' + str(window_height))
    
        canvas0 = Canvas(self.some_frame, width=window_width, height=window_height)
        canvas0.pack()

        txt1 = Label(self.some_frame, text="Configure " + self.default_name + '\'s preferences', font=("Courier New", 10))
        canvas0.create_window(10,15, window=txt1, anchor=W)

        longtxt2 = '         Do you have any dietary restrictions? \nIf so, enter (vegetarian, vegan, gluten-free, or dairy-free)'
        txt2 = Label(self.some_frame, text=longtxt2, font=("Garamond", 20))
        canvas0.create_window(415, 150, window=txt2)

        entry1 = Entry(self.some_frame)
        canvas0.create_window(400, 210, window=entry1)

        self.dietary_restriction = entry1.get()

        longtxt3 = '         Do you have any other preferences? \nIf so, enter (healthy, cheap, sustainable, or popular)'
        txt3 = Label(self.some_frame, text=longtxt3, font=("Garamond", 20))
        canvas0.create_window(415, 280, window=txt3)

        entry2 = Entry(self.some_frame)
        canvas0.create_window(400, 340, window=entry2)

        self.other_preference = entry2.get()

        def query():
            restr = entry1.get()
            pref = entry2.get()

            restrictions = ''
            preferences = ''

            if 'vegetarian' in restr or 'Vegetarian' in restr:
                restrictions += 'vegetarian'
            elif 'vegan' in restr or 'Vegan' in restr:
                restrictions += ',vegan'
            elif 'dairyfree' in restr or 'dairy-free' in restr or 'Dairy Free' in restr:
                restrictions += ',dairyFree'
            elif 'glutenfree' in restr or 'gluten-free' in restr or 'Gluten Free' in restr:
                restrictions += ',dairyFree'

            if 'healthy' in pref or 'Healthy' in pref:
                preferences += 'veryHealthy'
            elif 'cheap' in pref or 'Cheap' in pref:
                preferences += ',cheap'
            elif 'popular' in pref or 'Popular' in pref:
                preferences += ',veryPopular'
            elif 'sustainable' in pref or 'Sustainable' in pref:
                preferences += ',sustainable'

            if (restrictions == '' and preferences == ''):
                self.query = 'https://api.spoonacular.com/recipes/random?apiKey=' + self.default_apikey + '&number=' + str(self.number_of_requested_recipes)
            else:
                self.query = (
                    "https://api.spoonacular.com/recipes/random"
                    + "?apiKey=" + self.default_apikey
                    + "&number=" + str(self.number_of_requested_recipes)
                    + "&tags=" + restrictions + ',' + preferences
                )

            self.some_frame.destroy()
            self.some_frame = None
            self.show_recipes()

        submitButton = Button(self.some_frame, text="Submit!", style = 'W.TButton', command = query)
        canvas0.create_window(400, 380, window=submitButton)

    def ingredient_list(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()
        
        window_width = 1300
        window_height = 900
        root.geometry(str(window_width) + 'x' + str(window_height))
    
        canvas0 = Canvas(self.some_frame, width=window_width, height=window_height)
        canvas0.pack()

        timemsg = Label(self.some_frame, text=self.timemessage + self.default_name + '.', font=("Courier New", 10))
        canvas0.create_window(10,15, window=timemsg, anchor=W)

        longtxt2 = 'These are the ingredients necessary for your recipes for the week. \n                    Check the ingredients you already have.'
        txt2 = Label(self.some_frame, text=longtxt2, font=("Garamond", 16))
        canvas0.create_window(650,40, window=txt2)

        self.data = get_data(self.query)
        self.ids = get_random_recipe_ids(self.data)
        lst = []
        for id in self.ids:
            ingr_query = 'https://api.spoonacular.com/recipes/' + str(id) + '/ingredientWidget.json?apiKey=' + self.default_apikey
            lst += get_ingredients(ingr_query) #replace with ingredient list

        accx = 50
        accy = 130
        finaly = 0
        ingdict = {}
        for number in range(0,len(lst)):
            ingdict[number] = IntVar()
            ingdict[number].set(2)
            if number%3==0:
                x = accx
            elif number%3==1:
                x = accx + 420
            else:
                x = accx + 840
            y = accy + (number//3)*30

            ingrcheck = Checkbutton(self.some_frame, text='', variable=ingdict[number])
            canvas0.create_window(x,y, window=ingrcheck)

            txt1 = Label(self.some_frame, text=lst[number], font=("Courier New", 13))
            canvas0.create_window(x+20,y, window=txt1, anchor=W)

            finaly = y
        
        window_width = 1300
        window_height = finaly + 100
        root.geometry(str(window_width) + 'x' + str(window_height))
        
        def gotolist():
            self.some_frame.destroy()
            self.some_frame = None

            self.list_of_necessary_ingredients = lst
            state_of_ingredient_list = ingdict.values()
            accum = []
            for element in state_of_ingredient_list:
                accum.append(element.get())
            self.state_of_ingredient_list = accum

            self.shopping_list()
        
        submitButton = Button(self.some_frame, text="Continue to Shopping List", style = 'W.TButton', command=gotolist)
        canvas0.create_window(650, finaly+60, window=submitButton)

    def show_recipes(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()
        
        window_width = 1300
        window_height = 900
        root.geometry(str(window_width) + 'x' + str(window_height))
    
        canvas0 = Canvas(self.some_frame, width=window_width, height=window_height)
        canvas0.pack()

        timemsg = Label(self.some_frame, text=self.timemessage + self.default_name + '.', font=("Courier New", 10))
        canvas0.create_window(10,15, window=timemsg, anchor=W)

        longtxt2 = 'Here are your recipes!'
        txt2 = Label(self.some_frame, text=longtxt2, font=("Garamond", 24))
        canvas0.create_window(400,80, window=txt2)

        self.data = get_data(self.query) # delete later
        lst = get_random_recipe_urls(self.data)

        names = get_random_recipe_names(self.data)
        accx = 140
        accy = 150
        finaly = 0
        listoftext = [0,0,0,0,0,0,0]
        for number in range(0,len(lst)):
            y = accy + 60*number
            canvas0.create_window(accx,y, window=Label(self.some_frame, text=names[number], font=("Courier New", 14)), anchor=W)

            def callback(url):
                webbrowser.open_new(url)

            listoftext[number] = Label(root, text="See the recipe!", foreground="blue", cursor="hand2")
            canvas0.create_window(accx,y+20, window=listoftext[number], anchor=W)
            listoftext[number].bind("<Button-1>", lambda e: callback(lst[number]))

            finaly = y

        def gotoing():
            self.some_frame.destroy()
            self.some_frame = None
            self.ingredient_list()

        root.geometry("800x" + str(finaly+140))
        submitButton = Button(self.some_frame, text="Continue to Ingredient List", style = 'W.TButton', command=gotoing)
        canvas0.create_window(400, finaly+80, window=submitButton)
    
    def shopping_list(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()
        
        window_width = 1080
        window_height = 900
        root.geometry(str(window_width) + 'x' + str(window_height))
    
        canvas0 = Canvas(self.some_frame, width=window_width, height=window_height)
        canvas0.pack()

        txt1 = Label(self.some_frame, text='Here is your shopping list for the week. Have fun!', font=("Garamond", 20))
        canvas0.create_window(window_width/2, 50, window=txt1)

        accumulator = 0
        for number in range(0, len(self.list_of_necessary_ingredients)):
            if accumulator%2 == 0:
                x = 100
            else:
                x = 480
            if self.state_of_ingredient_list[number] == 2:
                canvas0.create_window(x, 140+20*accumulator, window=Label(self.some_frame, text=self.list_of_necessary_ingredients[number], font=("Courier New", 12)), anchor=W)
                accumulator += 1
        root.geometry("900x" + str(180+20*accumulator))
            
root = Tk()
app = Window(root)
root.mainloop()