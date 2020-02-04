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

    # --------------- ADDING CONTENT ---------------

    # ----- ALIEN: -----
    story.get_page(character_name='alien', chapter=0, page='intro').add_page_variation(
        txt=['Welcome to what your people call Planeta stultorum! Here it’s just called Earth. ',
             'I know you’re not thrilled to be here,but trust me your 157 day trip from Mars will be worth it. ',
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
        txt=['Such a strange place isn’t it? Yet so appealing. Let’s take a look around , discover the area, draw a mental map of the city, observe its people. ',
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
        txt=['Oh look, a sealed scroll. Should we take the risk and open it? What’s the worst could happen anyway, let’s just read what’s inside. ',
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
             'Well if you look over there you can see a big building that says “Foreigners Registration Office”. Well technically  you are a foreigner, so i say we go in and check out the place. ',
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
             'Oh look at her with her manners, offering you a cup of water. Just drink it, humans drink water. Tastes horrible right? That’s actually the main reason they want to invade your planet. ',
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
    story.get_page(character_name='alien', chapter=4, page='outro').set_last_page(True)

    # ----- ADVENTURER: -----
    story.get_page(character_name='adventurer', chapter=0, page='intro').add_page_variation(
        txt=['Ahoy Adventurer! Finally arrived at the promising land. How are you feeling after your 3 weeks cruise with the pirates? I hope you’re not too tired. ',
             'You need to be in your best game if you wanna find the hidden ~treasure~.'
             ]
    )

    story.get_page(character_name='adventurer', chapter=1, page='intro').add_page_variation(
        txt=['A beautiful city isn’t it? Let’s take a look around , have a long walk, admire the city, embrace its vibe. ',
             'So many food stands everywhere, and the food smells phenomenal. Getting hungry huh? May I suggest pizza? Oh god no, not the pineapple pizza! ',
             'C’mon that’s common sense 101. ',
             'You’re lucky this guy just stopped you. ',
             'Perfect timing i must say. It’s almost as if he was already here, watching you.. ',
             'But let’s not jump to conclusions, he is obviously new here and just wants to make friends. ',
             'Although, he is a weird looking fella.. And what’s that beeping device he’s trying so hard to hide? ',
             'Just look closely and focus. C’mon you know this one. It’s ~tech~ ! ',
             'What kind of lunatic walks around with a ~tech~ ? ',
             'On second thought, this is exactly what you need to find the ~treasure~ . '
             'Let’s get him on board, a ~treasure~ hunt is more fun in pairs anyway!'.

]
    )

    story.get_page(character_name='adventurer', chapter=1, page='outro').add_page_variation(
        txt=['Magnificent, you found it very easily. Too easily actually, now that we think about .. ',
             'Did the secret messenger send you all the way to Munich just to find this ~treasure~ in one hour? ',
             'This can’t be it. It must be just a misdirection. The real treasure must be hidden somewhere else. ',
             'Wait what’s happening here? Are you sensing this magic wave? Were you just cursed? ',
             'Well now we know for sure there’s more to this mystery. ',
             'Let’s go, take the device and leave alone, this whole situation just got too risky.'
            ]
    )

      story.get_page(character_name='adventurer', chapter=1, page='outro').add_page_variation(
        txt=['Oh look, a sealed scroll. Should we take the risk and open it? What’s the worst could happen anyway, let’s just read what’s inside. ',
             ' “Breaking this seal, breaks your destiny. Accept the deal, or follow the mystery” ',
             'Oh oh, looks like you’ve been cursed. You can’t quit now. ',
             'The destiny of this city lies in your hands, you must go on with this quest and lift the curse. ',
             'I say you leave alone with the ~tech~ and seek the help of the locals instead.'
             ]
    )

    story.get_page(character_name='adventurer', chapter=2, page='intro').add_page_variation(
        txt=['A bar, the perfect place to get intel from drunken locals. Take a look around and  try to find a resourceful target. ',
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
             'Oh great , look at what you’ve done. Now they’re all yelling and throwing chairs at you. ', 
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
             'Oh how classic,you lost it. Why am I not surprised. At least you still have that ~tech~ you got from the Alien. Now make yourself useful by making it useful. ',
             'Interesting.. It’s actually translating the code. So now you know there is no curse. Good. However there is an ancient ritual for summoning a bloodcurdling creature every 500 years. Bad. Very Bad. ',
             'Calm down now, listen to what your partner has to say. '
             'She says she knows what items are necessary for this ritual, and she knows for a fact that all the formal prerequisites have already  been fulfilled. Very very bad.'
             ]
    )

    story.get_page(character_name='adventurer', chapter=3, page='outro').add_page_variation(
        txt=['Hold on a second. The wizard seems to be picking up on a signal or something from the ~tech~ . Hand over the ~tech~ to her and let her lead the way. ',
             'Oh my, the energy from the ~tech~ just got unbearably massive. ',
             'Congratulations, you got to the right place in no time. ']
    )
    story.get_page(character_name='adventurer', chapter=3, page='outro').add_page_variation(
        txt=['Hmm.. What is that tiny writing in the corner of the wall? Another hint Maybe? Why don’t you read it. ',
             'Oups,mea culpa. This one is on me, so I’ll get you out of it. ',
             'After scanning the area, there seems to be a Jabuticaba. Such an unusual location for a Brazillian grape tree. Just go over there and check if there is something behind it. ',
             'Et voilà! There you have your secret tunnel. Oh what would you two do without me. ',
             'Now you must go through the tunnel, it’s the only way out. ',
             'You can thank me later.'
             ]
    )   

    story.get_page(character_name='adventurer', chapter=4, page='outro').set_last_page(True)


    # ----- Wizard : -----
    story.get_page(character_name='wizard', chapter=0, page='intro').add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list'
             # 'And this word: ~B01~ has been randomly selected from the internet',
             ]
    )

    story.get_page(character_name='wizard', chapter=0, page='outro').add_page_variation(
        txt=['Good outcome']
    )
    story.get_page(character_name='wizard', chapter=0, page='outro').add_page_variation(
        txt=['Bad outcome']
    )
    story.get_page(character_name='wizard', chapter=0, page='outro').set_last_page(True)

    # ----- Wizard : -----
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