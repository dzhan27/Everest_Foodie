from tkinter import *
from tkinter.ttk import *
import requests
import json

from get_info import get_data
from get_info import get_ingredients
from get_info import get_random_recipe_urls
from get_info import get_random_recipe_ids
from get_info import get_random_recipe_names

class Window(Frame):

    db_name = 'New User'
    db_apikey = '74384699376e430daeedabdc69e3e48e'
    db_numofrecipes = 0

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

        self.master.title("Culinary Odyssey")

        canvas0 = Canvas(self.some_frame, width=800, height=600)
        canvas0.pack()

        txt1 = Label(self.some_frame, text="\nWelcome to Culinary Odyssey.", font=("Garamond", 35))
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

        longtxt3 = '         Do you have any other preferences? \nIf so, enter (healthy, cheap, sustainable, or popular)'
        txt3 = Label(self.some_frame, text=longtxt3, font=("Garamond", 20))
        canvas0.create_window(415, 280, window=txt3)

        entry2 = Entry(self.some_frame)
        canvas0.create_window(400, 340, window=entry2)

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
                self.query = 'https://api.spoonacular.com/recipes/random?apiKey=' + self.db_apikey
            else:
                self.query = (
                    "https://api.spoonacular.com/recipes/random"
                    + "?apiKey=" + self.db_apikey
                    + "number=" + str(self.db_numofrecipes)
                    + "&tags=" + restrictions + ',' + preferences
                )

            print(self.query)

            self.some_frame.destroy()
            self.some_frame = None
            self.show_recipes()

        submitButton = Button(self.some_frame, text="Submit!", style = 'W.TButton', command = query)
        canvas0.create_window(400, 380, window=submitButton)

    def ingredient_list(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()
        canvas0 = Canvas(self.some_frame, width=800, height=600)
        canvas0.pack()

        longtxt2 = 'These are the ingredients necessary for your recipes for the week. \n                    Check the ingredients you already have.'
        txt2 = Label(self.some_frame, text=longtxt2, font=("Garamond", 16))
        canvas0.create_window(400,40, window=txt2)

        self.data = get_data(self.query)
        self.ids = get_random_recipe_ids(self.data)
        lst = []
        for id in self.ids:
            ingr_query = 'https://api.spoonacular.com/recipes/' + str(id) + '/ingredientWidget.json?apiKey=' + self.db_apikey
            lst += get_ingredients(ingr_query) #replace with ingredient list

        accx = 85
        accy = 130
        dict = {}
        for number in range(0,len(lst)):
            dict[number] = IntVar()
            if number%3==0:
                x = accx
            elif number%3==1:
                x = accx + 250
            else:
                x = accx + 500
            y = accy + (number//3)*50

            ingrcheck = Checkbutton(self.some_frame, text='', variable=dict[number])
            canvas0.create_window(x,y, window=ingrcheck)

            txt1 = Label(self.some_frame, text=lst[number], font=("Courier New", 14))
            canvas0.create_window(x+20,y, window=txt1, anchor=W)
            print(IntVar())

    def show_recipes(self):
        self.some_frame = Frame(self.master)
        self.some_frame.pack()
        canvas0 = Canvas(self.some_frame, width=800, height=600)
        canvas0.pack()

        longtxt2 = 'Here are your recipes! \n                    Check the ingredients you already have.'
        txt2 = Label(self.some_frame, text=longtxt2, font=("Garamond", 16))
        canvas0.create_window(400,40, window=txt2)

        self.data = get_data(self.query) # delete later
        lst = get_random_recipe_urls(self.data)

        names = get_random_recipe_names(self.data)

        accx = 85
        accy = 130
        dict = {}
        for number in range(0,len(lst)):
            dict[number] = IntVar()
            if number%3==0:
                x = accx
            elif number%3==1:
                x = accx + 250
            else:
                x = accx + 500
            y = accy + (number//3)*50


            txt1 = Label(self.some_frame, text=names[number], font=("Courier New", 14))
            canvas0.create_window(x+20,y, window=txt1, anchor=W)

            link1 = Label(root, text=lst[number], fg="blue", cursor="hand2")
            canvas0.create_window(x+20,y+40, window=link1, anchor=W)
            # link1 = Label(root, text="See the recipe!", fg="blue", cursor="hand2")
            # canvas0.create_window(x+20,y+40, window=link1, anchor=W)
            # link1.bind("<Button-1>", lambda e: callback(lst[number]))




root = Tk()
root.geometry("800x600")
app = Window(root)
root.mainloop()
