import math 
import random
import time
from datetime import datetime
class Randoms:
    now = datetime.now()
    currenttime = now.strftime("%H%M%S")
    rn=int(datetime.now().strftime("%H%M%S"))
    print('using seed',rn)
    random.seed(rn)
random1=Randoms()

def sp0():
    print('')
    print('_____________________________________________________________________')
    print('')
def sp1():
    print('')
    print('=====================================================================')
    print('')
def sp2():
    print('')
    print('---------------------------------------------------------------------')
    print('')
def sp3():
    print('-------')

recipesq=20
recipes=[]
for x in range(recipesq):
    recipes.append(' ')
recipes2=[]
for x in range(recipesq):
    recipes2.append(' ')


class Ingredient():
    ingredientsq=20
    ingredients=[]
    for x in range(ingredientsq):
        ingredients.append('x')
    ingredients2=[]
    for x in range(ingredientsq):
        ingredients2.append('x')
    def __init__(self,id,name,saltindex,meatindex,vegindex,protein,fat,glucid):
        self.id=id
        self.name=name
        self.saltindex=saltindex
        self.meatindex=meatindex
        self.vegindex=vegindex
        self.protein=protein
        self.fat=fat
        self.glucid=glucid
        Ingredient.ingredients[id]=self.name
        Ingredient.ingredients2[id]=self
    def scan(self):
        sp3()
        str4=''
        for x in self.name:
            str4=str4+' '
        print(f'{self.name.upper()} ____ salt{self.saltindex}')
        print(f'{str4} ____ vegetable{self.vegindex}')
        print(f'{str4} ____ meat{self.meatindex}')
        print(f'{str4} ____ protein{self.protein}')
        print(f'{str4} ____ fat{self.fat}')
        print(f'{str4} ____ glucid{self.glucid}')
        

class Recipe1():
    
    def __init__(self,id,name,ingredient1):
        self.id=id
        self.name=name
        self.ingredient1=ingredient1
        self.ingredients=[ingredient1]
        recipes[id]=self.name
        recipes2[id]=self
    def scan(self):
        print(f'{self.name}has 1 ingredient:{self.ingredient1.name}')
        self.ingredient1.scan() 
class Recipe2(Recipe1):
    def __init__(self,id,name,ingredient1,ingredient2):
        Recipe1.__init__(self,id,name,ingredient1)
        self.ingredient2=ingredient2
        self.ingredients=[ingredient1,ingredient2]
        recipes[id]=self.name
    def scan(self):
        print(f'{self.name}has 2 ingredients:{self.ingredient1.name}{self.ingredient2.name}')
        self.ingredient1.scan()
        self.ingredient2.scan()
class Recipe3(Recipe2):
    def __init__(self,id,name,ingredient1,ingredient2,ingredient3):
        Recipe2.__init__(self,id,name,ingredient1,ingredient2)
        self.ingredient3=ingredient3
        self.ingredients=[ingredient1,ingredient2,ingredient3]
        recipes[id]=self.name
    def scan(self):
        print(self.name,'has 3 ingredients:',self.ingredient1.name,',',self.ingredient2.name,',',self.ingredient3.name)
        self.ingredient1.scan()
        self.ingredient2.scan()
        self.ingredient3.scan()
class Recipe4(Recipe3):
    def __init__(self,id,name,ingredient1,ingredient2,ingredient3,ingredient4):
        Recipe3.__init__(self,id,name,ingredient1,ingredient2,ingredient3)
        self.ingredient4=ingredient4
        self.ingredients=[ingredient1,ingredient2,ingredient3,ingredient4]
        recipes[id]=self.name
    def scan(self):
        print(self.name,'has 4 ingredients:',self.ingredient1.name,',',self.ingredient2.name,',',self.ingredient3.name,',',self.ingredient4.name)
        self.ingredient1.scan()
        self.ingredient2.scan()
        self.ingredient3.scan()
        self.ingredient4.scan()
class Recipe5(Recipe4):
    def __init__(self,id,name,ingredient1,ingredient2,ingredient3,ingredient4,ingredient5):
        Recipe4.__init__(self,id,name,ingredient1,ingredient2,ingredient3,ingredient4)
        self.ingredient5=ingredient5
        self.ingredients=[ingredient1,ingredient2,ingredient3,ingredient4,ingredient5]
        recipes[id]=self.name
    def scan(self):
        print(self.name,'has 5 ingredients:',self.ingredient1.name,',',self.ingredient2.name,',',self.ingredient3.name,',',self.ingredient4.name,',',self.ingredient5)
        self.ingredient1.scan()
        self.ingredient2.scan()
        self.ingredient3.scan()
        self.ingredient4.scan()
        self.ingredient5.scan()
class Recipe6(Recipe5):
    def __init__(self,id,name,ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,ingredient6):
        Recipe5.__init__(self,id,name,ingredient1,ingredient2,ingredient3,ingredient4,ingredient5)
        self.ingredient6=ingredient6
        self.ingredients=[ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,ingredient6]
        recipes[id]=self.name
    def scan(self):
        print(self.name,'has 6 ingredients:',self.ingredient1.name,',',self.ingredient2.name,',',self.ingredient3.name,',',self.ingredient4.name,',',self.ingredient5,',',self.ingredient6)
        self.ingredient1.scan()
        self.ingredient2.scan()
        self.ingredient3.scan()
        self.ingredient4.scan()
        self.ingredient5.scan()
        self.ingredient6.scan()
class Recipe7(Recipe6):
    def __init__(self,id,name,ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,ingredient6,ingredient7):
        Recipe6.__init__(self,id,name,ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,ingredient6)
        self.ingredient7=ingredient7
        self.ingredients=[ingredient1,ingredient2,ingredient3,ingredient4,ingredient5,ingredient6,ingredient7]
        recipes[id]=self.name
    def scan(self):
        print(self.name,'has 7 ingredients:',self.ingredient1.name,',',self.ingredient2.name,',',self.ingredient3.name,',',self.ingredient4.name,',',self.ingredient5,',',self.ingredient6,',',self.ingredient7)
        self.ingredient1.scan()
        self.ingredient2.scan()
        self.ingredient3.scan()
        self.ingredient4.scan()
        self.ingredient5.scan()
        self.ingredient6.scan()
        self.ingredient7.scan()
        
#name=ingredient(id,name,salt,meat,veg,protein,fat,glucid)
corn=Ingredient(0,'corn',('unk'),0,1,0.104,0.053,0.82)
rice=Ingredient(1,'rice',('unk'),0,1,0.081,0.008,0.92)
wheat=Ingredient(2,'wheat',('unk'),0,1,0.145,0.018,0.82)
potatoes=Ingredient(3,'potatoes',('unk'),0,1,0.095,0.0004,0.81)
yuca=Ingredient(4,'yuca',('unk'),0,1,0.035,0.007,0.95)
soya=Ingredient(5,'soya',('unk'),0,1,0.406,0.216,0.34)
sweetpotato=Ingredient(6,'sweet potato',('unk'),0,1,0.07,0.002,0.34)
yam=Ingredient(7,'boniato',('unk'),0,1,0.05,0.006,0.93)
banana=Ingredient(8,'banana',('K'),0,1,0.037,0.011,0.91)

soymilk=Ingredient(9,'soy milk',(0.0001),0,1,0.0003,0.02,0.04)
cookies=Ingredient(10,'cookies',('un'),0,1,'unk','unk','unk')

tomato=Ingredient(11,'tomato',('unk'),0,1,0.009,0.002,0.039)
oliveoil=Ingredient(12,'olive oil',(0),0,1,0,1,0)
NaCl=Ingredient(13,'NaCl salt',('Na'),0,0,0,0,0)
mandarin=Ingredient(14,'mandarin',('unk')0,1,'u','u','u')

chicken=Ingredient(14,'chicken',('unknown'),1,0,0.2684,0.1256,0)
cheese=Ingredient(15,'cheese',('medium'),1,0,0.2,0.26,0.03)
egg=Ingredient(16,'egg',('unk'),1,0,0.126,0.106,0.0112)

#RECIPES

riceandchicken=Recipe2(0,'rice and chicken',rice,chicken)
cubanrice=Recipe3(1,'cuban rice',rice,egg,tomato)
bread=Recipe1(2,'bread',wheat)
toasts=Recipe3(3,'toasts',bread,oliveoil,NaCl)
breadandcheese=Recipe2(4,'bread and cheese',bread,cheese)
cubanricecomplete=Recipe4(5,'complete cuban rice',rice,egg,tomato,banana)
#milkandcookies=Recipe2(6,'milk and cookies',soymilk,cookies)

def debugger():
    sp0()
    print('DEBUGGER')
    print(debugger)
    sp1()
    print(str(riceandchicken.ingredient1.id),'has',riceandchicken.ingredient1.glucid*100,'percent glucid')
    sp1()
    cubanrice.scan()
    sp2()
    riceandchicken.scan()
    sp1()
    breadandcheese.scan()
    sp1()
    toasts.scan()
    sp1()
    print(Ingredient.ingredients)
    print(recipes)
    sp1()
    str1=' '
    y=-1
    for x in riceandchicken.ingredients:
        str1=str1+' '+(str(riceandchicken.ingredients[y].name))
        y=y+1
    print(type(riceandchicken.ingredients),riceandchicken.ingredients,str1)
    print(str1)
    print(riceandchicken.ingredients[0].name)
    print(riceandchicken.ingredients[1].name)
    print(Ingredient.ingredients)
    for i in range(len(Ingredient.ingredients)):
        print(Ingredient.ingredients[i])
    sp1()
#debugger()

def randomingredient():
    random1.rn=random1.rn+1
    random.seed(random1.rn)
    print(f'             {Ingredient.ingredients[int(random.randrange(len(Ingredient.ingredients)))]}')
#randomingredient()
def randomrecipe():
    random1.rn=random1.rn+1
    random.seed(random1.rn)
    print('             ',recipes[int(random.randrange(len(recipes)))])
#randomrecipe()
def ingredientAnalyzer():
    print(Ingredient.ingredients)
    str3=str(input('select ingredient:   '))
    for x in range(len(Ingredient.ingredients)):
        if Ingredient.ingredients[x]==str3.lower():
             Ingredient.ingredients2[x].scan()
#ingredientAnalyzer()
def recipeAnalyzer():
    print(recipes)
    str3=str(input('select recipe:   '))
    for x in range(len(recipes)):
        if recipes[x]==str3.lower():
             recipes2[x].scan()
#ingredientAnalyzer()
def whiletrue():
    while Ingredient.ingredients[-1]=='x':
        Ingredient.ingredients.pop(-1)
    while recipes[-1]==' ':
        recipes.pop(-1)
    while(True):
        menu='''
        ______________________________

        1. Show Ingredients
        2. Show All Recipes
        3. Show random ingredient
        4. Show random recipe
        5. Analyze Ingredient
        6. Analyze Recipe
        7. DEBUGGER
        8. END PROGRAM
        9. beta...
        ______________________________
        '''
        print(menu)
        try:
            option=input('option?  ')
            print('------------')
            try:
                option=int(option)
            except NameError as err:
                print(err,'error en el primertry del menu')
                '''
            if type(option) != int:
                print(type(option))
                print('only integers allowed')
            el
            '''
            if option==1:
                print(Ingredient.ingredients)
            elif option==2:
                print(recipes)
            elif option==3:
                randomingredient()
            elif option==4:
                randomrecipe()
            elif option==5:
                ingredientAnalyzer()
            elif option==6:
                recipeAnalyzer()     
            elif option==7:
                debugger()
                print('END OF PROGRAM')
                return
            elif option==8:
                print('END OF PROGRAM')
                return
            elif option==9:
                print('beta')
            else:

                print(type(option),'please dont try to hack the program')
        except NameError as err:
            print(err,'error al final del whiletrue')
whiletrue()





