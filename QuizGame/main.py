from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import random


question_bank = []
for item in question_data:
    question_bank.append(Question(item['question'], item['correct_answer']))


playing = True
while playing:
    random_numbers = []
    while len(random_numbers) < 10:
        q = random.randrange(0, len(question_bank) - 1)
        if not random_numbers.__contains__(q):
            random_numbers.append(q)

    selected_questions = []
    for i in random_numbers:
        selected_questions.append(question_bank[i])

    quiz = QuizBrain(selected_questions)

    while quiz.still_has_question():
        quiz.next_question()

    quiz.print_result()
    if input("Another game (y/n)? ").lower() == 'no':
        playing = False
