

python:
    girl1 = "Ana"
    town = "Derlutgate"
    college = "Tetra College"

    my_name = renpy.input("What is your name?")
    my_name = my_name.strip()

    if not my_name:
         my_name = "Kevin"

define m = Character("[my_name]", color="#008080")
define c = Character('Cat Lady', color="#FF69B4")

label start:
    ## INTRO
    
    "You are [my_name], a 19 year old college student, and work part time at a cafe."
    "You feel as if you lack excitement in your life, but the future is unknown..."
    "Throw yourself into the city of [town] and date some girls!"
    

    ## SCENE 

    "Ugh... another day... another shift..."
    "I've been working here at Uncle Mugen's as a part time barrista for about 2 weeks."
    "I look up to read the clock: 2pm."
    "... 4 hours until the end of shift. This is torture."
    "A girl with [girl1_desc] comes up to the counter and ponders on her choices."
    c "Hi, I'd like latte large please."
    "I recognise her from college, but she is from another class and I don't know her name."
    "She digs into her handbag searching for her purse, and stares at me for a moment..."
    c "Huh... have I seen you before?..."
    m "Uh... I think we go to the same college. [college]."
    c "Oh? You do? That's wonderful! I'm [girl1]."
    "I give a smile and begin making her drink."
    c "My name is [my_name]. Nice to meet you. That will be $4 please."
    
    
    
