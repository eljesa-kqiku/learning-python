class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q. {self.question_number}: {question.text} (True/False)?")
        self.check_answer(question, ans)

    def check_answer(self, question, answer):
        if answer.lower() == question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Wrong answer")
        print(f"The answer was: {question.answer}.")
        print(f"Your current score is {self.score}/{self.question_number}.\n")

    def print_result(self):
        print("You have completed the quiz!")
        print(f"Your final score: {self.score}/{self.question_number}")

