# Functions with outputs
def format_name(f_name, l_name):
    """ Explicacao do que a funcao faz - Docstring """   ## Comecar a fazer isso em toda funcao pra ter o costume
    if f_name == "" or l_name == "":
        return  # -> Return acaba a funao
    formated_f_name = f_name.title()         # Note: .title() formata a string para primeira letra maiuscula: Exemplo
    formated_l_name = l_name.title() 

    return f"{formated_f_name} {formated_l_name}"    ## Tem como retornar print      

