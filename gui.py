from tkinter import *
from tkinter.ttk import *
import requests
import json
import webbrowser

from get_info import get_data
from get_info import get_ingredients
from get_info import get_random_recipe_urls
from get_info import get_random_recipe_ids
from get_info import get_random_recipe_names

class Window(Frame):

    db_name = 'New User'
    db_apikey = '74384699376e430daeedabdc69e3e48e'
    db_numofrecipes = 0

    listofing = []
    stateofing = []

    data = {}
    ids = []

    query = ''

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        
        self.some_frame = None
        self.init_window()

    def init_window(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()

        self.master.title("Foodie!")
    
        canvas0 = Canvas(self.some_frame, width=800, height=600)
        canvas0.pack()

        txt1 = Label(self.some_frame, text="\nWelcome to Foodie!", font=("Garamond", 35))
        canvas0.create_window(400,90, window=txt1)

        longtext1 = 'An application that helps you explore \n   and prepare to try new recipes.'
        txt2 = Label(self.some_frame, text=longtext1, font=('Courier New', 11))
        canvas0.create_window(400,180, window=txt2)

        txt3 = Label(self.some_frame, text='\n\n\n\nLet\'s begin by logging in:', font=('Courier New', 11))
        canvas0.create_window(400,240, window=txt3)

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
                self.db_name = entry1.get()
            if entry2.get() != '':
                self.db_apikey = entry2.get()

            link = 'https://api.spoonacular.com/recipes/635447/ingredientWidget.json?apiKey=' + self.db_apikey
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
        canvas0 = Canvas(self.some_frame, width=800, height=600)
        canvas0.pack()

        txt1 = Label(self.some_frame, text="Good day, " + self.db_name + '.', font=("Courier New", 10))
        canvas0.create_window(10,15, window=txt1, anchor=W)

        longtxt2 = '         Let\'s try some new recipes this week! \nHow many random recipes would you like to try?'
        txt2 = Label(self.some_frame, text=longtxt2, font=("Garamond", 20))
        canvas0.create_window(415,150, window=txt2)

        longtxt3 = 'Please limit yourself to 7.'
        txt3 = Label(self.some_frame, text=longtxt3, font=("Courier New", 10))
        canvas0.create_window(415,200, window=txt3)

        entry1 = Entry(self.some_frame)
        canvas0.create_window(400, 280, window=entry1)

        def check():
            num = entry1.get()
            try:
                intnum = int(num)
                assert intnum < 8
                self.db_numofrecipes = intnum
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
        canvas0 = Canvas(self.some_frame, width=800, height=600)
        canvas0.pack()

        txt1 = Label(self.some_frame, text="Configure " + self.db_name + '\'s preferences', font=("Courier New", 10))
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
                self.query = 'https://api.spoonacular.com/recipes/random?apiKey=' + self.db_apikey + '&number=' + str(self.db_numofrecipes)
            else:
                self.query = (
                    "https://api.spoonacular.com/recipes/random"
                    + "?apiKey=" + self.db_apikey
                    + "&number=" + str(self.db_numofrecipes)
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
        canvas0 = Canvas(self.some_frame, width=1300, height=900)
        canvas0.pack()

        root.geometry("1300x900")

        longtxt2 = 'These are the ingredients necessary for your recipes for the week. \n                    Check the ingredients you already have.'
        txt2 = Label(self.some_frame, text=longtxt2, font=("Garamond", 16))
        canvas0.create_window(650,40, window=txt2)

        self.data = get_data(self.query)
        self.ids = get_random_recipe_ids(self.data)
        lst = []
        for id in self.ids:
            ingr_query = 'https://api.spoonacular.com/recipes/' + str(id) + '/ingredientWidget.json?apiKey=' + self.db_apikey
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
        
        def gotolist():
            self.some_frame.destroy()
            self.some_frame = None

            self.listofing = lst
            stateofing = ingdict.values()
            accum = []
            for element in stateofing:
                accum.append(element.get())
            self.stateofing = accum

            self.shopping_list()
        
        submitButton = Button(self.some_frame, text="Continue to Shopping List", style = 'W.TButton', command=gotolist)
        canvas0.create_window(650, 820, window=submitButton)

    def show_recipes(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()
        canvas0 = Canvas(self.some_frame, width=1000, height=600)
        canvas0.pack()

        root.geometry("1000x1000")

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
        canvas0 = Canvas(self.some_frame, width=1300, height=900)
        canvas0.pack()

        txt1 = Label(self.some_frame, text='Here is your shopping list for the week. Have fun!', font=("Garamond", 20))
        canvas0.create_window(400, 50, window=txt1)

        accumulator = 0
        for number in range(0, len(self.listofing)):
            if accumulator%2 == 0:
                x = 100
            else:
                x = 600
            if self.stateofing[number] == 2:
                Label(self.some_frame, text='Here is your shopping list for the week!', font=("Courier New", 13))
                canvas0.create_window(x, 140+20*accumulator, window=Label(self.some_frame, text=self.listofing[number], font=("Courier New", 12)), anchor=W)
                accumulator += 1
        root.geometry("1300x" + str(180+30*accumulator))
            
root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()