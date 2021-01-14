__author__ = 'mmalca'


import pymongo
from db import db_operations
#db_operations.add_ingredients_from_recipe(dict)

#col =  db_init.init_collection('counters')
#col.insert({"_id":get_next_sequence_value("ingredientid"),
                #    "name":recipe_ing})


######################################################################################################
    ###  Adding new recipe ####


# from db import db_operations
# name = ""
# ingredients = []
# directions = []
# db_operations.add_recipe(name,ingredients , directions, "jpg")
#
#     ########### test - printing the recipe that we have inserted:
#
# from db import db_init
# collection = db_init.init_collection('recipes')
# myquery = { "name":name}
# mydoc = collection.find(myquery)
# for doc in mydoc:
#     id = doc["_id"]
#     print(doc)
    ########### fixing specific element of our recipe if needed

# from db import db_init
# collection = db_init.init_collection('recipes')
# myquery = { "name":"עוגת כדורי שוקולד"}
# mydoc = collection.find(myquery)
# for doc in mydoc:
#     id = id = doc["_id"]
    ##to_update_pic = "C:\pictures\\" + str(id) + ".jpg"
    ##to_update_ing = [{"name":"","amount" :""}, {"name":"","amount" :""}, {"name":"","amount" :""},{"name":"","amount" :""}, {"name":"","amount" :""}, {"name":"","amount" :""},{"name":"","amount" :""}, {"name":"","amount" :""}, {"name":"","amount" :""}]
    ##to_update_ing = [{"name":"בצל","amount" :"1"}, {"name":"שום","amount" :"2-3 שיניים"}, {"name":"אפונה","amount" :"2 כוסות"},{"name":"","amount" :""}, {"name":"שעועית ירוקה","amount" :"3 כוסות"}, {"name":"","amount" :""},{"name":"מים","amount" :"שליש כוס"}, {"name":"מלח","amount" :"חצי כפית"}, {"name":"כורכום","amount" :"רבע כפית"},{"name":"אבקת מרק","amount" :"כפית"},{"name":"פלפל שחור","amount" :"מעט"}]
    # to_update_ing = [{"name":"ביסקוויט","amount" :"400 גרם"},
    #  {"name":"שמנת מתוקה","amount" :"375 מל"},
    #  {"name":"שוקולד מריר","amount" :"200 גרם"}]

    # updated = collection.find_one_and_update(
    #         {"_id" : id},
    #         {"$set":
    #             {"ingredients": to_update_ing}
    #
    #         },upsert=True
    #     )

        ################# print all recipes

# from db import db_init
# collection = db_init.init_collection('recipes')
# docs = collection.find()
# for doc in docs:
#     print(doc)
#     print()
#     print("=======================")
#     print()

######################################################################################################


########################### MAYA - test validations before inserting data to db #################################
########################### WIP #################################

# import json
# import jsonschema
# from jsonschema import validate
#
#
# ing = [{"name": "סוכר", "amount": "חצי כוס"}, {"name": "ביצה", "amount":"2"}]
# dir = ["שלב1","שלב2"]
#
# recipe = {
#     "name" : 123,
#     "ingredients" : dir,
#     "directions" : dir
# }
# schema = {
#     "type": "object",
#     "name": {"type" : "string"},
#     "ingredients":[{"name":{"type": "string"}, "amount" : {"type":"string"}}],
#     "directions": [{"type" : "string"}]
# }
#
# try:
#     validate(instance=recipe, schema=schema)
# except schema.exceptions.ValidationError as err:
#     print(False)
######################################################################################
######################################################################################



######################################################################################
########### Maya - tests regarding inserting ingredients from recipe ###########
########### did't work with inserting vectors, changed to list .tolist() - V ###########

import fasttext
ingredients = db_operations.init_collection("ingredients")
counters = db_operations.init_collection("counters")
    # c = counters.find()
    # for x in c:
    #     print(x)
# i = ingredients.find()
# for ing in i:
#     print(ing)
# #for recipe_ing in recipe['ingredients']:
#         ##print(recipe_ing)
#
# #ingredients.find()
# print("-------after:--------")
#
#############
# i = ingredients.find()
# for ing in i:
#     print(ing)
# name = "מלפפון"
# if ingredients.find_one({"name":name}) == None:
# #             #this is a new ingredient, add to ingredients collection:
#     ft = fasttext.load_model('cc.he.300.bin')
#     vector = ft.get_word_vector(name) ##use fsst text op
#     vector_list = vector.tolist()
#     id = db_operations.get_next_sequence_value()
#     print(id)
#     ingredients.insert_one({"_id":id,
#                                  "name":name,
#                                  "vector": vector_list
#                                  })


#
#
# i = ingredients.find()
# for ing in i:
#     print(ing)

import numpy
#vector_new = vector.tolist()
#print(type(vector_new))

     ### back to ndarray
# vec=numpy.array([numpy.array(v) for v in vector_new])
# print(type(vec))
####
#i = ingredients.find()
#for ing in i:
#    print(ing)


######################################################################################
########### Maya - tests regarding distances with lists instead of vectors ###########
########### working well with lists - V ###########

def test_distances():
    ft = fasttext.load_model('cc.he.300.bin')
    vector1 = ft.get_word_vector("שמנת") ##use fsst text op
    vector_list = vector1.tolist()

    vector2 = ft.get_word_vector("גבינה") ##use fsst text op
    vector_list = vector2.tolist()

    from scipy import spatial

    distance_vec = 1 - spatial.distance.cosine(vector1, vector2)
    print("distance_vec = ")
    print(distance_vec)
    list1 = vector1.tolist()  ### ---> this!
    list2 = vector2.tolist()
    distance_lists = 1 - spatial.distance.cosine(list1, list2)
    print("distance_lists = ")
    print(distance_lists)

    b1 = numpy.array(list1)#([numpy.array(v1) for v1 in list1])
    b2 = numpy.array(list2)#([numpy.array(v2) for v2 in list2])
    distance_vec_after = 1 - spatial.distance.cosine(b1, b2)
    print("distance_vec_after = ")
    print(distance_vec_after)

######################################################################################
######################################################################################

############ Worked on adding missing data - fixed recipes, set counter to 0 and added all ingredients of my recipes. ####
#### תבשיל שעועית ואפונה, עוגת כדורי שוקולד, מוס שוקולד#########


from db import db_operations

#ingredients_collection = db_operations.init_collection("ingredients")
#
#ingredients = ingredients_collection.find().count()
#
# #for i in ingredients:
# #    print (i)
#print (ingredients)
#
recipe_collection = db_operations.init_collection("recipes")
recipes = recipe_collection.find()
for r in recipes:
    print (r["name"])

    print("---------")

recipe = recipe_collection.find_one({"name":"מוס שוקולד"})
db_operations.add_ingredients_from_recipe(recipe)

ings = recipe["ingredients"]
for ing in ings:
    print(ing)

ingredients_collection = db_operations.init_collection("ingredients")
#
ingredients = ingredients_collection.find()
#
for i in ingredients:
    print (i)
#print (ingredients)



# recipes = recipe_collection.find()
# for r in recipes:
#     print (r)
#     print()
#     print("--------------------")
#     print()
#
#rec = recipe_collection.find_one({"name" : "תבשיל שעועית ואפונה"})
# db_operations.add_ingredients_from_recipe(rec)
#
# ingredients = ingredients_collection.find()
# for i in ingredients:
#     print (i)
#######################################################################################
#######################################################################################

###  September 23 ###
##
# ingredients = [{"name": "פסטה", "amount": "1 כוס"}, {"name": "מים", "amount":"1/2 כוס"}, {"name": "חלב", "amount":"2 כפות"}, {"name": "חמאה", "amount":"1 כפית"}, {"name": "גבינה צהובה", "amount":"1/2 כוס"}, {"name": "מלח", "amount":"1/2 כפית"}]
# directions = ["מכניסים את הפסטה לכוס או קערית גדולה.", "מוסיפים את המים והמלח ומערבבים","מכניסים למיקרוגל ומחממים בעוצמה הגבוהה במשך 4.5 דקות." , "מוציאים מהמיקרוגל ויוצקים על הפסטה את החלב.", "מניחים על הפסטה את החמאה ואת הגבינות המגורדות ומערבבים", "מכניסים שוב למיקרוגל לחצי דקה נוספת. מוציאים, מערבבים ומגישים."]
#
# db_operations.add_recipe("מק אנד צ'יז במיקרו",ingredients , directions, "jpg")

#     ########### test - printing the recipe that we have inserted:
#

#############3
# from db import db_init
# collection = db_init.init_collection('recipes')
# myquery = { "name":"מק אנד צ'יז במיקרו"}
#
#
# r = collection.find(myquery)
# for i in r:
#     print(i)
#     print("---")
#############
# from db import db_init
# collection = db_init.init_collection('ingredients')
#
# f = collection.find_one({"name":"בצל"})
# print(f)

# db_response = db_operations.get_ingredients_list()
# for i in db_response:
#     print (i)
#     print("\n=====\n"  )

#from db import db_operations
#db_operations.add_ingredients(["בצל סגול"])

# from db import db_init
# collection = db_init.init_collection('ingredients')
# f = collection.find_one({"name":"בצל סגול"})
# print(f)

from db import db_operations

def verify_all_recipe_ings_and_add_if_needed():
    recipes_collection = db_operations.init_collection("recipes")
    #ings = db_operations.init_collection("ingredients")
    recipes = recipe_collection.find()
    for r in recipes:
        db_operations.add_ingredients_from_recipe(r)