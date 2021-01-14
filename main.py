from algorithm import algorithm
algorithm.choose_recipe([1,2,3,4,5,6,7,8,9])
#
# from db import db_operations
#
# col = db_operations.init_collection("recipes")
# recipes = col.find()
#
# i = 1
# for r in recipes:
#     print(i)
#     i=i+1
#     print(r["name"])
#     print(r["pictureName"])
#     print()
#     print("----")
#     print()

# picture_type = "jpg"


###############################
#
# name ="טבעות תפוחים מטוגנות"
#
# ingredients = [
# {"name":"תפוח","amount" :"3"},
# {"name":"ביצה","amount" :"1"},
# {"name":"סוכר","amount" :"2 כפות"},
#
# {"name":"מיץ תפוזים","amount" :"שלושת רבעי כוס"},
# {"name":"קינמון","amount" :"חצי כפית"},
#
# {"name":"קמח תופח","amount" :"כוס"}
# ]
#
#
# directions = [
# "חותכים את התפוחים הקלופים לפרוסות עגולות בעובי של עד חצי סמ (לא מומלץ לחתוך עבה יותר). קורצים באמצע בעזרת חותכן עגול קטן או פקק של בקבוק (ניתן להעזר גם בסכין) לקבלת צורה של טבעת.",
# "מערבבים את חומרי הבלילה בקערה עד לקבלת בלילה חלקה (מומלץ להשתמש במטרפה ידנית).",
# "מחממים סיר קטן/בינוני בשמן עמוק (גובה השמן לפחות 3-4 סמ). טובלים כל טבעת תפוח בבלילה משני הצדדים וכשהשמן חם, מוסיפים בזהירות לשמן, מנמיכים לאש בינונית ומטגנים כדקה וחצי-שתיים מכל צד, עד להשחמה. מעבירים לצלחת עם נייר סופג.",
# "מומלץ לטגן עד 3-5 יחידות בכל פעם (זה תלוי בגודל הסיר, צריך שיהיה מקום לכולם לצוף מעל השמן).",
# "הצעות להגשה: לפזר מעל אבקת סוכר, לערבב כף סוכר עם חצי כפית אבקת קינמון ולטבול משני הצדדים מיד לאחר הטיגון, לזלף מעל סירופ מייפל."
# ]
#
#
#
# db_operations.add_recipe(name, ingredients, directions, picture_type)
#
# col = db_operations.init_collection("recipes")
# rec = col.find_one({"name": name})
# print(rec["pictureName"])