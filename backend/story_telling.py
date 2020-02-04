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
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list'
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