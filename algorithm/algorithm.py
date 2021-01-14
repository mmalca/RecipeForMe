__author__ = 'mmalca'

from algorithm import algorithm_helper
from db import db_operations
from scipy import spatial

### CORE ALGORITHM FUNCTION ###

def choose_recipe(ingredients_from_user):
    ing_count_threshold = 0.4
    distance_threshold = 0.5
    score_threshold = 80
    final_list = []
    ## access to the ingredients list from db
    ingredients_list = db_operations.get_ingredients_list()
    ingredients_count = ingredients_list.count()
    ## access to recipes list in db
    recipes_list = db_operations.get_recipes_list()
    for recipe in recipes_list:
        replaced = []
        print(recipe)
        #   break
        is_match, missed_ingredients = algorithm_helper.ingredients_to_recipe_comparison(recipe, ingredients_from_user, ingredients_count)
        score = 100
        if is_match:
            score = round(score,2)
            recipe["score"] = score
            final_list.append(recipe)
            continue
        else:
            missed_ing_count = algorithm_helper.how_many_missed_ingredients(missed_ingredients)
            recipe_ing_count = len(recipe['ingredients'])
            rate = (missed_ing_count / recipe_ing_count)
            if rate > ing_count_threshold:
                #print("missed more than " + ing_count_threshold + "continue")
                continue
            else:
                i = 0
                for missed_ing in missed_ingredients:
                    if missed_ing != 1:
                        i += 1
                        continue
                    else:
                        #score = 100
                        #max_score = 0
                        rec_missed_ing = db_operations.get_ing_by_id(i)
                        #####
                        if rec_missed_ing['name'] == 'אורז לבן':
                            rec_missed_ing = db_operations.get_ing_by_name('אורז')
                        rec_vec = rec_missed_ing['vector']
                        max_dist = 0
                        for user_ing_id in ingredients_from_user:
                            user_ing = db_operations.get_ing_by_id(user_ing_id)
                            ####
                            if user_ing['name'] == 'אורז לבן':
                                user_ing = db_operations.get_ing_by_name('אורז')
                            user_vec = user_ing['vector']
                            user_ing_name = user_ing['name']
                            #
                            distance_vec = 1 - spatial.distance.cosine(rec_vec, user_vec)
                            if distance_vec > distance_threshold:
                                if distance_vec  > max_dist:
                                    max_dist = distance_vec
                        if max_dist == 0:
                            break # move to next recipe
                        else:
                            score -= (1-max_dist)
                            replace_ing = db_operations.get_ing_by_id(missed_ing)
                            my_tuple = (rec_missed_ing['name'], user_ing_name)
                            replaced.append(my_tuple)
                        i += 1

                    if score > score_threshold:
                        score = round(score, 2)
                        recipe["score"] = score
                        recipe["replaced"] = replaced
                        final_list.append(recipe)
        # for user_ingredient in ingredients_from_user:
        #    if recipe_ingredient._id != user_ingredient._id and recipe_ingredient._id:

    # checking vector distance between ingredients and setting score to recipe

    ###
    #sorted_obj = dict(final_list)
    final_list = sorted(final_list, key=lambda i: i['score'], reverse=True)
    print(final_list)
    return final_list
    ## send to user back, using http_server functions
    print()  ## to delete after
