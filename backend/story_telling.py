def set_story(story):
    # --------------- ADDING CHARACTERS ---------------
    story.add_character(name='adventurer', description='drunk')
    story.add_character(name='alien', description='academic')
    story.add_character(name='wizard', description='foreign cultures')
    story.add_character(name='detective', description='break free')

    # --------------- DEFINING CONTENT STRUCTURE ---------------
    rows = story.story_size[0]
    columns = story.story_size[1]
    for row in range(rows):
        for i in range(1, columns - 1, 3):
            story.get_page_raw(row, i).set_page_type('challenge')
            story.get_page_raw(row, i + 1).set_page_type('outcome')

    # --------------- ADDING BLANKS ---------------

    # --------------- ADDING CONTENT ---------------


def set_example_story(story):

    # --------------- ADDING CHARACTERS ---------------
    story.add_character(name='adventurer', description='drunk')
    story.add_character(name='alien', description='academic')
    story.add_character(name='wizard', description='foreign cultures')
    story.add_character(name='detective', description='break free')

    # --------------- DEFINING CONTENT STRUCTURE ---------------
    rows = story.story_size[0]
    columns = story.story_size[1]
    for row in range(rows):
        for i in range(1, columns - 1, 3):
            story.get_page_raw(row, i).set_page_type('challenge')
            story.get_page_raw(row, i + 1).set_page_type('outcome')

    # --------------- ADDING BLANKS ---------------
    # story.add_blank('B00', ['apples', 'bananas', 'tomatoes'])
    # story.add_blank_random('B01', 'noun')
    # story.add_blank_random('B02', 'verb')
    story.add_blank('treasure') # in text refer to the keyword as ~treasure~
    story.add_blank('map')  # ~map~
    story.add_blank('tech')  # ~tech~
    story.add_blank('magic')  # ~magic~
    story.add_blank('weapon')  # ~weapon~
    story.add_blank('B00', word_type='strange_words', changes_every_time=True) # ~B00~

    # --------------- ADDING CONTENT ---------------

    # ----- ALIEN: -----
    story.get_page(character_name='alien', chapter=0, page='intro').add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list. Testing if ~treasure~ works.',
             'Also testing if repetions of ~treasure~ work.'
             # 'And this word: ~B01~ has been randomly selected from the internet',
             ]
    )

    # BE FUCKING CAREFUL: THE ORDER IN WHICH YOU STORE THE OUTCOME MATTERS!
    # FIRST GOOD OUTCOME, THEN BAD OUTCOME
    story.get_page(character_name='alien', chapter=0, page='outro').add_page_variation(
        txt=['Good outcome']
    )
    story.get_page(character_name='alien', chapter=0, page='outro').add_page_variation(
        txt=['Bad outcome']
    )
    story.get_page(character_name='alien', chapter=0, page='outro').set_last_page(True)

    # ----- ADVENTURER: -----
    story.get_page(character_name='adventurer', chapter=0, page='intro').add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list'
             # 'And this word: ~B01~ has been randomly selected from the internet',
             ]
    )

    story.get_page(character_name='adventurer', chapter=0, page='outro').add_page_variation(
        txt=['Good outcome']
    )
    story.get_page(character_name='adventurer', chapter=0, page='outro').add_page_variation(
        txt=['Bad outcome']
    )
    story.get_page(character_name='adventurer', chapter=0, page='outro').set_last_page(True)

    # ----- Detective : -----
    story.get_page(character_name='detective', chapter=0, page='intro').add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list'
             # 'And this word: ~B01~ has been randomly selected from the internet',
             ]
    )

    story.get_page(character_name='detective', chapter=0, page='outro').add_page_variation(
        txt=['Good outcome']
    )
    story.get_page(character_name='detective', chapter=0, page='outro').add_page_variation(
        txt=['Bad outcome']
    )
    story.get_page(character_name='detective', chapter=0, page='outro').set_last_page(True)

    # ----- Wizard : -----
    story.get_page(character_name='wizard', chapter=0, page='intro').add_page_variation(
        txt=['You are a wizard and you are proud of that!',
        'After having studied ancient magic for years you are ready to go out into the world and finally use your powers for good.',
        'You are also passionate about exploring foreign cultures and aiding the people you meet on the way.',
        'This is the creed you live by and not a single day passes without you contemplating the wonders of the world.',
        'But one day, you jolt awake violently as a wave of energy crackles through your limbs.',
        'You are highly attuned to your environment and can sense auras and high concentrations of magic potential…',
        'but you have never felt something like this before. It felt like the utterance of a vast, unfathomably powerful incantation and the mere thought of this makes you shiver.',
        'Almost immediately, you also feel your ~magic~… pulsing. Its red glow surprises you.'
        'The ~magic~ was a family heirloom, an important and mighty artefact, passed down generation-by-generation to be guarded by powerful wizards like yourself or your ancestors.',
        'However, you don’t believe that it has ever behaved this way before. You take a deep breath. Something is very wrong and it’s up to you to ensure that no innocent people will be hurt.',
        'Without furter ado, you put your belongings into a duffle bag and let your senses lead you to the origin of this burst of energy.']
    )

    story.get_page(character_name='wizard', chapter=1, page='intro').add_page_variation(
        txt=['When you finally arrive in Munich you are overwhelmed by the feeling that something terrible is about to happen here.',
        'It sets you on edge and you fidget with your ~magic~. A novice would find it difficult to navigate such an environment and succumb to this sensory overload but you’re an expert.',
        'So you close your eyes and focus on the gentle tug of the ~magic~, wandering through the streets of this foreign place and doing your best to ignore this vibrant city.',
        'The pulsing increases steadily so you ought to be on the right track unless… unless something is interfering. You halt and look around.',
        'There is one person, sitting all by himself on a park bench in deep contemplation. His brows are furrowed and his trenchcoat is torn.',
        'In an instant, you feel that something terrible has happened to this man and you know exactly whose overpowering grief is interfering with your readings.',
        'Naturally, you approach him. Maybe you can help, after all. The man is new in town and he neither remembers his past nor does he know who he is.',
        'A poor, unfortunate soul tormented by fragmented memories. He says that he’s here to find clues, to piece together what happened.',
        'So do I, you tell him, and you have always enjoyed company on your adventures. He, a former detective apparently (that much he remembers), does not want to work with you initially.'
        'But after a demonstration of your skill set he nods in approval and you begin your exploration.']
    )

    story.get_page(character_name='wizard', chapter=1, page='outro').add_page_variation(
        txt=['He finds an envelope that you wouldn’t have thought twice about. It is tucked between the branches of a tree and curiously, it is addressed to him.',
             'Upon opening it, two slivers of paper fall out: the first one is yellow and old, very old. Strange, wiggly symbolds adorn the backside of the paper.',
             'The cursive lettering reveals a prophecy, that the stagewise combination of sacred relicts will unleash an unfathomable curse upon the people in this town.',
             'Surely, the burst of energy was the first sign of what is to come!',
             'You do not know what is written on the second piece of paper but it must be equally concerning, as the detective pales at the sight of the letters and stuffs it quickly into his pocket.',
             'Time is of the essence now and you try to convince your companion to help you prevent the prophecy but he shakes his head. He has to attend to personal matters. So your ways part.']
    )

    story.get_page(character_name='wizard', chapter=1, page='outro').add_page_variation(
        txt=['He finds an envelope that you wouldn’t have thought twice about. It is tucked between the branches of a tree and curiously, it is addressed to him.',
            'Upon opening it, two slivers of paper fall out: the first one is a letter. Strange, wiggly symbolds adorn the backside of the paper.',
            'On the front side, it’s written in neat cursive that the town has been cursed and that its inhabitants will fall sick to a mysterious illness within the days.',
            'You are shaken to your core. You were right with your suspicion…. the energy wave you felt must have been caused by the curse.',
            'You do not know what is written on the second piece of paper but it must be equally concerning, as the detective pales at the sight of the letters and stuffs it quickly into his pocket.',
            'Time is of the essence now and you try to convince your companion to help you find a cure but he shakes his head. He has to attend to personal matters. So your ways part.']
    )

    story.get_page(character_name='wizard', chapter=2, page='intro').add_page_variation(
        txt=['There is no need to follow the wiles of the ~magic~ anymore now. What you need to do is consult the council of wizards of which there is one in every city.',
            'Surely, they will know what to do in this dire situation and right now you need all the help you can get. But finding their location proves to be more difficult than anticipated.',
            'You wander the streets once more but for some reason it seems to be impossible to find them! Suddenly, you remember that some cities are hostile towards wizards.',
            'In those cases, the council would adopt an inconspicous name and mask itself as a part of local government in order to go unrecognized. Perhaps Munich is more wizard-phobic than you thought?',
            'You decide to visit the municipal administration authority for more information. It is a terrible experience but odds are that the most obscure department will be responsible for wizardry.',
            'So, you receive a waiting number, settle down in the waiting room, and wait. And wait. And wait. It’s very boring and feels like an immense waste of time.',
            'The person to your left seems equally bored except….something is very off with him. Looking at him for an extended period of time causes your eyes to water.',
            'His skin is stretched a little bit too tight across his bones and his clothes hang off his frame in an odd way.',
            'Suddenly, he asks you if you require assistance. He has a strange lilting accent when he speaks and doesn’t get the intonation right. Perhaps he too is a foreigner from a far-away country?',
            'Admittedly, you feel a bit sheepish at being caught staring at him but you quickly decide to use this opportunity to start a conversation.',
            'It turns out that, indeed, he is from a country you have never heard of and came to Munich for research purposes.',
            'When prodded about his research topic he becomes very flustered and releases a quiet trilling sound like a cricket. He says it’s a behavioral study on...the humans.',
            'You tell him that this is a very alien way to phrase things and his eyes widen considerably. You decide not to ask any more questions.',
            'Nonetheless, you offer him your help with his study! Perhaps you could tell him something about your own experiences or conduct short interviews with other people while you’re waiting?',
            'He seems a bit taken-aback but quite relieved. He accepts your offer and in return, he agrees to help you find out more about obsure departments by asking the civil servants and people around him.',
            'Thus, both of you begin striking up conversations with other people.']
    )

    story.get_page(character_name='wizard', chapter=2, page='outro').add_page_variation(
        txt=['There is an old man sitting in the far corner of the room. His hair is stringy and his clothes are covered in grime.',
            'But as you approach him, he smiles and tells you that he knows what you are looking for. All of your pent-up stress comes to a head and you break down in relief!',
            'Finally, you have found another wizard in Munich who might be able to help you! You quickly tell him everything you know about the current situation and he strokes his beard in a wise, wizardly manner.',
            'Then he tells you that the problem is your ~magic~. You raise your eyebrows involuntarily. He explains that by bringing it to the city, it merely accelerated the ongoing events.',
            'If you want to save the city, he says, you need to remove it and destroy it. You clutch your ~magic~ defensively – after all these years you have grown quite attached to it.',
            'Could this really be true? After all, you followed the tug of the ~magic~. You never considered that it was an evil artefact and that this may have been the reason why you were tasked with guarding it.',
            'The wizard looks at you with kind eyes and says that he will be leaving the city tomorrow. He knows a blacksmith who is capable of destroying magic items.',
            'All you have to do is give him the ~magic~. What else are you supposed to do? So with a heavy heart, you do as he says.']
    )

    story.get_page(character_name='wizard', chapter=2, page='outro').add_page_variation(
        txt=['There is an old man sitting in the far corner of the room. His hair is stringy and his clothes are covered in grime. But as you approach him, he smiles and tells you that he knows what you are looking for.',
            'All of your pent-up stress comes to a head and you break down in relief! Finally, you have found another wizard in Munich who might be able to help you!',
            'You quickly tell him everything you know about the current situation and he strokes his beard in a wise, wizardly manner. Then he tells you that the city is doomed. All hope is already lost.',
            'Your stomach sinks rapidly – is there truly nothing you can do? He shakes his head. The council has been observing the ongoing events and already tried to prevent the situation from getting worse… to no avail.',
            'Most of the wizards in this city have already evacuated and he was one of the last ones left. It was a lucky coincidence that you found him. He urges you to leave as soon as possible as well.',
            'Tears begin welling up in your eyes. No...this can’t be true...what is going to happen to all the poor people here? Will they just die? Could this have been prevented if you had arrived earlier?',
            'You start weeping and the wizard hugs you in an attempt to console you. He smells terrible. You hear a rustling sound and feel his hand wander… what is he doing?',
            'Hey, where is the ~magic~? But before you can say anything you hear a loud bang.']
    )

    story.get_page(character_name='wizard', chapter=3, page='intro').add_page_variation(
        txt=['You hear a violent yell and turn just in time to see your new friend, the mysterious researcher, being dragged away by a couple of men in suits.',
            'Immediately you rise to your feet, magic energy crackling in your fingertips. Without wasting another thought on the old wizard you just talked to, you run outside in an attempt to track them down but they are already gone.',
            'Cursing under your breath you close your eyes and focus on the despair and fear that the alien scientist emits. Then you begin your pursuit.',
            'But unfortunately, the trail gets weaker as you go on. Your friend must have passed out, because you can’t feel his emotional aura anymore and are left somewhat disoriented.',
            'You have reached the outskirts of the city and can’t find any other people. It makes your nervous. Suddenly, a flash of relief. Hidden behind a thicket there is an entrance to a cave and you can sense that somebody is in there.',
            'Could it be your friend? You decide to trust your gut-feeling and squeeze through the tiny opening.',
            'The room you enter seems to be much bigger on the inside. You find stone walls with hieroglyphs pain-stakingly carved into them, ancient patterns that are indeciphrable but… seem vaguely familiar.',
            'A voice calls out to you. Across the room you find a young woman who is bandaging a particularly nasty bruise on her arm. She gives you the once-over and asks you what the hell you’re doing here.',
            'So you explain yourself, tell her that you are a wizard trying to do good. She raises an eyebrow. There are no wizards in Munich, she says off-handedly, a local told her that.',
            'This confuses you and you want to reply but she seems so...sure of it. It sends you reeling. There are no wizards in Munich. That means there is no council. There probably never was.',
            'The absence of your ~magic~ strikes you all of a sudden and you howl in anger. You have been tricked, damn it! How could you be so naive and stupid? And just who the hell was that old man you met?',
            'You explain the other woman what happened to you and she gives you a wry smirk. She too has lost something very important, she says. She’s an adventurer and somewhere along the journey the treasure she found had been stolen.',
            'But maybe it was for the better, she says, because when she found it she believes she got cursed. It even released some kind of shockwave, when she found it. And at the very least, she’s had bad luck ever since.',
            'Both of you sigh. It has been a long day and you’ve dealt with enough curses for a life time. No sign of your friend either. An uncomfortable silence has settled in the room so you take another look at the strange symbols on the walls.',
            'Suddenly, you remember the wiggly symbols – they were marked on the paper you found at the very beginning of your journey! These hieroglyphs must be linked to your current predicament then.',
            'You quickly tell the adventurer about it and suddenly she’s very interested, thinking it might be related to her curse. Unfortunately, neither of you know what these symbols mean.',
            'But then the adventurer’s face lights up. She pulls out a thin, alien-looking device from one of her pockets and tells you that this tool can do a bunch of things.',
            'That it wouldn’t surprise her, if it had a built-in translator as well. You ask her what it is and where she got it from, but she just shrugs her shoulders and tells you that a friend of hers lent it to her.',
            'Indeed, you quickly figure out the translation function and the wiggly lines on the wall turn into English words. Together you start learning about the history of this place.']
    )

    story.get_page(character_name='wizard', chapter=3, page='outro').add_page_variation(
        txt=[
            'You find out that there is no curse, neither on the city, nor on the adventurer. There is no illness that might befall the people.',
            'Instead, you learn about an ancient ritual meant to summon an Eldritch God and awaken him from his century-long slumber.',
            'Special artefacts would need to be combined correctly at the right time in the right place and what would follow is nothing short of the end of the world.',
            'You find out that the ~magic~ is one of these artefacts. What is left You also find out that the treasure the adventurer lost is one of those key items as well and it makes your stomach turn.',
            'Someone is trying to perform the ritual… and that person needs to be stopped.',
            'You still have an eye on the translator. Its technology seems to be highly advanced and you wonder who the original owner might have been. You have a gut feeling but...it would be so unlikely.',
            'However, the more you concentrate on it, the more you receive…some kind of signal. A low energetic pulse emitted by it. It’s… pulsing.',
            'Just like your ~magic~ did. If it lead you to the source of the energy burst… and that was caused by the adventurer’s treasure…',
            'Could it be that if you followed its signal...it will would lead you to the other artefacts? You quickly grab the device and follow the path it shows you.',
            'The adventurer is taken aback but she quickly follows and together you run, as it turns out, to a local research facility.',
            'Both of you manage to sneak in through an open window and then you finally find the right room…'
        ]
    )

    story.get_page(character_name='wizard', chapter=3, page='outro').add_page_variation(
        txt=['You find out that there is no curse, neither on the city, nor on the adventurer. There is no illness that might befall the people.',
        'Instead, you learn about an ancient ritual meant to summon an Eldritch God and awaken him from his century-long slumber.',
        'Special artefacts would need to be combined correctly at the right time in the right place and what would follow is nothing short of the end of the world.',
        'You find out that the ~magic~ is one of these artefacts. What is left You also find out that the treasure the adventurer lost is one of those key items as well and it makes your stomach turn.',
        'Someone is trying to perform the ritual… and that person needs to be stopped.',
        'Suddenly the walls start shaking and rumbling. Both of you are panicking, as suddenly debris is falling from the ceiling. Boulders are raining down and you duck and cover.',
        'After a minute it stops and you open your eyes to almost complete darkness: the entrance is now blocked with rubble. There is no way you’ll be able to get out the way you came in.',
        'But what’s that? A glimmer of light in the far corner? Together with the adventurer you take a closer look and find what appears to be the entrance to a secret tunnel.',
        'It is barely illuminated and you have no idea where it leads to. You look at the adventurer and she shrugs her shoulders.',
        'Alas, you don’t have any choice but to descend and hope for the best. It takes a long time but when you finally exit the tunnel you are…in a lab?']
    )
    assert len(story.get_page(character_name='wizard', chapter=3, page='outro').page_variations) == 2
    story.get_page(character_name='wizard', chapter=3, page='outro').set_last_page(True)

    story.get_page(character_name='wizard', chapter=4, page='intro').add_page_variation(
        txt=['fuck off it is not done yet']
    )

    story.get_page(character_name='wizard', chapter=4, page='outro').add_page_variation(
        txt=['fuck off it is not done yet']
    )

    story.get_page(character_name='wizard', chapter=4, page='intro').add_page_variation(
        txt=['fuck off it is not done yet']
    )

    story.get_page(character_name='wizard', chapter=4, page='outro').set_last_page(True)
