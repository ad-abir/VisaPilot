import json
import random
import os

class SpeechHandler:
    def __init__(self):
        # Load data from the data folder (adjusted path to reach root)
        data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'interview_data.json')
        with open(data_path, 'r') as f:
            data = json.load(f)
        self.greetings = data['greetings']
        self.questions = data['questions']

    def get_script(self):
        # Generate a script: one random greeting + 5 random questions
        greeting = random.choice(self.greetings)
        questions = random.sample(self.questions, min(5, len(self.questions)))
        return {
            'greeting': greeting,
            'questions': questions
        }