from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


questions_bank = []
for data in question_data:
    new_question = Question(q_text=data['text'],
                            q_answer=data['answer'])
    questions_bank.append(new_question)
quiz = QuizBrain(questions_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f'Your final score is {quiz.score}/{quiz.next_question}')