from utils import *
import numpy as np
import random

# There are 2 types of blanks:
# 1. A blank is filled in with a word from a list
# 2. A blank is filled with a random word
class Blank:
    def __init__(self, words=None, w_type='', random_word=False, keep_initial_word=True):
        self.words = words
        self.w_type = w_type
        self.random_word = random_word
        self.keep_initial_word = keep_initial_word

    def fill_in_the_blank(self):
        return 'dummy word'

    def fill_in_the_blank_with_random_word(self):
        return 'random word'

    def pick_a_word_from_list(self):
        return random.choice(self.words)


class Challenge:
    def __init__(self, challenge_text='', options=None, location=''):
        self.challenge_text = challenge_text
        self.options = options
        self.location = location

    def run_challenge(self):
        print("CHALLENGE RUNNING!")
#
# class UserInput:
#     def __init__(self, name='', q_type='', scenario_mapping=None, weight=0, answer=''):
#         self.name = name
#         self.q_type = q_type
#         # Maps the user input to a scenario.name dict(option_A='scenario1',option_B='scenario2')
#         self.scenario_mapping = scenario_mapping
#         self.weight = weight
#         self.answer = answer


class Stage:
    def __init__(self):
        self.end = False
        self.beginning = False
        self.sub_stages = []
        self.sub_stage_probabilities = []

    def add_sub_stage(self, plot, location):
        # Split the strings in plot using '~' as a separator
        splitted_plot = []
        for txt in plot:
            splitted_plot += txt.split('~')
        sub_stage = SubStage(splitted_plot, location)
        self.sub_stages.append(sub_stage)

    def pick_a_sub_stage(self):
        # Dummy functionality:
        return random.choice(self.sub_stages)


class SubStage:
    def __init__(self, plot, location):
        self.plot = plot  # array of stings!
        self.location = location


class Story:
    def __init__(self):
        self.story_name = ''
        self.stages = []
        self.challenges = {}
        self.blanks = {}
        self.questions = []  # Nice to have

    def run_story(self):
        pass

    def dummy_run_story(self):
        for stage in self.stages:
            sub_stage = stage.pick_a_sub_stage()
            for txt in sub_stage.plot:
                if len(txt) == 3:
                    # Challenge
                    if txt[0] == 'C':
                        if txt in self.challenges.keys():
                            self.challenges[txt].run_challenge()
                    # Blank
                    elif txt[0] == 'B':
                        if txt in self.blanks.keys():
                            word = self.blanks[txt].fill_in_the_blank()
                            print(word, end='')
                else:
                    print(txt, end='')

    # Load a story from a json file. It's a nice to have
    def load_story(self):
        pass

    # Nice to have
    def add_question(self, question_key, question_text):
        pass

    def add_blank(self, blank_key, words, keep_initial_word=True):
        self.blanks['B' + blank_key] = Blank(words=words, keep_initial_word=keep_initial_word)

    def add_blank_random(self, blank_key, w_type, keep_initial_word=True):
        self.blanks['B' + blank_key] = Blank(w_type=w_type, random_word=True, keep_initial_word=keep_initial_word)

    def add_challenge_multiple_choice(self, challenge_key, challenge_text, options):
        self.challenges['C' + challenge_key] = Challenge(challenge_text=challenge_text, options=options)

    def add_challenge_location_based(self, challenge_key, challenge_text, location):
        self.challenges['C' + challenge_key] = Challenge(challenge_text=challenge_text, location=location)

    def add_challenge_text_input(self, challenge_key, challenge_text):
        self.challenges['C' + challenge_key] = Challenge(challenge_text=challenge_text)

    def add_stage(self, stage):
        self.stages.append(stage)

    def setup(self):
        self.add_blank('00', ['interesting', 'wise'])
        self.add_blank_random('01', 'adjective')

        self.add_challenge_text_input('00', 'What is the capital of Bavaria?')
        self.add_challenge_multiple_choice('01', 'would you like to do A or B?', ['A', 'B'])
        self.add_challenge_location_based('02', 'Go to Marienplatz!', 'marien_platz')

        intro = Stage()
        intro.add_sub_stage([

            'Hello \n',
            'Welcome to this story \n',
            'C00',
            'What a ~B00~ answer! \n',
            'I feel very ~B01~ today \n',
        ], 'location one')

        self.add_stage(intro)

            'Hello',
            'Welcome to this story',
            '~challenge:00~',
            'What a ~blank:00~ answer!',
            'I feel very ~blank:01~ today',
        ])



    # @staticmethod
    # def setup():
    #     # Creating the intro
    #     intro = SubStage()
    #
    #     intro.add_blank(blank_key='B1', words=['beautiful', 'ugly'])
    #     intro.add_blank(blank_key='B2', w_type='adjective', random_word=True)
    #
    #     intro.add_user_input(input_key='I1', name='Question name')
    #     intro.add_user_input(input_key='I2', q_type='multiple choice', scenario_mapping=dict(A='scenario1', B='scenario2'),
    #                          weight=1)
    #
    #     intro.plot = ['Hello, how are you doing in this ',
    #                   'B1',
    #                   ' day?',
    #                   'I1',
    #                   'Oh I am very ',
    #                   'B2',
    #                   ' that you are doing ',
    #                   'A1',
    #                   '\nWould you like to do A or B?',
    #                   'I2',
    #                   'Some more text\n']
    #
    #     story.chapters.append(Stage([intro]))
    #
    #     # Creating two more scenarios
    #
    #     scenario1 = SubStage()
    #     scenario1.plot = ['PLOT A']
    #     scenario1.name = 'scenario1'
    #     scenario2 = SubStage()
    #     scenario2.plot = ['PLOT B']
    #     scenario2.name = 'scenario2'
    #
    #     story.chapters.append(Stage([scenario1, scenario2]))

class Stage:
    def __init__(self):
        self.end = False
        self.beginning = False
        self.sub_stages = []
        self.sub_stage_probabilities = []

    def add_sub_stage(self, plot):
        self.sub_stages.append(plot)

    # def get_next_scenario(self, user_inputs):
    #     next_scenario = SubStage()
    #     if user_inputs is not None:
    #         for user_input in user_inputs.values():
    #             # Multiple Choice
    #             if user_input.q_type == 'multiple choice':
    #                 for c, scenario in enumerate(self.scenarios):
    #                     scenario_picked_by_user = user_input.scenario_mapping[user_input.answer]
    #                     if scenario_picked_by_user == scenario.name:
    #                         self.scenario_probabilities[c] += user_input.weight
    #
    #         next_scenario = self.scenarios[np.argmax(self.scenario_probabilities)]
    #
    #     else:
    #         next_scenario = random.choice(self.scenarios)
    #     return next_scenario


class SubStage:
    def __init__(self, sub_stage_name, plot, location):
        self.sub_stage_name = sub_stage_name
        self.plot = plot  # array of stings!
        self.location = location

    # # This function can later used to add blanks from a dictionary or Wikipedia!
    # def add_blank(self, blank_key, name='', w_type='', words=None, random_word=False):
    #     self.blanks[blank_key] = Blank(name=name, words=words, w_type=w_type, random_word=random_word)
    #
    # def add_user_input(self, input_key='', name='', q_type='', scenario_mapping=None, weight=0, answer=''):
    #     self.user_inputs[input_key] = UserInput(name=name, q_type=q_type, scenario_mapping=scenario_mapping, weight=weight,
    #                                             answer=answer)
    #
    # def store_user_answer(self, input_key, answer):
    #     self.user_inputs[input_key].answer = answer
    #
    # # Replace all blank.name for a word from the blank.words list in the plot
    # def fill_in_the_blank(self, blank_key):
    #     word = ''
    #     if blank_key in self.blanks.keys():
    #         if self.blanks[blank_key].random_word:
    #             word = get_random_word(self.blanks[blank_key].w_type)
    #         else:
    #             word = random.choice(self.blanks[blank_key].words)
    #     return word
    #
    # def run_scenario(self):
    #
    #     for txt in self.plot:
    #         if len(txt) == 2:
    #             # Input
    #             if txt[0] == 'I' and txt[1].isnumeric():
    #                 input_key = txt
    #                 answer = input("\n> ")
    #                 self.store_user_answer(input_key=input_key, answer=answer)
    #             # Blank
    #             elif txt[0] == 'B' and txt[1].isnumeric():
    #                 blank_key = txt
    #                 blank = self.fill_in_the_blank(blank_key)
    #                 print(blank, end='')
    #             # Answer: Gives back a user input in the text
    #             elif txt[0] == 'A' and txt[1].isnumeric():
    #                 input_key = 'I' + txt[1]
    #                 user_answer = self.user_inputs[input_key].answer
    #                 print(user_answer, end='')
    #         else:
    #             print(txt, end='')
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

#option choice is dependent on: random number, if players succeeded in LAST task, with what probability the outcomes of the previous stages were selected
#option choice returns a PROBABILITY to select a good/bad outcome in substage3
    def determine_substage3(challenge_outcome, prob_array): #challenge outcome is 0 for "failed task" and 1 for "achieved task"
    #prob_array is a list of tuples like [(0.82, "good"), (0.63, "bad")]
        total_val = 0;
        rand_num = round(random.uniform(-1, 1),2);
        good_probability = max(min(challenge_outcome + rand_num, 1), 0); #all calculations performed for probability to get good event
        for el in prob_array:
          if el[1] == "bad":
              val = -1 * el[0];
          else:
              val = el[0];
          total_val = total_val + val;
        good_probability = max(min(good_probability + total_val, 1), 0);
        if (good_probability >= 0.5):
            prob_array.append((good_probability, "good"));
        else:
            prob:array.append((1-good_probability, "bad")); #gets probability for bad event
        return prob_array;

    def generate_random_word():
        adventurer_treasure = ["Crystal Skull", "Monkey Statue", "Stuffed Wolpertinger", "Ancient Porn Magazine", "Long-Lost Martian Technology", "Hoard of Gold", "Creepy Medieval Painting", "Golden Globe", "Holy Grail", "Perpetuum Mobile"];
        adventurer_map = ["Legendary Map", "Ancient Scroll", "Mysterious Hieroglyphs", "Wise GPS System", "Ominous Road Sign", "Misleading Pictogram Panel", "Tacky Compass", "Sarcastic Recommendation", "Letter Of A Lost Lover", "Battered Postcard"]
        sci_fi_thing = ["Sonic Screwdriver", "Flux Capacitative Transcriber", "Bionic Sewing Needle", "Alpha ray excavator", "Chromospheric Sensation Cord", "Cepheid Variability Oscillator", "Ceolostatic Clockwork", "Cybernetic Bottleneck", "Diurnal Dynamite Mug", "Homunculoid Electrowaiver"];
        magic_thing = ["Ring", "Amulet", "Toe ring", "Nose ring", "Earring", "Necklace", "Book", "Staff", "Wand", "Cloak"];
        detective_weapon = ["Shotgun", "Plasma rifle", "Trusty Fists", "Unbreakable Katana Sword", "Machete", "Dagger", "Revolver", "Legendary Broadsword", "Pistol", "Scythe"];

        treasure = random.choice(adventurer_treasure);
        map = random.choice(adventurer_map);
        alien_item = random.choice(sci_fi_thing);
        weapon = random.choice(detective_weapon);


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
    story.dummy_run_story()
