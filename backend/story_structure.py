from utils import *
import numpy as np
import random


class Blank:
    def __init__(self, name, words, w_type='', random_word=False):
        self.name = name
        self.words = words

        self.w_type = w_type
        self.random_word = random_word


class UserInput:
    def __init__(self, name='', q_type='', scenario_mapping=None, weight=0, answer=''):
        self.name = name
        self.q_type = q_type
        # Maps the user input to a scenario.name dict(option_A='scenario1',option_B='scenario2')
        self.scenario_mapping = scenario_mapping
        self.weight = weight
        self.answer = answer


class Story:
    def __init__(self):
        self.story_name = ''
        self.chapters = []

    def run_story(self):
        user_inputs = None
        for chapter in self.chapters:
            scenario = chapter.get_next_scenario(user_inputs)
            scenario.run_scenario()
            user_inputs = scenario.user_inputs

    # This will be a BIG BIG task
    def load_story(self):
        pass

    @staticmethod
    def setup():
        # Creating the intro
        intro = Scenario()

        intro.add_blank(blank_key='B1', words=['beautiful', 'ugly'])
        intro.add_blank(blank_key='B2', w_type='adjective', random_word=True)

        intro.add_user_input(input_key='I1', name='Question name')
        intro.add_user_input(input_key='I2', q_type='multiple choice', scenario_mapping=dict(A='scenario1', B='scenario2'),
                             weight=1)

        intro.plot = ['Hello, how are you doing in this ',
                      'B1',
                      ' day?',
                      'I1',
                      'Oh I am very ',
                      'B2',
                      ' that you are doing ',
                      'A1',
                      '\nWould you like to do A or B?',
                      'I2',
                      'Some more text\n']

        story.chapters.append(Chapter([intro]))

        # Creating two more scenarios

        scenario1 = Scenario()
        scenario1.plot = ['PLOT A']
        scenario1.name = 'scenario1'
        scenario2 = Scenario()
        scenario2.plot = ['PLOT B']
        scenario2.name = 'scenario2'

        story.chapters.append(Chapter([scenario1, scenario2]))


class Chapter: #stage
    def __init__(self, scenarios):
        self.end = False
        self.beginning = False
        self.scenarios = scenarios
        self.scenario_probabilities = [0] * len(scenarios)

    def get_next_scenario(self, user_inputs):
        next_scenario = Scenario()
        if user_inputs is not None:
            for user_input in user_inputs.values():
                # Multiple Choice
                if user_input.q_type == 'multiple choice':
                    for c, scenario in enumerate(self.scenarios):
                        scenario_picked_by_user = user_input.scenario_mapping[user_input.answer]
                        if scenario_picked_by_user == scenario.name:
                            self.scenario_probabilities[c] += user_input.weight

            next_scenario = self.scenarios[np.argmax(self.scenario_probabilities)]

        else:
            next_scenario = random.choice(self.scenarios)
        return next_scenario


class Scenario: #substage
    def __init__(self):
        self.name = ''
        self.location = ''
        self.plot = []  # array of stings!
        self.blanks = dict()
        self.user_inputs = dict()

    # This function can later used to add blanks from a dictionary or Wikipedia!
    def add_blank(self, blank_key, name='', w_type='', words=None, random_word=False):
        self.blanks[blank_key] = Blank(name=name, words=words, w_type=w_type, random_word=random_word)

    def add_user_input(self, input_key='', name='', q_type='', scenario_mapping=None, weight=0, answer=''):
        self.user_inputs[input_key] = UserInput(name=name, q_type=q_type, scenario_mapping=scenario_mapping, weight=weight,
                                                answer=answer)

    def store_user_answer(self, input_key, answer):
        self.user_inputs[input_key].answer = answer

    # Replace all blank.name for a word from the blank.words list in the plot
    def fill_in_the_blank(self, blank_key):
        word = ''
        if blank_key in self.blanks.keys():
            if self.blanks[blank_key].random_word:
                word = get_random_word(self.blanks[blank_key].w_type)
            else:
                word = random.choice(self.blanks[blank_key].words)
        return word

    def determine_substage3(challenge_outcome):
        

    def run_scenario(self):

        for txt in self.plot:
            if len(txt) == 2:
                # Input
                if txt[0] == 'I' and txt[1].isnumeric():
                    input_key = txt
                    answer = input("\n> ")
                    self.store_user_answer(input_key=input_key, answer=answer)
                # Blank
                elif txt[0] == 'B' and txt[1].isnumeric():
                    blank_key = txt
                    blank = self.fill_in_the_blank(blank_key)
                    print(blank, end='')
                # Answer: Gives back a user input in the text
                elif txt[0] == 'A' and txt[1].isnumeric():
                    input_key = 'I' + txt[1]
                    user_answer = self.user_inputs[input_key].answer
                    print(user_answer, end='')
            else:
                print(txt, end='')


if __name__ == "__main__":
    story = Story()
    story.setup()
    story.run_story()
