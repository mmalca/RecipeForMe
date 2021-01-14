from db.db_init import init_collection
##import pymongo
from fast_test_operations import fast_text

def get_ingredients_list(): ## returns only names and _ids
    ingredients_collection = init_collection("ingredients")
    ingredients_list = ingredients_collection.find({},{'name' : 1})
    return ingredients_list

def get_recipes_list():
    recipes_collection = init_collection("recipes")
    recipes_list = recipes_collection.find({},{"_id": 0})
    return recipes_list

#### TO NOT USE !!!! #########################
def add_ingredients(ingredients_list): ## gerring list of names - strings
    # myclient = pymongo.MongoClient("mongodb://193.106.55.98:5000/")
    # mydb = myclient["RecipeForMe"]
    # ingredientsCollection = mydb["ingredients"]
    ingredients_collection = init_collection("ingredients")

    # ingredients_collection.insert_many(ingredients_list)
    #
    # documents = ingredients_collection.find()
    # for x in documents:
    #     print(x)


   # for ing in ingredients_list:
    vector = fast_text.get_vector(ingredients_list) ##use fsst text op
    vector_list = vector.tolist()
    #id = get_next_sequence_value()
    id=40
    ingredients_collection.insert_one({"_id": id,
                                "name":ingredients_list,#ing,
                                "vector": vector_list
                                })
#############################################

def add_ingredients_from_recipe(recipe):
    #Create a dictionary and add to the Collection
    ##TO: for each ingredient in list: if does not exist: add to

    ingredients = init_collection("ingredients")
    counters = init_collection("counters")

    for recipe_ing in recipe['ingredients']:
        ##print(recipe_ing)
        name = recipe_ing["name"]
        if (ingredients.find_one({"name":name}) == None) and name != "":
            #only is it is a new ingredient, add to ingredients collection:
            vector = fast_text.get_vector(name) ##use fsst text op
            vector_list = vector.tolist()
            id = get_next_sequence_value()
            ingredients.insert_one({"_id": id,
                                "name":name,
                                "vector": vector_list
                                })


#returns the next sequence for the increasing counter (sequence_name=ingredientid)
def get_next_sequence_value():
    collection = init_collection("counters")
    sequence_document = collection.find_and_modify(
        query = {'_id': "ingredientid" },
        update = {"$inc":{'sequence_value':1}},
        new = 'true' ##?
    )
    return sequence_document["sequence_value"]

    ##### TO USE WHEN INSERTING INGREDIENT: #####
    #.insert({"_id":get_next_sequence_value("ingredientid"),
    #       "name": ....
    #       ...})


def add_recipe(name, ingredients, directions, picture_type):
    collection = init_collection('recipes')
    exist = collection.find_one({"name":name})
    if exist != None:
        print("ERROR - Already exist recipe with this name!")
        return
    collection.insert_one({"name":name,
                           "ingredients":ingredients,
                           "directions":directions
                           #"pictureName":'C:\pictures\default.jpg'
                           })
    #adding picture name
    myquery = { "name": name ,  "pictureName" : { "$exists": False } }
    mydoc = collection.find(myquery) ## change to find_one?? and then loop is not required??
    # update picture name

    ##add validation: only if there is only one doc -- add (for case of )
    for doc in mydoc: # suppose to find only one

        id = doc["_id"]
    # add picture name filed
        picture_url = str(id) + "." + picture_type
        updated = collection.find_one_and_update(
            {"_id" : id},
            {"$set":
                {"pictureName": picture_url}
            },upsert=True
        )
    #update={ "$set": { "pictureName": { "$regex": "^S" } } }
    #collection.update_one(myquery, update)
        add_ingredients_from_recipe(doc)


    # print the doc dict returned by API call
    if type(updated) == dict:
        print ("doc dict obj:", updated)

def get_ing_by_id(id):
    ingredients_collection = init_collection("ingredients")
    return ingredients_collection.find_one({"_id" : id})


def get_ing_by_name(name):
    ingredients_collection = init_collection("ingredients")
    return ingredients_collection.find_one({"name" : name})
