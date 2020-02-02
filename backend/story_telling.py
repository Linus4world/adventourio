from story_structure_v2 import *

# THIS IS A STORY EXAMPLE
def get_story_one():
    story = Story()

    story.add_blank('B00', ['apples', 'bananas', 'tomatoes'])
    story.add_blank_random('B01', 'noun')
    story.add_blank_random('B02', 'verb')

    # Add challenges to the story:
    story.load_all_challenges('challenges_v2.json')

    # # Add content of the story:
    story.get_page(character_name='alien', chapter=0, page=0).add_page_variation(
        txt=['Hello',
             'The word: ~B00~ has been randomly selected from a list',
             'And this word: ~B01~ has been randomly selected from the internet',
             'And this one as well: ~B02~',
             ]
    )

    # Adding Page 2
    # story.get_page(character='alien', chapter=0, page=1).set_page_type('challenge')
    story.get_page(character_name='alien', chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 1'], challenge=story.get_challenge('00')
    )
    story.get_page(character_name='alien', chapter=0, page=1).add_page_variation(
        txt=['CHALLENGE 2'], challenge=story.get_challenge('01')
    )

    # Adding Page 3
    story.get_page(character_name='alien', chapter=0, page=2).set_page_type('outcome')
    story.get_page(character_name='alien', chapter=0, page=2).add_page_variation(
        txt=['Good outcome']
    )
    story.get_page(character_name='alien', chapter=0, page=2).add_page_variation(
        txt=['Bad outcome']
    )

    return story