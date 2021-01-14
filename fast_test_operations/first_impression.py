### This file will be erased ###

import fasttext
import fasttext.util
from scipy import spatial

def first_try():
    fasttext.util.download_model('he', if_exists='ignore')

    ft_he = fasttext.load_model('cc.he.300.bin')
    # fasttext.util.reduce_model(ft_en, 100)
    #ft_he.save_model('cc.en.100.bin')
    #
    # print("done english")
    #fasttext.util.download_model('en', if_exists='ignore')
    ing = ['עגבניה',
           'מלפפון',
            'פלפל',
           'בצל',
           'שום',
           'חסה',
            'גזר',
           'זיתים',
            'בטטה',
            'פטרוזיליה',
           'כוסברה',
           'סלרי',
           'קישוא',
           'תירס',
           'סלק',
          'פטריות',
           'שעועית ירוקה',
            'תפוח אדמה',

           'אורז',
           'שעועית',
            'חומוס',
           'עדשים',

            'תפוח',
           'תפוז',
           'בננה',
            'שזיפים',
           'משמשים',
           'צימוקים',

           'פפריקה',
            'כרכום',
            'רסק עגבניות',
           'אבקת מרק',
           'מלח',
           'סוכר',

           'קוקוס',
           'חמאה',
          'שוקולד',
           'קקאו',

           'פודינג',
           'ביסקוויט',
           'קפה',
           'חלב',
           'שמן',
           'קמח',
           'שמרים',
            'קורנפלור',
           'אבקת אפיה',
            'אבקת סוכר',
           'שיבולת שועל',
           'תמצית וניל',
           'שמנת צמחית',
           'חמאת בוטנים',
           'פצפוצי אורז',
            'שמנת מתוקה',
            'קינמון',
           'סודה לשתיה',
            'טחינה',
           'סילאן',
           'ריבה',
            'מייפל',

           'טופו',
           'עוף',
           'ביצה',
           'בשר',
           'דג',
           'מיונז',
           'קטשופ',

            'חלב סויה',
            'גבינה',
           'שמנת',
           'קוטג',
            'גבינה צהובה',
           'מים',
            'יין',
           'עגבנייה'
            ]

    ing_en = [
         'Tomato',
           'cucumber',
            'pepper',
           'Onion',
           'garlic',
           'lettuce',
            'Carrot',
           'olives',
            'sweet potato',
            'parsley',
           'coriander',
           'celery',
           'Squash',
           'corn',
           'beet',
          'mushrooms',
           'green beans',
            'Potato',

           'Rice',
           'bean',
            'Hummus',
           'Lentils',

            'Apple',
           'orange',
           'Banana',
            'plum',
           'Apricot',
           'raisins',

            'paprika',
            'turmeric',
            'Tomato paste',
           'Soup powder',
           'Salt',
           'Sugar',

           'coconut',
           'butter',
          'chocolate',
           'cocoa',

           'pudding',
           'Biscuit',
           'coffee',
           'milk',
           'Oil',
           'flour',
           'yeast',
           'Cornflour',
           'Baking powder',
            'sugar powder',
           'Oatmeal',
           'Vanilla extract',
           'vegetarian whipped cream',
           'Peanut Butter',
           'Rice Crackers',
            'whipping cream',
            'cinnamon',
           'Drinking soda',
            'Tehina',
           'Date Honey',
           'Jam',
            'Maple',

           'Tofu',
           'chicken',
           'egg',
           'meat',
           'Fish',
           'mayonnaise',
           'ketchup',

            'soy milk',
            'cheese',
           'cream',
           'cottage cheese',
            'cheddar',
           'water',
            'wine'

    ]

    ft = fasttext.load_model('cc.he.300.bin')
    ft_en = fasttext.load_model('cc.en.300.bin')


    for v1, v1_en in zip(ing, ing_en):
        for v2, v2_en in zip(ing, ing_en):
            vector1 = ft.get_word_vector(v1)
            vector1_en = ft_en.get_word_vector(v1_en)
            vector2 = ft.get_word_vector(v2)
            vector2_en = ft_en.get_word_vector(v2_en)
            cosine_similarity = 1 - spatial.distance.cosine(vector1, vector2)
            cosine_similarity_en = 1 - spatial.distance.cosine(vector1_en, vector2_en)

            #similarity = spatial.distance.sqeuclidean(vector1, vector2)
            print("v1:",v1,"[v1_en:",v1_en, "]", "v2: ", v2,"[v2_en:",v2_en, "]" ,"similarity is ========= ",cosine_similarity, "[english: ", cosine_similarity_en, "]")

    '''
    vec1=ing[0]
    vec2=ing[1]
    print(vec1)
    print(vec2)
    vector1=ft.get_word_vector(vec1)
    vector2=ft.get_word_vector(vec2)

    cosine_similarity = 1 - spatial.distance.cosine(vector1, vector2)

    print(cosine_similarity)
'''




    # print("reducing heb model")
    # fasttext.util.reduce_model(ft_he, 100)
    # print("done - reducing heb model")
    # ft_he.save_model('cc.he.100.bin')


    #fasttext.util.download_model('he', if_exists='ignore')

    # potato_he = ft_he.get_nearest_neighbors('תפוח אדמה')
    # print(potato_he)

    # potato_en = ft.get_nearest_neighbors('potato')
    # print(potato_en)
    # print()
    #
    # chocolate_he = ft_he.get_nearest_neighbors('שוקולד')
    # print(chocolate_he)
    #
    # chocolate_en = ft.get_nearest_neighbors('chocolate')
    # print(chocolate_en)
    # print()
    #
    # coconut_he = ft_he.get_nearest_neighbors('קוקוס')
    # print(coconut_he)
    # coconut_en = ft.get_nearest_neighbors('coconut')
    # print(coconut_en)
    # print()
    #
    # egg_he = ft_he.get_nearest_neighbors('ביצה')
    # print(egg_he)
    # egg_en = ft.get_nearest_neighbors('egg')
    # print(egg_en)
    # print()
    #
    # rice_he = ft_he.get_nearest_neighbors('אורז')
    # print(rice_he)
    # rice_en = ft.get_nearest_neighbors('rice')
    # print(rice_en)
    # print()
    #
    # flour_he = ft_he.get_nearest_neighbors('קמח')
    # print(flour_he)
    # flour_en = ft.get_nearest_neighbors('flour')
    # print(flour_en)
    # print()


    # ft_he = fasttext.load_model('wiki.he.bin')
    # #fasttext.util.reduce_model(ft_he, 50)
    #
    # #ft = fasttext.load_model('cc.en.300.bin')
    # #fasttext.util.reduce_model(ft, 100)
    #
    #
    # potato_he = ft_he.get_nearest_neighbors('עגבניה')
    # print(potato_he)
    # fasttext.util.reduce_model(ft_he, 100)
    # potato_he = ft_he.get_nearest_neighbors('עגבניה')
    # print(potato_he)




