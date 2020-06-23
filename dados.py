import matplotlib.pyplot as plt
import cv2
import pickle
from skimage.io import imread, imshow
from skimage.filters import gaussian, threshold_otsu
from skimage import measure
from skimage.measure import label, regionprops, regionprops_table
import math
import matplotlib.pyplot as plt
import numpy as np
from skimage.draw import ellipse
from skimage.morphology import label
from scipy.ndimage import geometric_transform
from random import *
from random import shuffle
import random


def rolagem(d, i, n, s):
  random.seed(a=None, version=2)
  num = randrange(1,d+1)
  s.append(num)
  print("Dado número %d: %d" %(i+1, num))
  if (i == n-1):
    soma(s)

def quantidade(n, dado, s):
  for i in range(n):
    rolagem(dado, i, n, s)

def validar_dado(dado):
  if (dado == 4 or dado == 6 or dado == 8 or dado == 10 or dado == 20 or dado == 100):
    qtd = int(input("Digite a quantidade de dados: "))
    s = []
    quantidade(qtd, dado, s)
  else:
    print("Valor de dado invalido, digite novamente...")
    receber_valor()

def receber_valor():
  dado = int(input("Digite o número de faces para o dado (4, 6, 8, 10, 20 ou 100): "))
  validar_dado(dado)

def soma(s):
  soma_s = 0
  for cada in s:
    soma_s = soma_s + cada
  print("Total dos dados = %d" %soma_s)  

receber_valor()