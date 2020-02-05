from utils import *
import pycorpora


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
    story.add_blank_v2('treasure', adventurer_treasure)
    story.add_blank_v2('map', adventurer_map)
    story.add_blank_v2('tech', sci_fi_thing)
    story.add_blank_v2('magic', magic_thing)
    story.add_blank_v2('weapon', detective_weapon)
    story.add_blank_v2('B00', pycorpora.words.strange_words['words'])

    # --------------- ADDING CONTENT ---------------

    # ----- ALIEN: -----
    story.get_page(character_name='alien', chapter=0, page='intro').add_page_variation(
        txt=['Welcome to what your people call Planeta stultorum! Here it’s just called Earth. ',
             'I know you’re not thrilled to be here, but trust me your 157 day trip from Mars will be worth it. ',
             'There is so much to learn and discover here. But also there are so many distractions. ',
             'So you must really stay focused and be careful with hiding your identity. Try to blend in and act like humans. '
             'So basically just eat Sauerkraut and talk about how almond milk changed your life. '
             'And if anyone suggests you add pineapples on your pizza, just say no. It’s a trap. '
             'Paramount, don’t let anything stand in your way. You were chosen for this mission for a reason, and you can’t let your people down. ',
             'Now let’s start this journey and get you the experience you need to collect from the humans.'
             ]
    )

    # BE FUCKING CAREFUL: THE ORDER IN WHICH YOU STORE THE OUTCOME MATTERS!
    # FIRST GOOD OUTCOME, THEN BAD OUTCOME
    story.get_page(character_name='alien', chapter=1, page='intro').add_page_variation(
        txt=['Such a strange place isn’t it? Yet so appealing. Let’s take a look around, discover the area, draw a mental map of the city, observe its people. ',
             'Do you see that disc shaped thing covered in white mush everyone is eating? That’s a pizza. Now would you look at that guy over there; about to eat pizza with pineapples. ',
             'Quick, stop him! Ah, humans. Not the brightest creatures. You’d invade this place in a heartbeat.The more you discover about the human daftness the easier your alien attack on earth would be.',
             'So keep this human near you and study his behaviour. ',
             'Now would you listen to him go on and on about some ~treasure~. Is this place really 4 billion years old? ',
             'Well, just go with it, lend him your ~tech~ even. This is the sacrifice you have to make for the better of your kind.'
             ]
    )
    story.get_page(character_name='alien', chapter=1, page='outro').add_page_variation(
        txt=['Oh would you look at that. What a rush! You actually took part in a ~treasure~ hunt and it wasn’t bad at all. ',
             'You actually helped this human find the ~treasure~, and you also had fun, didn’t you. ',
             'I say you try to relive this experience with other humans. Ones with a higher IQ maybe? ',
             'That would make the research way more interesting. ',
             'Now run away from this human before you get trapped in his nonsense.'
             ]
    )
    story.get_page(character_name='alien', chapter=1, page='outro').add_page_variation(
        txt=['Oh look, a sealed scroll. Should we take the risk and open it? What’s the worst that could happen anyway, let’s just read what’s inside. ',
             'It reads: Breaking this seal, breaks your destiny. Accept the deal, or follow the mystery. ',
             'Ah, humans and their drama.. ',
             'Wait why are you so frightened? Aren’t you a bit too scientific to be superstitious? ',
             'Wow, nevermind, you’re right. This ~treasure~ just released a massive energy wave. ',
             'You could have been contaminated by it, and we don’t know what the side effects are. ',
             'You need to go back to Mars as soon as possible. You can’t risk staying here any longer. ',
             'Leave this human behind and go seek help elsewhere!'
             ]
    )
    story.get_page(character_name='alien', chapter=2, page='intro').add_page_variation(
        txt=['Okay now, all you have to do is find the interplanetary base or at least some human intelligence center. It shouldn’t be that hard, considering the fair amount of technological advances these species have achieved. ',
             'Over the time span of 4 billions years. ',
             'Well if you look over there you can see a big building that says “Foreigners Registration Office”. Well technically you are a foreigner, so I say we go in and check out the place. ',
             'Would you look at that. It’s amazing how many different faces and how many different voices there are. Humans must love how diverse their planet is. ',
             'Now let’s scan this place and try to find the smartest looking person that could help you. ',
             'Hmm, if you look over there you would see someone with a really big hat. Must be because they have a really big head. You know what that means right? They’re a genius! The bigger their head is, the more knowledge it contains. ',
             'Go on now, just say hi and tell her about the little adventure you had. See? Not that hard. Humans aren’t complicated. And this one seems really interested in your story. ',
             'Although she doesn’t believe in aliens, she does agree that something strange is going on in this city. She even emphasizes that the city could be doomed, if no one saves it. ',
             'She is willing to get you in contact with someone who can help you, in exchange for your own help in finding the master wizard. ',
             'Well, you did have a hand in that energy wave outbreak. So let’s get onboard and help this new friend you just made.']
    )

    story.get_page(character_name='alien', chapter=2, page='outro').add_page_variation(
        txt=['Okay, no need to panic. But it does seem to me like everyone is staring at you. No worries though, worst case scenario it’s just because they don’t like your outfit. '
             'But don’t take it personally, that’s just how humans react to what’s different. ',
             'A nice lady just approached you and invited you into her office for a chat. If you decline you’d come off suspicious. So just go with it, and if things escalate just use your ~tech~ . ' 
             'Oh no, you seem to have forgotten it with the adventurer. Classic. ',
             'Oh look at her with her manners, offering you a cup of water. Just drink it, humans drink water. Tastes horrible, right? That’s actually the main reason they want to invade your planet. ',
             'Come on now, she’s talking to you, answer her. Why did you suddenly get so dizzy? Are you okay? You seem to be losing your consciousness. ',
             'Oh, so that explains the weird taste in the water. Another classic. Mea culpa, should’ve warned you about it.'
              ]
    )
    story.get_page(character_name='alien', chapter=2, page='outro').add_page_variation(
        txt=['Is it just me or is everyone intensively staring at you? Are they on to you or is it just Germans playing with the boundaries of normal social conduct? ',
             'Oh no, everyone is pointing their finger at you. ' ,
             'A big black van stops near you and three big built humans step out and approach you. Oh boy, this never ends well. Calm down now, they could be here for the wizard. ',
             'It’s okay let them take him. You guys weren’t that close anyways, and long distance friendships aren’t even a thing. ',
             'Hmm.. I spoke too soon. The three humans grab you and try to shove you inside the van. The poor wizard is trying so hard to help you escape, but he’s left behind. ',
             'Shame on you, just a few seconds later you were willing to let him go down. ',
             'Let’s save the moral conflict for later, now just grab your ~tech~ and free yourself. ',
             'You can’t seem to find it, you must have left it with that adventurer. Ah humans, you spare their lives and they can’t even return something they borrowed. ',
             'Look at you now, on your way to a containment facility where you will be the subject of study. You should have let him eat that pineapple pizza.'
              ]
    )

    story.get_page(character_name='alien', chapter=3, page='intro').add_page_variation(
        txt=['Rise and shine you Alien. Okay maybe just rise. There is no shining inside the cage you’re in. Although there is a well dressed human waiting for you in this room. ', 
             'He is too chic to be a scientist. Just listen to what he has to stay, and try to gain his trust. ',
             'Oh for the love of science! He’s been going on and on about how he’s a detective but he can’t figure out that you’re not the bad guy. ',
             'I give up, just start begging until he frees you. Well that was easier than I expected. ',
             'Dobby is free! Wait nevermind, forgot you’re an alien, you won’t get that reference. ',
             'So now how do you get out of this maze. I think you should follow the detective’s instructions. He seems to know what he’s doing. ',
             'I take that back. You seem to have taken the wrong exit and ended up at some secret laboratory. ',
             'Humans again. They can’t help you with something without screwing up something else.'
              ]
    )
    story.get_page(character_name='alien', chapter=3, page='outro').add_page_variation(
        txt=['What kind of mastermind orchestrated this whole charade? This place is like nothing you’ve ever seen before. ',
             'Hold on a second, is that the ~treasure~ you found with the adventurer? Pick it up quickly! What’s this thing beneath it? ' 
             'It’s probably some human thing, ask the detective. He says it’s just some piece of jewelry. Hand it over and let him examine it further. ',
             'Wait, why did he suddenly get so ecstatic? Did he really just hug you? I am no expert but this does not seem like such usual human behaviour. ',
             'Screaming out “ I remember! I figured it all out!”. He seems to be having a Eureka moment. ',
             'I don’t know what’s going on either, but it seems to be a good thing. You can take some of the credit.'
              ]
    )

    story.get_page(character_name='alien', chapter=3, page='outro').add_page_variation(
        txt=['What kind of mastermind orchestrated this whole charade? This place is like nothing you’ve ever seen before. ',
             'The detective just found the ~treasure~ you have already helped the adventurer find. Are the dots getting connected somehow? ',
             'Hold on, he has another unfamiliar object in his hand, magic of some sort. He’s not sure but he says it looks like some magic jewelry.'
             'Why is his face getting so serious suddenly? It’s like he’s just seen an alien. ',
             'Oh no, this is no time for jokes. The detective is really overwhelmed by what he just saw. '
             'His face is suddenly so yellow, he is excessively sweating all over, he has this hollow look that does not see you because it’s seeing something else. ',
             ' “I remember.. I remember it all.. It’s all coming back..” He stutters incoherently. ',
             'Remember what? What’s coming back? What in the Milky Way is happening here. '
              ]
    )
        story.get_page(character_name='alien', chapter=4, page='intro').add_page_variation(
        txt=['The door slams wide open and you all are overwhelmed by someone. Someone you can’t see, but you can feel.',
        ' You can sense him with your entity, moving through your body and into your soul.',
        'Messing with your head, reaching your heart and pulling it strings. The feeling is so intense you wish he would just rip it out already. '.
        'Yes it’s him. He is real and he is here. The greatest trick he ever pulled was convincing the world he didn’t exist.',
       'You must be wondering why he went through all this trouble to gather you all here. What are the chances that four beings,',
        'with such contrasting backgrounds and traits, ending up here. At this exact place, this exact time.'

        ]
    )

    story.get_page(character_name='alien', chapter=4, page='outro').add_page_variation(
        txt=['How did he plan all this? Let me help you my dears by telling you that he didn’t.',

'You by your own choice and your own will, took every step that led you to this place.',

'And he, like always, is ecstatic that the entire universe conspired to help  him find you.', 

'He is not your enemy. The only real enemy to have ever existed, is an internal one.',

'You can’t give in to this. You can’t get sucked in by the darkness.',
 
'This is exactly what he wants, don’t hand it to him. Don’t pour salt to the open wound. Fight his evil with good, and his darkness with light.',

'Can you see it now? Is it getting clearer? Can you see how each and every one of you, despite your differences, helped one another do and be better?',

'You came to this city all alone, you crossed paths with a hundred other people. But you chose these three standing in front of you.',

'You didn’t fall into this maze. You  walked into it, with your eyes wide open, choosing to take every step along the way.',
 'Maybe there is no fate or destiny, but I believe you are only fated to do the things that you’d choose anyway.'
'And you’d choose each other; in a hundred lifetimes, in a hundred worlds, in any version of reality, you’d find one another and you’d choose one another.',

'You all, remember where you were when this journey first started, and look at yourselves now.',

'The more you look, the clearer you see, the faster the peace and serenity take over.',

'All you touch and all you see is all your lives would ever be. And now, your lives would never be the same, after crossing paths with these exceptional people.'

'So here’s the best part, distilled for you; you saved yourselves, and in the process saved the world from doom.'

'Congrats my dears. It was a blast accompanying you on this journey.
']
    )

    story.get_page(character_name='alien', chapter=4, page='outro').add_page_variation(
        txt=['How did he plan all this? Let me help you my dears by telling you that he didn’t.',
'You by your own choice and your own will, took every step that led you to this place.',
'And he, like always, is ecstatic that the entire universe conspired to help  him find you.',
'He is not your enemy. The only real enemy to have ever existed, is an internal one.',
'You the adventurer, are your own enemy. Fleeing from place to place all your life, trying to fill the void inside.',
 'But in reality you are fleeing yourself. Fleeing the dissatisfaction, seeking glorification and validation, as if your values increases by the count of the places you explore.',
'You the detective, are your own enemy. Spending your entire time solving people’s issues so you wouldn’t have to face your own.',
 'Helping people is merely an overcorrection for the fact that you were responsible for your own brother’s death.',
'You the Wizard, are your own enemy. You spent your entire life isolated,  hating humans before they hate you.',
 'Convincing yourself that you are better than them, more powerful, and that your magic is something they envy you for.',
  'When really you are the one envying them for a life so simple and sweet. All you ever wanted was to flee and live a normal life.',
   'To live like a human.',
'You the Alien, are your own enemy. You must’ve really hated your own kind for you to travel all the way from Mars.',
 'You were always the underdog of aliens, they all thought you weren’t good enough and you knew it.',
'You want us to believe you got on a spaceship all alone for 157 just for research? Who are you kidding ? You were never good enough for your people, they underestimated you.',
 'The only time they ever looked up to you was because you let them down. And now you come here to this planet, thinking you’re superior, plotting to take over the world.',
'You all, look at yourselves now. Look at where the devil in you got you.',
'The more you look, the deeper you see, the faster the darkness takes over.',
'All you touch and all you see is all your lives would ever be.',
'But now all there is, is darkness. You and everything surrounding you vanish into nothingness.',
'So long my friends, i am pained to have lost this way.']
    story.get_page(character_name='alien', chapter=4, page='outro').set_last_page(True)

    # ----- ADVENTURER: -----
    story.get_page(character_name='adventurer', chapter=0, page='intro').add_page_variation(
        txt=['Ahoy Adventurer! Finally arrived at the promising land. How are you feeling after your 3 weeks cruise with the pirates? I hope you’re not too tired. ',
             'You need to be in your best game if you wanna find the hidden ~treasure~.'
             ]
    )

    story.get_page(character_name='adventurer', chapter=1, page='intro').add_page_variation(
        txt = [
                'A beautiful city, isn’t it? Let’s take a look around, have a long walk, admire the city, embrace its vibe. ',
                'So many food stands everywhere, and the food smells phenomenal. Getting hungry huh? May I suggest pizza? Oh god no, not the pineapple pizza! ',
                'C’mon that’s common sense 101. ',
                'You’re lucky this guy just stopped you. ',
                'Perfect timing I must say. It’s almost as if he was already here, watching you.. ',
                'But let’s not jump to conclusions, he is obviously new here and just wants to make friends. ',
                'Although, he is a weird looking fella.. And what’s that beeping device he’s trying so hard to hide? ',
                'Just look closely and focus. C’mon you know this one. It’s ~tech~ ! ',
                'What kind of lunatic walks around with a ~tech~ ? ',
                'On second thought, this is exactly what you need to find the ~treasure~ . ',
                'Let’s get him on board, a ~treasure~ hunt is more fun in pairs anyway!'
            ]
    )

    story.get_page(character_name='adventurer', chapter=1, page='outro').add_page_variation(
        txt=['Magnificent, you found it very easily. Too easily actually, now that we think about it .. ',
             'Did the secret messenger send you all the way to Munich just to find this ~treasure~ in one hour? ',
             'This can’t be it. It must be just a misdirection. The real treasure must be hidden somewhere else. ',
             'Wait what’s happening here? Are you sensing this magic wave? Were you just cursed? ',
             'Well now we know for sure there’s more to this mystery. ',
             'Let’s go, take the device and leave alone, this whole situation just got too risky.'
            ]
    )

    story.get_page(character_name='adventurer', chapter=1, page='outro').add_page_variation(
        txt=['Oh look, a sealed scroll. Should we take the risk and open it? What’s the worst that could happen anyway, let’s just read what’s inside. ',
             ' “Breaking this seal, breaks your destiny. Accept the deal, or follow the mystery” ',
             'Oh oh, looks like you’ve been cursed. You can’t quit now. ',
             'The destiny of this city lies in your hands, you must go on with this quest and lift the curse. ',
             'I say you leave alone with the ~tech~ and seek the help of the locals instead.'
             ]
    )

    story.get_page(character_name='adventurer', chapter=2, page='intro').add_page_variation(
        txt=['A bar, the perfect place to get intel from drunken locals. Take a look around and try to find a resourceful target. ',
             'Look over there, someone sitting by themselves sipping on their drink, eavesdropping  on conversations. Nothing better than a nosy local. Let’s approach them and see. ',
             'He’s a bit too secretive for someone who spies on others. Maybe if you mention the tip that sent you here he’ll be more interested in your story. ',
             'He recognizes the initials! What are the chances! ',
             'You two better start asking around to get to the end of this. But you need to step up your game. Everyone either takes you for lunatics or just avoids the subject. I wonder why..'
             ]
    )   

    story.get_page(character_name='adventurer', chapter=2, page='outro').add_page_variation(
        txt=['A wise man just approached you. He heard you and the detective and says you’re looking in the wrong place. He seems to know something about the matter and advises you to go east. ',
             'Why is he being so helpful unlike the others? Should we trust him? ',
             'I think you should follow your gut and take his word. The detective seems reluctant, let’s just leave him behind. It’s too late to quit now.'
             ]
    )
    story.get_page(character_name='adventurer', chapter=2, page='outro').add_page_variation(
        txt=['Wow, it seems like you came off a bit too invasive. People here get annoyed very quickly. You mix that with alcohol and you get a ticking bomb. ',
             'Oh great, look at what you’ve done. Now they’re all yelling and throwing chairs at you. ', 
             'Quick, run! And make sure to split up so they won’t find you. ',
             'And next time try being more subtle with your questions maybe? ',
             'And also maybe not forget the ~treasure~ with the wise man?'
             ]
    )

    story.get_page(character_name='adventurer', chapter=3, page='intro').add_page_variation(
        txt=['Looks like you took your time to get here. I guess that little runaway you had messed up your sense of direction. ',
             'No worries, it’s not like there’s a curse you have to lift off the city. ',
             'What is this place. Bloody hell desolate ruins. Just like your adventuring skills. Hah. And they say misery can’t be funny. ',
             'Speaking of funny, that’s one hell of a funny looking lady over there. ',
             'Go on now, quick, overwhelm her with your shenanigans and have her hit you with that wand of hers. ',
             'She’s actually being friendly to you and sharing her story as well. Yup. Definitely not a local. ',
             'And once you’re done rambling about how there are no wizards in this place, could you please take the time to notice the hieroglyphs on the walls. ',
             'She seems to recognize some symbols and says it’s linked to some prophecy, but she just can’t pinpoint exactly what it is. ',
             'Maybe it would help  if you show her the ~treasure~ you found in the city center? ',
             'Oh how classic, you lost it. Why am I not surprised. At least you still have that ~tech~ you got from the Alien. Now make yourself useful by making it useful. ',
             'Interesting.. It’s actually translating the code. So now you know there is no curse. Good. However there is an ancient ritual for summoning a bloodcurdling creature every 500 years. Bad. Very Bad. ',
             'Calm down now, listen to what your partner has to say. '
             'She says she knows what items are necessary for this ritual, and she knows for a fact that all the formal prerequisites have already been fulfilled. Very, very bad.'
             ]
    )

    story.get_page(character_name='adventurer', chapter=3, page='outro').add_page_variation(
        txt=['Hold on a second. The wizard seems to be picking up on a signal or something from the ~tech~ . Hand over the ~tech~ to her and let her lead the way. ',
             'Oh my, the energy from the ~tech~ just got unbearably massive. ',
             'Congratulations, you got to the right place in no time. ']
    )
    story.get_page(character_name='adventurer', chapter=3, page='outro').add_page_variation(
        txt=['Hmm.. What is that tiny writing in the corner of the wall? Another hint Maybe? Why don’t you read it. ',
             'Oups, mea culpa. This one is on me, so I’ll get you out of it. ',
             'After scanning the area, there seems to be a Jabuticaba. Such an unusual location for a Brazillian grape tree. Just go over there and check if there is something behind it. ',
             'Et voilà! There you have your secret tunnel. Oh what would you two do without me. ',
             'Now you must go through the tunnel, it’s the only way out. ',
             'You can thank me later.'
             ]
    )   
    story.get_page(character_name='adventurer', chapter=4, page='intro').add_page_variation(
        txt=['The door slams wide open and you all are overwhelmed by someone. Someone you can’t see, but you can feel.',
        ' You can sense him with your entity, moving through your body and into your soul.',
        'Messing with your head, reaching your heart and pulling it strings. The feeling is so intense you wish he would just rip it out already. '.
        'Yes it’s him. He is real and he is here. The greatest trick he ever pulled was convincing the world he didn’t exist.',
       'You must be wondering why he went through all this trouble to gather you all here. What are the chances that four beings,',
        'with such contrasting backgrounds and traits, ending up here. At this exact place, this exact time.'

        ]
    )

    story.get_page(character_name='adventurer', chapter=4, page='outro').add_page_variation(
        txt=['How did he plan all this? Let me help you my dears by telling you that he didn’t.',

'You by your own choice and your own will, took every step that led you to this place.',

'And he, like always, is ecstatic that the entire universe conspired to help  him find you.', 

'He is not your enemy. The only real enemy to have ever existed, is an internal one.',

'You can’t give in to this. You can’t get sucked in by the darkness.',
 
'This is exactly what he wants, don’t hand it to him. Don’t pour salt to the open wound. Fight his evil with good, and his darkness with light.',

'Can you see it now? Is it getting clearer? Can you see how each and every one of you, despite your differences, helped one another do and be better?',

'You came to this city all alone, you crossed paths with a hundred other people. But you chose these three standing in front of you.',

'You didn’t fall into this maze. You  walked into it, with your eyes wide open, choosing to take every step along the way.',
 'Maybe there is no fate or destiny, but I believe you are only fated to do the things that you’d choose anyway.'
'And you’d choose each other; in a hundred lifetimes, in a hundred worlds, in any version of reality, you’d find one another and you’d choose one another.',

'You all, remember where you were when this journey first started, and look at yourselves now.',

'The more you look, the clearer you see, the faster the peace and serenity take over.',

'All you touch and all you see is all your lives would ever be. And now, your lives would never be the same, after crossing paths with these exceptional people.'

'So here’s the best part, distilled for you; you saved yourselves, and in the process saved the world from doom.'

'Congrats my dears. It was a blast accompanying you on this journey.
']
    )

    story.get_page(character_name='adventurer', chapter=4, page='outro').add_page_variation(
        txt=['How did he plan all this? Let me help you my dears by telling you that he didn’t.',
'You by your own choice and your own will, took every step that led you to this place.',
'And he, like always, is ecstatic that the entire universe conspired to help  him find you.',
'He is not your enemy. The only real enemy to have ever existed, is an internal one.',
'You the adventurer, are your own enemy. Fleeing from place to place all your life, trying to fill the void inside.',
 'But in reality you are fleeing yourself. Fleeing the dissatisfaction, seeking glorification and validation, as if your values increases by the count of the places you explore.',
'You the detective, are your own enemy. Spending your entire time solving people’s issues so you wouldn’t have to face your own.',
 'Helping people is merely an overcorrection for the fact that you were responsible for your own brother’s death.',
'You the Wizard, are your own enemy. You spent your entire life isolated,  hating humans before they hate you.',
 'Convincing yourself that you are better than them, more powerful, and that your magic is something they envy you for.',
  'When really you are the one envying them for a life so simple and sweet. All you ever wanted was to flee and live a normal life.',
   'To live like a human.',
'You the Alien, are your own enemy. You must’ve really hated your own kind for you to travel all the way from Mars.',
 'You were always the underdog of aliens, they all thought you weren’t good enough and you knew it.',
'You want us to believe you got on a spaceship all alone for 157 just for research? Who are you kidding ? You were never good enough for your people, they underestimated you.',
 'The only time they ever looked up to you was because you let them down. And now you come here to this planet, thinking you’re superior, plotting to take over the world.',
'You all, look at yourselves now. Look at where the devil in you got you.',
'The more you look, the deeper you see, the faster the darkness takes over.',
'All you touch and all you see is all your lives would ever be.',
'But now all there is, is darkness. You and everything surrounding you vanish into nothingness.',
'So long my friends, i am pained to have lost this way.']
    story.get_page(character_name='adventurer', chapter=4, page='outro').set_last_page(True)


    # ----- Detective : -----
    story.get_page(character_name='detective', chapter=0, page='intro').add_page_variation(
        txt=['You are a detective...you guess? You’re not sure, but that’s what the namecard said that you found in your coat pocket.',
            'You are new in this town and you arrived with nothing but the clothes on your body, a fragmented mind and hands covered in blood.',
            'You don’t know what exactly happened and you’re not sure if you care to find out. All you remember is waking up on the cold floor and seeing your broth-never mind.',
            'You don’t want to think about it. You don’t want to think about anything right now, except a nice glass of scotch. Anything to dull your senses and make this cold world a little bit more bearable.',
            'Sometimes you think that this is a great opportunity: to start your life over as a new person. Leave your regrets and mistakes behind and be a new man.',
            'But deep down you know that the past will catch up with you. It always does. And it torments you with half-forgotten memories and leaves you behind with a throbbing headache and burning eyes.']
    )

    story.get_page(character_name='detective', chapter=1, page='intro').add_page_variation(
        txt=['You can’t sleep at night and during the day you are restless and anxious. So you go out, sit down on a park bench.',
            'Do the pedestrians know that you’re a murderer when they look at you? Do they know that your ~weapon~ is hidden beneath your coat?',
            'Can they still see the blood under your fingernails, even though you already scrubbed your hands raw? Your thoughts are suddenly interrupted when a girl approaches you.',
            'She’s wearing an intricate dress covered with exotic patterns and ornaments and her whole body is decked out with jewelry.',
            'She looks incredibly out of place but her eyes speak of kindness and compassion. She asks you, if you need help. You try to send her away, you really do, but she’s insistent.',
            'Eventually, you settle on giving her scraps of the truth.',
            'You let her know about your amnesia. Your occupation. But instead of telling her that you’d rather leave the past behind, you invent some bullshit about wanting to piece together what really happened.',
            'There’s no need for her to be bogged down with your issues. You don’t want to hurt even more people. She’s also looking for something, babbles something about curses and energy.',
            'You start paying attention when she ignites a flame in the palm of her hand. A wizard? A sorceress? Finally you agree to help her. Together you begin to explore the city. She, on a quest to do good, burning with earnest passion.',
            'You… well. You suppose you could try your luck.']
    )

    story.get_page(character_name='detective', chapter=1, page='outro').add_page_variation(
        txt=['By sheer coincidence you find an envelope. It is tucked between the branches of a tree and curiously, it is addressed to… you.',
            'Upon opening it, two slivers of paper fall out: the first one is a short note. It simply reads: Do You Miss Me? And then, at the bottom, initials.',
            'They are so familiar to you that it aches. Where have you seen them before? From where do you know this handwriting?',
            'You feel the beginning of a headache develop behind the back of your eyes. You tell yourself to focus, dig deeper and then… a memory.',
            'Hatred bubbling up in you, a flash of blue eyes and a sneer. You remember him. He is here. Your...nemesis. It leaves you shaking. Does he know you’re here?',
            'Is he following you? What does he want? You do not know what is written on the second paper but it must be equally concerning, as the wizard pales at the sight of the letter.',
            'She attempts to tell you what the problem is, tries to convince you to join her. But you feel numb. Her words pass through you and all you can think about… is him.',
            'Him, on your tracks like a bloodhound. It is not difficult to imagine what he would do to this young woman, if he found her with you.',
            'So you tell her that you have to attend to personal matters. It’s better if she doesn’t know. It’s safer this way. And thus, your ways part.']
    )

    story.get_page(character_name='detective', chapter=1, page='outro').add_page_variation(
        txt=['By sheer coincidence you find an envelope. It is tucked between the branches of a tree and curiously, it is addressed to… you.',
            'Upon opening it, two slivers of paper fall out: the first one is a short note. It simply reads: Do You Miss Me? And then, at the bottom, initials.',
            'They are so familiar to you that it aches. Where have you seen them before? From where do you know this handwriting? You feel the beginning of a headache develop behind the back of your eyes.',
            'You tell yourself to focus, dig deeper and then… a memory. Hatred bubbling up in you, a flash of blue eyes and a sneer. You remember him. Your...nemesis. But how is it possible?',
            'You remember… wasn’t he dead? It leaves you shaking. Is he still alive? Is he following you? Another even more terrifiyng thought enters your head.'
            'The thought of an imposter, trying to lure you into a trap. Someone who wants… what? Revenge, maybe?',
            'You do not know what is written on the second paper but it must be equally concerning, as the wizard pales at the sight of the letter.',
            'She attempts to tell you what the problem is, tries to convince you to join her. But you feel numb. Her words pass through you and all you can think about…',
            'is whoever wrote this letter. They are on your tracks like a bloodhound. And it is not difficult to imagine what they would do to this young woman, if they found her with you.',
            'So you tell her that you have to attend to personal matters. It’s better if she doesn’t know. It’s safer this way. And thus, your ways part.']
    )

    story.get_page(character_name='detective', chapter=2, page='intro').add_page_variation(
        txt=['You need more intel, quickly. If it’s really him, then you can’t wait another second. As long as that man is free, this city is in danger.',
            'That megalomaniacal genius, he needs to be stopped. Now, generally speaking you don’t have many talents apart from fucking up the lives of your loved ones.',
            'But gathering information, tracking down people?  That used to be your job and you were damn good at it.',
            'Empirically, the quickest way to find out what you need is to settle down in the seediest bar in town and get the person opposite of you absolutely plastered.',
            'Besides, you could do with a stiff drink yourself. The bar you end up in is… alright. Populated by various drunkards and lowlifes, you’ll fit right in.',
            'You order a glass of scotch, lean against the counter and wait for the right moment to strike. That is when a young woman enters the bar. She’s all loud swagger and devil-may-care grin.',
            'But behind her sunglasses… is that fear in her eyes? She sits down next to you, orders a beer and tries to strike up a conversation with you.',
            'Obviously, she thinks you’re a local. You take note of the jittery movements of her hands. Withdrawal symptoms? No, she doesn’t seem like an addict.',
            'There is dirt beneath her nails, so she works with her hands. Well-worn backpack, she travels light and often but doesn’t have the cash to buy new equipment.',
            'Some sort of freelancer maybe? She strikes you as the adventorous type. Either way, she’s not from here which makes her useless to you. That is, until she explains why she is here.',
            'She got a tip from someone and when she names their initials your blood freezes in its veins.',
            'She says something about a curse, God, what is it with people and magic these days, you wonder, but if she’s working with him, you bet that you’re going to help her with whatever she wants.',
            'Maybe this way you’ll figure out what is going on. And since she wants to talk to locals about some kind of curse that she has unleashed and since she needs help… why the hell not?']
    )

    story.get_page(character_name='detective', chapter=2, page='outro').add_page_variation(
        txt=['You finish listening to the biography of one of the patrons and turn to see the woman talking to an elderly man. He seems oddly familiar and that is enough to make you very suspicious.',
            'The woman rummages in her backpack and pulls something out that seems to be very old and very precious.',
            'The headache returns and you flinch again – something about the artefact triggers a feeling in you but for the life of you, you can’t figure out why.',
            'You see the way the man stares at it and decide to keep an eye on him. Sure enough, as soon as she turns away his quick fingers manage to get a hold of it and the artefact vanishes into his own briefcase.',
            'It takes everything in you not to get up right then and there to confront that bastard and your fingers are twitching, almost reaching for your ~weapon~. Instead, you wait.',
            'The woman returns to you and says she got a tip to go eastwards. She’ll be moving on and thanks you for your help. You grimace, say nothing, and wave her goodbye.',
            'It’s likely that the man is deliberately trying to distract her and that he sent her off to who knows where. But whoever that man is… he was too skilled to be a simple pick-pocket.',
            'He’s probably affiliated with someone of his likes. And also, you’re going to get that woman her treasure back, damn it. Like hell you’re letting a thief get away with something like this.',
            'So as soon the man finishes his drink and gets up to leave, you follow from a distance. Eventually, you see him enter a building – it seems like a research facility.',
            'You don’t have the time for a stake out, so you sneak around the building and break a window on the ground floor. Fuck it, you’ll deal with the consequences once you’re inside.']
    )

    story.get_page(character_name='detective', chapter=2, page='outro').add_page_variation(
        txt=['You finish listening to the biography of one of the patrons and turn to see the woman talking to an elderly man. He seems oddly familiar and that is enough to make you very suspicious.',
            'The woman rummages in her backpack and pulls something out that seems to be very old and very precious.',
            'The headache returns and you flinch again – something about the artefact triggers a feeling in you but for the life of you, you can’t figure out why.',
            'You see the way the man stares at it and decide to keep an eye on him. Sure enough, as soon as she turns away his quick fingers manage to get a hold of it and the artefact vanishes into his own briefcase.',
            'Immediately, you reach for your ~weapon~ and call him out. Everyone in the bar is staring at you. Then the shouting begins.',
            'Who are you calling a thief, huh? Never seen you around, who the hell are you? The sound of breaking bottles. The woman looks like she’s mildly confused but ready to punch someone.',
            'Once again you command the man to return his stolen goods. He denies everything. Then everything happens in a flash.',
            'You yell at the woman to get the hell out of there and before the bartender can take out his shotgun from under the counter you’re fighting your way through the crowd.',
            'You have been in a fair share of brawls yourself but whoever that woman is, she knows how to stand  her ground and throw a punch or two. Bones crack and blood flows but it doesn’t matter.',
            'Both of you make it out of the building and then you start running. Without thinking you turn left, see an open window on the ground floor and take a chance.',
            'It is only once you’re inside, lying flat on the floor and catching your breath that you realize you’ve lost the woman. You hope she’s alright.']
    )

    story.get_page(character_name='detective', chapter=3, page='intro').add_page_variation(
        txt=['The room you find yourself in is sparse. There is a large table in the middle and vast array of different medical tools.',
            'And there, in the corner, there’s a cage with a… human in it? What the fuck. What is this place? He stares at you and seems to be about as confused as you are.',
            'Then he asks you for help. It’s a strange trilling sound, not like any accent you know. You hesitate for a moment.',
            'What if he’s some kind of freak of nature or has some deadly illness? And now that you get closer you notice that something is wrong with him after all.',
            'Looking at him… it causes your eyes to water. His skin is stretched a little bit too tight across his bones and his clothes hang off his frame in an odd way.',
            'You ask him what he is, because he sure as hell ain’t human. He replies that indeed, he isn’t. He’s a scientist from another planet sent to earth to study humans.',
            'Unfortunately, he was now captured by government officials who intend to study him. I chuckle at the irony of this but he doesn’t see to think it’s particularly funny.',
            'Throughout your career you have learned to distinguish the liars from people who speak the truth. Now, you’re not sure if this can be applied to aliens as well, but you don’t think that he’s lying.',
            'So you use your ~weapon~ to break the lock of the cage and tell him to leave. But to no avail. The alien has decided to return the favor and assist you with… what exactly?',
            'The alien tells you that while he was locked away, he heard someone talking about secret artefacts. The walls are thin here - the voice must have come from the adjacent room.',
            'You heart leaps at this suggestion. Could it be that the thief from the bar is involved with this somehow? Together with the alien you sneak out and enter the other room forcefully.',
            'Luckily nobody is inside. It appears to be a lab, walls covered with dozens of papers and drawings of obscure objects. Details about past events.',
            'Both of you wander around and attempt to learn as much as possible about the history these papers detail.']
    )

    story.get_page(character_name='detective', chapter=3, page='outro').add_page_variation(
        txt=['The alien yelps and points at the desk. He recognizes these, he says, what are the odds? To your surprise, you find the treasure of the woman and some kind of… jewelry?',
            'Why is that also so familiar to you? And then suddenly all your memories come rushing back. He is there, after all these years of animosity, after all these times you nearly caught him.',
            'He has your brother, you are there as well, pleading him to let him go. Instead, a shot rings out and the lifeless body of your brother drops to the floor.',
            'You cry out, seeking revenge but he, your nemesis, he keeps going on and on about the way all the artefacts are supposed to fit together.',
            'You are familiar with this topc of course, after all you memorized the plan before destroying it. That was why he attempted to blackmail you in the first place.',
            'With nothing to hold you back now you lunge at him, tackling him to the ground.',
            'But he quickly escapes your grip and gets a fistful of your hair before he smashes your head into a boulder. Then: darkness.',
            'You grip your head, now, in the present. You are shaking but you remember everything. And...you are pissed.',
            'The alien seems to be concerned but doesn’t have much time to dwell on it as the door abruptly swings open.']
    )

    story.get_page(character_name='detective', chapter=3, page='outro').add_page_variation(
        txt=['On the desk you find the treasure of the woman and some kind of… jewelry?',
            'Why is that also so familiar to you? And then suddenly all your memories come rushing back. He is there, after all these years of animosity, after all these times you nearly caught him.',
            'He has your brother, you are there as well, pleading him to let him go. Instead, a shot rings out and the lifeless body of your brother drops to the floor.',
            'You cry out, seeking revenge but he, your nemesis, he keeps going on and on about the way all the artefacts are supposed to fit together.',
            'You are familiar with this topc of course, after all you memorized the plan before destroying it. That was why he attempted to blackmail you in the first place.',
            'With nothing to hold you back now you lunge at him, tackling him to the ground.',
            'But he quickly escapes your grip and gets a fistful of your hair before he smashes your head into a boulder. Then: darkness.',
            'You grip your head, now, in the present. You are shaking but you remember everything. And...you are pissed.',
            'The alien seems to be concerned but doesn’t have much time to dwell on it as the door abruptly swings open.']
    )

    story.get_page(character_name='detective', chapter=4, page='intro').add_page_variation(
        txt=['The door slams wide open and you all are overwhelmed by someone. Someone you can’t see, but you can feel.',
        ' You can sense him with your entity, moving through your body and into your soul.',
        'Messing with your head, reaching your heart and pulling it strings. The feeling is so intense you wish he would just rip it out already. '.
        'Yes it’s him. He is real and he is here. The greatest trick he ever pulled was convincing the world he didn’t exist.',
       'You must be wondering why he went through all this trouble to gather you all here. What are the chances that four beings,',
        'with such contrasting backgrounds and traits, ending up here. At this exact place, this exact time.'

        ]
    )

    story.get_page(character_name='detective', chapter=4, page='outro').add_page_variation(
        txt=['How did he plan all this? Let me help you my dears by telling you that he didn’t.',

'You by your own choice and your own will, took every step that led you to this place.',

'And he, like always, is ecstatic that the entire universe conspired to help  him find you.', 

'He is not your enemy. The only real enemy to have ever existed, is an internal one.',

'You can’t give in to this. You can’t get sucked in by the darkness.',
 
'This is exactly what he wants, don’t hand it to him. Don’t pour salt to the open wound. Fight his evil with good, and his darkness with light.',

'Can you see it now? Is it getting clearer? Can you see how each and every one of you, despite your differences, helped one another do and be better?',

'You came to this city all alone, you crossed paths with a hundred other people. But you chose these three standing in front of you.',

'You didn’t fall into this maze. You  walked into it, with your eyes wide open, choosing to take every step along the way.',
 'Maybe there is no fate or destiny, but I believe you are only fated to do the things that you’d choose anyway.'
'And you’d choose each other; in a hundred lifetimes, in a hundred worlds, in any version of reality, you’d find one another and you’d choose one another.',

'You all, remember where you were when this journey first started, and look at yourselves now.',

'The more you look, the clearer you see, the faster the peace and serenity take over.',

'All you touch and all you see is all your lives would ever be. And now, your lives would never be the same, after crossing paths with these exceptional people.'

'So here’s the best part, distilled for you; you saved yourselves, and in the process saved the world from doom.'

'Congrats my dears. It was a blast accompanying you on this journey.
']
    )

    story.get_page(character_name='detective', chapter=4, page='outro').add_page_variation(
        txt=['How did he plan all this? Let me help you my dears by telling you that he didn’t.',
'You by your own choice and your own will, took every step that led you to this place.',
'And he, like always, is ecstatic that the entire universe conspired to help  him find you.',
'He is not your enemy. The only real enemy to have ever existed, is an internal one.',
'You the adventurer, are your own enemy. Fleeing from place to place all your life, trying to fill the void inside.',
 'But in reality you are fleeing yourself. Fleeing the dissatisfaction, seeking glorification and validation, as if your values increases by the count of the places you explore.',
'You the detective, are your own enemy. Spending your entire time solving people’s issues so you wouldn’t have to face your own.',
 'Helping people is merely an overcorrection for the fact that you were responsible for your own brother’s death.',
'You the Wizard, are your own enemy. You spent your entire life isolated,  hating humans before they hate you.',
 'Convincing yourself that you are better than them, more powerful, and that your magic is something they envy you for.',
  'When really you are the one envying them for a life so simple and sweet. All you ever wanted was to flee and live a normal life.',
   'To live like a human.',
'You the Alien, are your own enemy. You must’ve really hated your own kind for you to travel all the way from Mars.',
 'You were always the underdog of aliens, they all thought you weren’t good enough and you knew it.',
'You want us to believe you got on a spaceship all alone for 157 just for research? Who are you kidding ? You were never good enough for your people, they underestimated you.',
 'The only time they ever looked up to you was because you let them down. And now you come here to this planet, thinking you’re superior, plotting to take over the world.',
'You all, look at yourselves now. Look at where the devil in you got you.',
'The more you look, the deeper you see, the faster the darkness takes over.',
'All you touch and all you see is all your lives would ever be.',
'But now all there is, is darkness. You and everything surrounding you vanish into nothingness.',
'So long my friends, i am pained to have lost this way.']
    )

    story.get_page(character_name='detective', chapter=4, page='outro').set_last_page(True)

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
        txt=['The door slams wide open and you all are overwhelmed by someone. Someone you can’t see, but you can feel.',
        ' You can sense him with your entity, moving through your body and into your soul.',
        'Messing with your head, reaching your heart and pulling it strings. The feeling is so intense you wish he would just rip it out already. '.
        'Yes it’s him. He is real and he is here. The greatest trick he ever pulled was convincing the world he didn’t exist.',
       'You must be wondering why he went through all this trouble to gather you all here. What are the chances that four beings,',
        'with such contrasting backgrounds and traits, ending up here. At this exact place, this exact time.'

        ]
    )

    story.get_page(character_name='wizard', chapter=4, page='outro').add_page_variation(
        txt=['How did he plan all this? Let me help you my dears by telling you that he didn’t.',

'You by your own choice and your own will, took every step that led you to this place.',

'And he, like always, is ecstatic that the entire universe conspired to help  him find you.', 

'He is not your enemy. The only real enemy to have ever existed, is an internal one.',

'You can’t give in to this. You can’t get sucked in by the darkness.',
 
'This is exactly what he wants, don’t hand it to him. Don’t pour salt to the open wound. Fight his evil with good, and his darkness with light.',

'Can you see it now? Is it getting clearer? Can you see how each and every one of you, despite your differences, helped one another do and be better?',

'You came to this city all alone, you crossed paths with a hundred other people. But you chose these three standing in front of you.',

'You didn’t fall into this maze. You  walked into it, with your eyes wide open, choosing to take every step along the way.',
 'Maybe there is no fate or destiny, but I believe you are only fated to do the things that you’d choose anyway.'
'And you’d choose each other; in a hundred lifetimes, in a hundred worlds, in any version of reality, you’d find one another and you’d choose one another.',

'You all, remember where you were when this journey first started, and look at yourselves now.',

'The more you look, the clearer you see, the faster the peace and serenity take over.',

'All you touch and all you see is all your lives would ever be. And now, your lives would never be the same, after crossing paths with these exceptional people.'

'So here’s the best part, distilled for you; you saved yourselves, and in the process saved the world from doom.'

'Congrats my dears. It was a blast accompanying you on this journey.
']
    )

    story.get_page(character_name='wizard', chapter=4, page='outro').add_page_variation(
        txt=['How did he plan all this? Let me help you my dears by telling you that he didn’t.',
'You by your own choice and your own will, took every step that led you to this place.',
'And he, like always, is ecstatic that the entire universe conspired to help  him find you.',
'He is not your enemy. The only real enemy to have ever existed, is an internal one.',
'You the adventurer, are your own enemy. Fleeing from place to place all your life, trying to fill the void inside.',
 'But in reality you are fleeing yourself. Fleeing the dissatisfaction, seeking glorification and validation, as if your values increases by the count of the places you explore.',
'You the detective, are your own enemy. Spending your entire time solving people’s issues so you wouldn’t have to face your own.',
 'Helping people is merely an overcorrection for the fact that you were responsible for your own brother’s death.',
'You the Wizard, are your own enemy. You spent your entire life isolated,  hating humans before they hate you.',
 'Convincing yourself that you are better than them, more powerful, and that your magic is something they envy you for.',
  'When really you are the one envying them for a life so simple and sweet. All you ever wanted was to flee and live a normal life.',
   'To live like a human.',
'You the Alien, are your own enemy. You must’ve really hated your own kind for you to travel all the way from Mars.',
 'You were always the underdog of aliens, they all thought you weren’t good enough and you knew it.',
'You want us to believe you got on a spaceship all alone for 157 just for research? Who are you kidding ? You were never good enough for your people, they underestimated you.',
 'The only time they ever looked up to you was because you let them down. And now you come here to this planet, thinking you’re superior, plotting to take over the world.',
'You all, look at yourselves now. Look at where the devil in you got you.',
'The more you look, the deeper you see, the faster the darkness takes over.',
'All you touch and all you see is all your lives would ever be.',
'But now all there is, is darkness. You and everything surrounding you vanish into nothingness.',
'So long my friends, i am pained to have lost this way.']

    story.get_page(character_name='wizard', chapter=4, page='outro').set_last_page(True)
