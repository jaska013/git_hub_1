human1 = input("choose the country:")
country = ("The USSR", "GERMANY", "USA", "GB") #cтрана
tuple1 = ()
for i in country:
    if human1 == i:
        tuple1 = human1
print(tuple1)
tuple2 = ()
type_of_tanks = ("light_tanks", "medium_tanks", "heavy_tanks", "tank_destroyers", "self_propelled_guns")
light_tanks, medium_tanks, heavy_tanks, tank_destroyers, self_propelled_guns = 'LT', 'MT', 'HT', 'TD', 'SPG'
human2 = input("choose the type (LT, MT, HT, TD, SPG) ->:  ")
for i in type_of_tanks:
    if human2 == i:
        tuple2 = human2
print(tuple2)
