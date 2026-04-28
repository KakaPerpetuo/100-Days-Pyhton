import gameData
import random
import os

def clear():
    """ Funcao pra limpar o terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_random():
    """ Funcao para escolher dois instagrans aleatoriamente"""
    return random.choice(gameData.data)

def compare(insta_a, insta_b):
    """ Funcao para retornar qual insta é o mais seguido"""
    if insta_a['follower_count'] > insta_b['follower_count'] or insta_a['follower_count'] == insta_b['follower_count']:
        return "a"
    else:
        return "b"