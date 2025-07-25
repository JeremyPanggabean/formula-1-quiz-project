from question_model import Question
from data import f1_quiz_data, show_f1_intro
from quiz_brain import QuizBrain

question_bank = []

for question in f1_quiz_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

show_f1_intro()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")