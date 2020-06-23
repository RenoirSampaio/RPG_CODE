import PySimpleGUI as sg
from random import *
from random import shuffle
import random
import math

class TelaPython:
  def __init__(self):
    # Layout
    sg.change_look_and_feel('DarkPurple4')
    layout = [
      [sg.Text('Escolha o número de faces do dado: ', size=(28,0))],

      [sg.Radio('4', 'faces', key='4'),
      sg.Radio('6', 'faces', key='6'), 
      sg.Radio('8', 'faces', key='8'),
      sg.Radio('10', 'faces', key='10'),
      sg.Radio('20', 'faces', key='20'),
      sg.Radio('100', 'faces', key='100')],

      [sg.Text('Quantidade de dados:', size=(20,0)), sg.Input(size=(3,0), key='qtd')],

      [sg.Button('Roll This!')],
      [sg.Output(size=(30,40))]
    ]

    # Window
    self.window = sg.Window('Roll the dices!', size=(300,700)).layout(layout)


  def Init(self):
    while True:
      # Extract
      self.button, self.values = self.window.Read()

      d4 = self.values['4']
      d6 = self.values['6']
      d8 = self.values['8']
      d10 = self.values['10']
      d20 = self.values['20']
      d100 = self.values['100']
      
      qtd = self.values['qtd']
      qtd = int(qtd)


      s = []
      if (d4 == True):
        print(f'{qtd}d4')
        for i in range(qtd):
          random.seed(a=None, version=20)
          num = randrange(1,5)
          s.append(num)
          print("Dado número %d: %d" %(i+1, num))
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x
            print("Total dos dados = %d" %soma_s)
            print("\n")

      elif (d6 == True):
        print(f'{qtd}d6')
        for i in range(qtd):
          random.seed(a=None, version=10)
          num = randrange(1,7)
          s.append(num)
          print("Dado número %d: %d" %(i+1, num))
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x
            print("Total dos dados = %d" %soma_s)
            print("\n")

      elif (d8 == True):
        print(f'{qtd}d8')
        for i in range(qtd):
          random.seed(a=None, version=21)
          num = randrange(1,9)
          s.append(num)
          print("Dado número %d: %d" %(i+1, num))
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x
            print("Total dos dados = %d" %soma_s)
            print("\n")

      elif (d10 == True):
        print(f'{qtd}d10')
        for i in range(qtd):
          random.seed(a=None, version=1)
          num = randrange(1,11)
          s.append(num)
          print("Dado número %d: %d" %(i+1, num))
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x
            print("Total dos dados = %d" %soma_s)
            print("\n")

      elif (d20 == True):
        print(f'{qtd}d20')
        for i in range(qtd):
          random.seed(a=None, version=4)
          num = randrange(1,21)
          s.append(num)
          print("Dado número %d: %d" %(i+1, num))
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x
            print("Total dos dados = %d" %soma_s)
            print("\n")

      elif (d100 == True):
        print(f'{qtd}d100')
        for i in range(qtd):
          random.seed(a=None, version=3)
          num = randrange(1,101)
          s.append(num)
          print("Dado número %d: %d" %(i+1, num))
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x
            print("Total dos dados = %d" %soma_s)
            print("\n")

screen = TelaPython()
screen.Init()

