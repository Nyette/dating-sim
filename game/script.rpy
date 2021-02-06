init python:
    config.automatic_images = [ '/' , '_' , ' ' ]
    config.main_menu_music = "music/destiny.mp3"

# Player
default my_name = "Kevin"
default my_major = "computer science"

# Cat
default cat_name = "???"
default cat_appearance = "pink hair and unusually large breasts"
default cat_major = "biology"

# Fish
default fish_name = "???"

# Locations
default town_name = "Derlutgate"
default college_name = "Tetra College"

# Characters
define me = Character("[my_name]", color="#008080")
define cat = Character("[cat_name]", color="#008080")
define fish = Character("[fish_name]", color="#008080")

label start:

    call opening_scene

    "- END of DEMO -"

    "Stay tuned!"

    return