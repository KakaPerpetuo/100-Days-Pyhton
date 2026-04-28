from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Second Task:
question_bank = []
for element in range(len(question_data)):
    ## Fiz direto mas tem como fazer por partes
    question_object = Question(question_data[element]["text"], question_data[element]["answer"])
    question_bank.append(question_object)

quiz = QuizBrain(question_bank)
    
while quiz.still_has_questions():    
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")

# Pode-se usar o site Open Trivia Data Base para conseguir novas perguntas