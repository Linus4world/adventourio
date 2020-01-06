import numpy as np
import random
from random_word import RandomWords

class Blank:
    def __init__(self, name, words):
        self.name = name
        self.words = words


class Scenario:
    def __init__(self):
        self.scenario_name = ''
        self.location = ''
        self.plot = ''
        self.blanks = []
        self.next_possible_scenarios = []
        self.scenario_probabilities = []

    def get_next_scenario(self):
        return self.next_possible_scenarios[np.argmax(self.scenario_probabilities)]

    # This function can later used to add blanks from a dictionary or Wikipedia!
    def add_blank(self, name, words=None, random_word=''):
        if words is None:
            words = [get_random_word(random_word)]
        b = Blank(name, words)
        self.blanks.append(b)

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
                player_name = input("> ")

    # Use a json file to load the plot and the blanks
    def load_scenario(self, scenario_file):
        pass


def get_random_word(part_of_speech):
    rw = RandomWords()
    return rw.get_random_word(hasDictionaryDef="true",
                              # includePartOfSpeech='adjective',
                              includePartOfSpeech=part_of_speech,
                              minCorpusCount=50,
                              minDictionaryCount=1,
                              maxDictionaryCount=50,
                              minLength=5,
                              maxLength=10)


def setup():
    # Creating the intro
    intro = Scenario()

    intro.add_blank('B1', words=['beautiful', 'ugly'])
    intro.add_blank('B2', random_word='verb')

    intro.plot = 'Hello, how are you doing in this B1 day? _input_' \
                 'Oh I am very B2 that you are doing well \n' \
                 'Would you like to do A or B? _input_' \
                 'Some more text'

    intro.fill_in_the_blanks()

    intro.run_scenario()

    # Creating two more scenarios

    scenario1 = Scenario()
    scenario2 = Scenario()


if __name__ == "__main__":
    setup()