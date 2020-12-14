init python:

    # Player Input
    # my_name = renpy.input("What is your name?")
    # study_choice = renpy.input("What are you studying?")
    # my_name = my_name.strip()
    # study_choice = study_choice.strip()
    # if not my_name:
    #     my_name = "Kevin"
    # if not study_choice:
    #     study_choice = "computer science"

    # Default
    my_name = "Kevin"
    study_choice = "computer science"

    # Girls
    girl1_name = "Ana"
    girl1_description = "pink hair and unusually large breasts"
    girl1_study_choice = "political science"

    girl2_name = "Beatrice"
    
    # Locations
    town_name = "Derlutgate"
    college_name = "Tetra College"

# Characters
define me = Character("[my_name]", color="#008080")
define g1 = Character("[girl1_name]", color="#008080")
define g2 = Character("[girl2_name]", color="#008080")

label start:

    call opening_scene

    return