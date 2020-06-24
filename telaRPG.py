import PySimpleGUI as sg
from random import *
from random import shuffle
import random
import math
# import winsound
import cv2 
import numpy as np 
from ffpyplayer.player import MediaPlayer
import os

class TelaPython:
  def __init__(self):
    # Layout 
    # (Options: Black, Brownblue, Dark, Dark2, DarkAmber, DarkBrown2, 
    # DarkBrown4, DarkBrown5, DarkGreen, DarkGreen1, DarkPurple4, DarkPurple5, 
    # DarkPurple6, Default, LightBrown13, TealMono)
    sg.change_look_and_feel('TealMono')

    def AventItem(num):
        return [sg.Text(f'{num}.'), sg.In(),]
    layout = [AventItem(x) for x in range(1,9)] + [[sg.Button('Save'), sg.Button('Exit')]]
    window = sg.Window('Listagem dos Aventureiros', layout)
    event, values = window.read()
    lista = []
    for key, value in values.items():
        if value != '':
            lista.append(value)

    layout = [
      [sg.Text('Escolha o número de faces do dado: ', size=(28,0))],
      [sg.Radio('4', 'faces', key='4'),
      sg.Radio('6', 'faces', key='6'), 
      sg.Radio('8', 'faces', key='8'),
      sg.Radio('10', 'faces', key='10'),
      sg.Radio('12', 'faces', key='12'),
      sg.Radio('20', 'faces', key='20'),
      sg.Radio('100', 'faces', key='100')],

      [sg.Text('Quantidade de dados:', size=(20,0))], 
      [sg.Input(size=(3,0), key='qtd')],

      [sg.Text('Aventureiro: ', size=(12,0))], 
      [sg.Combo(lista, size=(30,0), key='player')],

      # Opção de lista pre definida
      # [sg.Combo(['Elfo', 'Humano', 'Meio-Orc'], key='player')],


      [sg.Button('Roll This!')],

      [sg.Output(size=(30,40))]
    ]

    # layout_2 = [[sg.Image(r'C:\\Users\\renoi\\OneDrive\\Documentos\\RPG\\CODE\\monsters.png')]]

    # Window
    self.window = sg.Window('Roll the dices!', size=(350,700)).layout(layout)


  def Init(self):
    while True:
      # Extract
      self.button, self.values = self.window.Read()
      
      # Video
      currDir = os.path.dirname(__file__)
      mediaDir = os.path.join(currDir, 'media')
      videoPath = os.path.join(mediaDir, 'dices_2.mp4')
      def PlayVideo(videoPath):
          video=cv2.VideoCapture(videoPath)
          player = MediaPlayer(videoPath)
          while True:
              grabbed, frame=video.read()
              audio_frame, val = player.get_frame()
              if not grabbed:
                  break
              if cv2.waitKey(28) & 0xFF == ord("q"):
                  break
              cv2.imshow("Video", frame)
              if val != 'eof' and audio_frame is not None:
                  #audio
                  img, t = audio_frame
          video.release()
          cv2.destroyAllWindows()
      PlayVideo(videoPath) 

      # # Song
      # winsound.PlaySound("dice_1.wav", winsound.SND_ALIAS)

      d4 = self.values['4']
      d6 = self.values['6']
      d8 = self.values['8']
      d10 = self.values['10']
      d12 = self.values['12']
      d20 = self.values['20']
      d100 = self.values['100']
      
      qtd = self.values['qtd']
      qtd = int(qtd)

      player = self.values['player']

      s = []
      if (d4 == True):
        print("Rolagem do", player)
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
        print("Rolagem do",player)
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
        print("Rolagem do",player)
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
        print("Rolagem do",player)
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

      elif (d12 == True):
        print("Rolagem do",player)
        print(f'{qtd}d12')
        for i in range(qtd):
          random.seed(a=None, version=1)
          num = randrange(1,13)
          s.append(num)
          print("Dado número %d: %d" %(i+1, num))
          if (i == qtd-1):
            soma_s = 0
            for x in s:
              soma_s = soma_s + x
            print("Total dos dados = %d" %soma_s)
            print("\n")

      elif (d20 == True):
        print("Rolagem do",player)
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
        print("Rolagem do",player)
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