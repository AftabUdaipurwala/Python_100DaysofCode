from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# PREPARING QUESTION BANK
question_bank = []
for i in range(0, len(question_data)):
    new_q = Question(question_data[i]['question'], question_data[i]['correct_answer'])
    question_bank.append(new_q)

# RUNNING THE QUIZ
quiz = QuizBrain(question_bank)
score = quiz.still_has_questions()

# GET FINAL SCORE
print(f"Quiz Completed !\n Your final score is {quiz.score}/{len(question_bank)}")
