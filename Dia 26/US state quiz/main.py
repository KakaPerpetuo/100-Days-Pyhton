import turtle
import pandas
from write_country_names import Country_names

screen = turtle.Screen()
screen.title("U.S. States Game")

# Forma de colocar uma imagem na tela
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

## Funcao para mostrar qual a coordenada do local que vc clicar na tela
#def get_mouse_click_coor(x, y):
#    print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

write_states = Country_names()
states_info = pandas.read_csv("50_states.csv")
state_name_lists = states_info['state'].to_list()
correct_guess_list = []
score = 0

game_is_on = True

# Tinha como fazer o loop direto, len(lista de estados) < 49
while game_is_on:
	# Em vez do score tinha como usar o tamanho da lista de respondidos
	# .title() -> Coloca string na formatacao: Amor, Banana, Etc...
    answer_state = screen.textinput(title = f"{score}/49 State Correct", prompt= "What's another state's name?").title()

    if answer_state == "Exit":

        states_missed = [state for state in state_name_lists if state not in correct_guess_list]
        states_to_learn = pandas.DataFrame(states_missed)
        states_to_learn.to_csv("states_to_learn.csv")

        game_is_on = False

    for state in state_name_lists:
        if state == answer_state and state not in correct_guess_list:
            actual_state = states_info[states_info.state == state]
            # Values[0] -> retorna o valor cru
            correct_guess_list.append(state)
            # Tbm funciona se eu apenas tranforma as informacoes em int
            # Funcao item() da biblioteca Pandas retorna o primeiro elemento de uma linha
            x = actual_state["x"].values[0]
            y = actual_state["y"].values[0]
            write_states.write_country(x= x, y= y, country= state)
            score += 1
        
        if len(state_name_lists) == len(correct_guess_list):
            game_is_on = False
