import random

QUIZ = [
    {"chat": "Let's team up! Drop in Pochinki?", "answer": "PUBG"},
    {"chat": "You're sus, Red!", "answer": "Among Us"},
    {"chat": "Triple word score, boom!", "answer": "Words With Friends"},
]

def get_random_question():
    return random.choice(QUIZ)
