class QuizBrain:
    # INITIALIZING THE CLASS
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    # TODO 1 : ASKING THE QUESTIONS
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}. {question.text} ? (True/False)  : ').lower()
        self.check_answer(answer, question.answer)

    # TODO 2 : CHECKING IF THE ANSWER WAS CORRECT
    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print(f"You Got it right !, your score is {self.score}/{self.question_number}")
        else:
            print(f"You got it wrong !, your score is {self.score}/{self.question_number} ")
        return self.score

    # TODO 3 : CHECKING IF WE WERE AT THE END OF THE QUIZ
    def still_has_questions(self):
        while self.question_number < len(self.question_list):
            self.next_question()
