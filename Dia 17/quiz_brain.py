# Third task:
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        ## Tentar pegar o habito de colocar tudo em variaveis para resumir
        ### Exemplo = current_question = self.question_list[self.question_number]
        ### Evita de escrever variaveis grandes o tempo todo
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ").lower()
        self.check_answer(user_answer, self.question_list[self.question_number].answer)
        self.question_number += 1
    
    # Forth task
    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True
        ## Outro jeito
        # return self.question_number < len(self.question_list) --- Vai retornar True ate o numero ficar maior

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Thats Wrong")
        print(f"The correct answer was: {correct_answer}")
        ## Lembrar que pode-se usar as variaveis da classe qualquer momento dentro da classe
        print(f"Your current score is: {self.score}/{self.question_number + 1}")
        print("\n")
        