label opening_scene:

    "You are [my_name], a 19 year old college student, and work part time at a cafe."
    "You feel as if you lack excitement in your life, but the future is unknown..."
    "Throw yourself into [town_name] and date some girls!"

    scene bg cafe
    with fade

    "Ugh... another day... another shift..."
    "I've been working here at Uncle Mugen's as a part-time barista for about 2 weeks."
    "I check the time. It's 2 pm."
    "... 4 hours until the end of my shift. This is torture."
    "A girl with [girl1_description] comes up to the counter and considers her choices."

    show g1

    g1 "Hi, I'd like a large latte, please."
    "I recognise her from college, but she is from another class and I don't know her name."
    "She digs into her handbag, searching for her purse, and then stares at me for a moment."
    g1 "... Have I seen you before?"
    me "Uh... I think we go to the same college, [college_name]."
    g1 "Oh? You do? That's wonderful! I'm [girl1_name]."
    "I smile as I begin preparing her drink."
    me "My name is [my_name]. Nice to meet you. That will be $4, please."

    hide g1

    # scene bg cafe evening

    "Alright. It's finally 6 pm!"
    "My shift is over."
    "I make my way out of the cafe and head towards the bus stop."

    # scene bg bus stop evening

    "It's rush hour, so there are a lot of people around."
    "I wait around for a moment or two before I see the bus I need pulling in."
    "As I board the bus, I hear a girl shout from behind me."
    g2 "Waaaaait!"

    show g2 shocked
    with hpunch

    "I'm suddenly shoved forward. Did she run into me?"
    g2 "I'm sorry!"
    me "No problem."

    hide g2

    "The rest of the journey home is rather uneventful."

    # scene bg home

    "I can't cook at all, so instant ramen it is."
    "Yum."
    "I've finished my studies for the most part, so I spend the rest of the evening playing video games."
    
    
    
