from utils import *
import numpy as np
import random


class Blank:
    def __init__(self, name, words):
        self.name = name
        self.words = words


class UserQuestion:
    def __init__(self, name='', q_type='', scenario_mapping=None, weight=0):
        self.name = name
        self.q_type = q_type
        # Maps the user input to a scenario.name dict(option_A='scenario1',option_B='scenario2')
        self.scenario_mapping = scenario_mapping
        self.weight = weight


class Story:
    def __init__(self):
        self.chapters = []

    def run_story(self):
        user_answers = None
        user_questions = None
        for chapter in self.chapters:
            scenario = chapter.get_next_scenario(user_questions, user_answers)
            scenario.run_scenario()
            user_answers = scenario.user_answers
            user_questions = scenario.user_questions

    # This will be a BIG BIG task
    def load_story(self):
        pass

    @staticmethod
    def setup():
        # Creating the intro
        intro = Scenario()

        intro.add_blank('B1', words=['beautiful', 'ugly'])
        # intro.add_blank('B2', words=['happy', 'sad'])
        intro.add_blank('B2', random_word='verb')

        intro.add_question('something else')
        intro.add_question('multiple choice', dict(A='scenario1', B='scenario2'), 1)

        intro.plot = 'Hello, how are you doing in this B1 day? _input_' \
                     'Oh I am very B2 that you are doing well \n' \
                     'Would you like to do A or B? _input_' \
                     'Some more text'

        intro.fill_in_the_blanks()

        story.chapters.append(Chapter([intro]))

        # Creating two more scenarios

        scenario1 = Scenario()
        scenario1.plot = 'PLOT A'
        scenario1.name = 'scenario1'
        scenario2 = Scenario()
        scenario2.plot = 'PLOT B'
        scenario2.name = 'scenario2'

        story.chapters.append(Chapter([scenario1, scenario2]))


class Chapter:
    def __init__(self, scenarios):
        self.end = False
        self.beginning = False
        self.scenarios = scenarios
        self.scenario_probabilities = [0] * len(scenarios)

    def get_next_scenario(self, user_questions, user_answers):

        if user_answers is not None:
            for question, answer in zip(user_questions, user_answers):
                # Multiple Choice
                if question.q_type == 'multiple choice':
                    for c, scenario in enumerate(self.scenarios):
                        scenario_name = question.scenario_mapping[answer]
                        if scenario_name == scenario.name:
                            self.scenario_probabilities[c] += question.weight

            return self.scenarios[np.argmax(self.scenario_probabilities)]

        else:
            return random.choice(self.scenarios)


class Scenario:
    def __init__(self):
        self.name = ''
        self.location = ''
        self.plot = ''
        self.blanks = []
        self.probability_of_happening = 0
        self.user_questions = []
        self.user_answers = []

    # This function can later used to add blanks from a dictionary or Wikipedia!
    def add_blank(self, name, words=None, random_word=''):
        if words is None:
            words = [get_random_word(random_word)]  # This has to be an array because the argument in Blank is an array
        b = Blank(name, words)
        self.blanks.append(b)

    def add_question(self, question_type='', scenario_mapping=None, weight=0):
        user_question = UserQuestion(question_type, scenario_mapping, weight)
        self.user_questions.append(user_question)

    # Replace all blank.name for a word from the blank.words list in the plot
    def fill_in_the_blanks(self):
        for blank in self.blanks:
            word = random.choice(blank.words)  # select a random word from the list
            self.plot = self.plot.replace(blank.name, word)

    def run_scenario(self):
        plot = self.plot.split('_input_')
        number_of_questions = len(plot) - 1
        for c, txt in enumerate(plot):
            print(txt)
            if c < number_of_questions:
                user_answer = input("> ")
                self.user_answers.append(user_answer)

if __name__ == "__main__":
    story = Story()
    story.setup()
    story.run_story()
