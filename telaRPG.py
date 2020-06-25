# Headers
import PySimpleGUI as sg
from random import *
from random import shuffle
import random
import math
import cv2            # Check https://docs.opencv.org/master/df/d65/tutorial_table_of_content_introduction.html
import numpy as np 
from ffpyplayer.player import MediaPlayer
import os
# from pydub.playback import play
# from pydub import AudioSegment
# import winsound

def PlayVideo(videoPath):
  video = cv2.VideoCapture(videoPath)
  player = MediaPlayer(videoPath)
  while True:
    grabbed, frame = video.read()
    audio_frame, val = player.get_frame()
    if not grabbed:
      break
    if cv2.waitKey(28) & 0xFF == ord("q"):
      break
    cv2.imshow("Video", frame)
    if val != 'eof' and audio_frame is not None:
      img, t = audio_frame              
  video.release()
  cv2.destroyAllWindows()

class TelaPython:
  def __init__(self):
    # Layout 
    layout = [
      [sg.Text('Escolha o layout de tela: ', size = (34, 0), font = ('Arial', 11))],
      [sg.Combo(sg.ListOfLookAndFeelValues(), size=(40, 15))] + [sg.Button('Ok')]
    ]
    window = sg.Window('Bem vindo!', layout)
    theme = window.read()
    nameTheme = theme[1]
    strTheme = nameTheme[0]
    sg.change_look_and_feel(strTheme)

    def AventItem(num):
        return [sg.Text(f'{num}.'), sg.In(font = ('Lucida Handwriting', 11)),]
    layout = [AventItem(x) for x in range(1, 9)] + [[sg.Button('Save')]]
    window = sg.Window('Listagem dos Aventureiros', layout)
    event, values = window.read()
    if (event == 'Save'):
      aventLista = []
      for key, value in values.items():
          if value != '':
              aventLista.append(value)

    layout = [
      [sg.Text('Escolha o número de faces do dado: ', size = (34, 0), font = ('Lucida Calligraphy', 11))],
      [sg.Radio('3', 'faces', key = '3'),
      sg.Radio('4', 'faces', key = '4'),
      sg.Radio('6', 'faces', key = '6'), 
      sg.Radio('8', 'faces', key = '8'),
      sg.Radio('10', 'faces', key = '10'),
      sg.Radio('12', 'faces', key = '12'),
      sg.Radio('20', 'faces', key = '20'),
      sg.Radio('100', 'faces', key = '100')],

      [sg.Text('Quantidade de dados:', size = (20, 0), font = ('Lucida Calligraphy', 11))],
      [sg.Slider(range = (1, 100), default_value = 1,
          size = (34, 8), orientation = 'horizontal',
          font = ('Lucida Calligraphy', 11), key = 'qtd')],

      [sg.Text('Adicional na rolagem:', size = (20, 0), font = ('Lucida Calligraphy', 11))], 
      [sg.Slider(range = (0, 100), default_value = 0,
                size = (34, 8), orientation = 'horizontal',
                font = ('Lucida Calligraphy', 11), key = 'add')],

      [sg.Text('Aventureiro: ', size = (34, 0), font = ('Lucida Calligraphy', 11))], 
      [sg.Combo(aventLista, size = (35, 0), key = 'player', font = ('Lucida Handwriting', 11))],

      [sg.Button('Roll This!', key = 'RollThis')],

      [sg.Output(size = (34, 40), font = ('Lucida Handwriting', 11))]
    ]

    # Window
    self.window = sg.Window('Roll the dices!', size = (390, 750)).layout(layout)

  def Init(self):
    # Path definitions
    currDir = os.path.dirname(__file__)
    mediaDir = os.path.join(currDir, 'media')
    videoPath = os.path.join(mediaDir, 'dices_2.mp4')

    while True:
      # Extract
      self.button, self.values = self.window.Read()

      # # Video
      PlayVideo(videoPath)

      # # Song
      # winsound.PlaySound("dice_1.wav", winsound.SND_ALIAS)

      d3 = self.values['3']      
      d4 = self.values['4']
      d6 = self.values['6']
      d8 = self.values['8']
      d10 = self.values['10']
      d12 = self.values['12']
      d20 = self.values['20']
      d100 = self.values['100']
      
      qtd = self.values['qtd']
      qtd = int(qtd)

      add = self.values['add']

      player = self.values['player']
      if player != '':
        print(f"{player} rolou: ")
      else:
        print("Rolagem simples: ")

      s = []
      if (d3 == True):
        if add != 0:
          add = int(add)
          print(f'{qtd}d3 + {add}')
        else:
          print(f'{qtd}d3')
        for i in range(qtd):
          random.seed(a = None, version = 20)
          num = randrange(1, 4)
          s.append(num)
          print(f"Dado número {i+1}: {num}")
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x

      elif (d4 == True):
        if add != 0:
          add = int(add)
          print(f'{qtd}d4 + {add}')
        else:
          print(f'{qtd}d4')
        for i in range(qtd):
          random.seed(a = None, version = 20)
          num = randrange(1, 5)
          s.append(num)
          print(f"Dado número {i+1}: {num}")
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x

      elif (d6 == True):
        if add != 0:
          add = int(add)
          print(f'{qtd}d6 + {add}')
        else:
          print(f'{qtd}d6')
        for i in range(qtd):
          random.seed(a = None, version = 10)
          num = randrange(1, 7)
          s.append(num)
          print(f"Dado número {i+1}: {num}")
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x

      elif (d8 == True):
        if add != 0:
          add = int(add)
          print(f'{qtd}d8 + {add}')
        else:
          print(f'{qtd}d8')
        for i in range(qtd):
          random.seed(a = None, version = 21)
          num = randrange(1, 9)
          s.append(num)
          print(f"Dado número {i+1}: {num}")
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x

      elif (d10 == True):
        if add != 0:
          add = int(add)
          print(f'{qtd}d10 + {add}')
        else:
          print(f'{qtd}d10')
        for i in range(qtd):
          random.seed(a = None, version = 1)
          num = randrange(1, 11)
          s.append(num)
          print(f"Dado número {i+1}: {num}")
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x

      elif (d12 == True):
        if add != 0:
          add = int(add)
          print(f'{qtd}d12 + {add}')
        else:
          print(f'{qtd}d12')
        for i in range(qtd):
          random.seed(a = None, version = 1)
          num = randrange(1, 13)
          s.append(num)
          print(f"Dado número {i+1}: {num}")
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x

      elif (d20 == True):
        if add != 0:
          add = int(add)
          print(f'{qtd}d20 + {add}')
        else:
          print(f'{qtd}d20')
        for i in range(qtd):
          random.seed(a = None, version = 4)
          num = randrange(1, 21)
          s.append(num)
          print(f"Dado número {i+1}: {num}")
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x

      elif (d100 == True):
        if add != 0:
          add = int(add)
          print(f'{qtd}d100 + {add}')
        else:
          print(f'{qtd}d100')
        for i in range(qtd):
          random.seed(a = None, version = 3)
          num = randrange(1, 101)
          s.append(num)
          print(f"Dado número {i+1}: {num}")
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x

      if add != 0:
        soma_n = soma_s + add  
        print(f"Total dos dados = {soma_s} + ({add}) = {soma_n}")
        print("\n")
      else:
        print(f"Total dos dados = {soma_s}")
        print("\n") 

screen = TelaPython()
screen.Init()