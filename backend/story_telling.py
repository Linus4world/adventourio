def set_example_story(story):

    # --------------- ADDING CHARACTERS ---------------
    story.add_character(name='adventurer', description='drunk')
    story.add_character(name='alien', description='academic')
    story.add_character(name='wizard', description='foreign cultures')
    story.add_character(name='detective', description='break free')

    # --------------- ADDING BLANKS ---------------
    story.add_blank('B00', ['apples', 'bananas', 'tomatoes'])
    story.add_blank_random('B01', 'noun')
    story.add_blank_random('B02', 'verb')

    # --------------- ADDING CONTENT ---------------
    story.get_page(character_name='alien', chapter=0, page='intro').add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list',
             'And this word: ~B01~ has been randomly selected from the internet',
             ]
    )

    # Adding Page 3
    story.get_page(character_name='alien', chapter=0, page='outro').add_page_variation(
        txt=['Good outcome']
    )
    story.get_page(character_name='alien', chapter=0, page='outro').add_page_variation(
        txt=['Bad outcome']
    )
