__author__ = 'mmalca'

import fasttext
import fasttext.util
from db import db_init

def get_rec():
    collection = db_init.init_collection('recipes')
    mydoc = collection.find()
    for doc in mydoc:
        id = doc["_id"]
        print(doc)

def remove_rec():
    collection = db_init.init_collection('recipes')
    collection.delete_one({"name": "פיתה מטוגנת"})

    collection2 = db_init.init_collection('ingredients')
    collection2.delete_one({"name":"פיתות"})

def get_ing():
    collection = db_init.init_collection('ingredients')
    #myquery = { "name":"תפוח אדמה"}
    mydoc = collection.find()
    print(mydoc)
    for doc in mydoc:
        id = doc["_id"]
        print(id)
from db import db_operations
from db import db_init
def add_rec():
    name = "אפונה"
    ingredients = [{"name":"אפונה","amount" :"2 כוסות"}, {"name":"מים","amount" :"חצי כוס"}, {"name":"שום","amount" :"2 שיניים"},  {"name":"כורכום","amount" :"רבע כפית"}, {"name":"כמון","amount" :"רבע כפית"},  {"name":"אבקת מרק","amount" :"כפית"}, {"name":"מלח","amount" :"כפית"}, {"name":"פלפל שחור","amount" :"קמצוץ"}]
    directions = ["מחממים מחבת רחבה עם כף שמן ומוסיפים את השום והאפונה (אין צורך להפשיר לפני). מערבבים במשך כ-2 דקות.", "מוסיפים חצי כוס מים ומתבלים באבקת מרק, מלח, כורכום, כמון ופלפל שחור. מבשלים עם מכסה על אש בינונית במשך 8-10 דקות, עד שהרוטב מצטמצם." ]
    db_operations.add_recipe(name,ingredients , directions, "jpg")
#
# #     ########### test - printing the recipe that we have inserted:
# #

    collection = db_init.init_collection('recipes')
    myquery = { "name":name}
    mydoc = collection.find(myquery)
    for doc in mydoc:
        id = doc["_id"]
        print(doc)
#
#     ########### test - print new ingredirnts list
# ingredients_list = db_operations.get_ingredients_list()
# print("new ingredients list (only names and ids): ---------------")
# for i in ingredients_list:
#     print(i)


#fasttext.util.download_model('he', if_exists='ignore')
#ft_he = fasttext.load_model('cc.he.300.bin')

#     ####  Adding new recipe ####
#
from db import db_operations
def myfunc():
     ingredients = [{"name": "עלי בייבי", "amount": "1 חבילה"}, {"name": "עגבנית שרי", "amount":"חופן"}, {"name": "אפרסק", "amount":"1"}, {"name": "מוצרלה", "amount":"150 גרם"} , {"name": "חומץ בלסמי", "amount":"4 כפיות"} , {"name": "מלח", "amount":"1 כפית"}]
     directions = ["בקערה גדולה מערבבים את העלים עם העגבניות ופרוסות האפרסק.", "קורעים את המוצרלה לחתיכות גסות בידיים ומוסיפים לקערה.","מתבלים בשמן הזית, בחומץ הבלסמי ובמלח. מערבבים, טועמים ומוסיפים מלח או חומץ לפי הטעם." ]
     #db_operations.add_recipe("סלט ירוק עם אפרסקים וגבינה ברוטב בלסמי",ingredients , directions, "jpg")
     from db import db_init
     collection = db_init.init_collection('recipes')
     myquery = { "name":"סלט ירוק עם אפרסקים וגבינה ברוטב בלסמי"}
     mydoc = collection.find(myquery)
     for doc in mydoc:
         id = id = doc["_id"]
         print(id)

    #ingredients = [{"name": "פסטה", "amount": "1 כוס"}, {"name": "מים", "amount":"1/2 כוס"}, {"name": "חלב", "amount":"2 כפות"}, {"name": "חמאה", "amount":"1 כפית"}, {"name": "גבינה צהובה", "amount":"1/2 כוס"}, {"name": "מלח", "amount":"1/2 כפית"}]
    #directions = ["מכניסים את הפסטה לכוס או קערית גדולה.", "מוסיפים את המים והמלח ומערבבים","מכניסים למיקרוגל ומחממים בעוצמה הגבוהה במשך 4.5 דקות." , "מוציאים מהמיקרוגל ויוצקים על הפסטה את החלב.", "מניחים על הפסטה את החמאה ואת הגבינות המגורדות ומערבבים", "מכניסים שוב למיקרוגל לחצי דקה נוספת. מוציאים, מערבבים ומגישים."]

    #db_operations.add_recipe("מק אנד צ'יז במיקרו",ingredients , directions, "jpg")

#     ########### test - printing the recipe that we have inserted:
#
    #from db import db_init
    #collection = db_init.init_collection('recipes')
    #for c in collection:
    #    print(c)
    #myquery = { "name":"מק אנד צ'יז במיקרו"}
    #r = collection.find_One(myquery)
    #print(r)

## from http_server.server_init import init_server
#from http_server import JsonOperations ##import *
from fast_test_operations.first_impression import first_try
from db import db_operations ## import *

# my tries to serialize / deserialize from/to json
# j = '{"action": "print", "method": "onData", "data": "Madan Mohan"}'
#p = JsonToObject(j)

#r = Recipe('hodaya', 123)
#m = r.ObjectToJson()
#print(m)
# end of json tests

##first_try()
#Connect to the DB
#myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
#GetIngredients()
#init_server()



####### Hodaya's test

# import pymongo
# mongo_server = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
# from algorithm import algorithm_helper
# id = algorithm_helper.get_ingredient_id_by_name("בצל")
#
# collection = db_init.init_collection('recipes')
# recipe = collection.find_one()
# print(recipe)
#
# collection = db_init.init_collection('ingredients')
# #doc = collection.find_one({ "name": "בצל" })
# items_in_ing_col_count = collection.count_documents({})
# bin1 = algorithm_helper.from_recipe_to_ingredients_binary(recipe, items_in_ing_col_count)
# bin = algorithm_helper.from_ingredients_to_binary(recipe['ingredients'], items_in_ing_col_count)
# print(bin)

