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

random.seed(a=None, version=2)
person = []
race = ["Anão","Elfo","Meio-Elfo","Halfling","Humano","Draconato","Gnomo","Meio-Orc","Tiefling","Aarakocra","Aasimar","Aviano","Bugbear","Etergênito","Feral"]
random.shuffle(race)
# print(race)
# num = 0
num = randrange(0,15)
# print(num)
# print(race[num])
person = race[num]

if race[num] == "Anão":
  race_anao = [" da Colina", " da Montanha"]
  aux = randrange(0,2)
  person = person + race_anao[aux]

elif race[num] == "Elfo":
  race_elfo = [" Alto", " da Floresta", " Negro"]
  aux = randrange(0,3)
  person = person + race_elfo[aux]

elif race[num] == "Halfling":
  race_hal = [" de Pés Leves", " Robusto"]
  aux = randrange(0,2)
  person = person + race_hal[aux]

elif race[num] == "Gnomo":
  race_gno = [" da Floresta", " das Rochas"]
  aux = randrange(0,2)
  person = person + race_gno[aux]

elif race[num] == "Tiefling":
  race_tie = [" Infernal", " Abissal"]
  aux = randrange(0,2)
  person = person + race_tie[aux]

elif race[num] == "Aasimar":
  race_aas = [" Protetor", " Flagelo", " Caído"]
  aux = randrange(0,3)
  person = person + race_aas[aux]

elif race[num] == "Aviano":
  race_avi = [" Íbis", " Falcão"]
  aux = randrange(0,2)
  person = person + race_avi[aux]

elif race[num] == "Feral":
  race_fer = [" Pele de Besta", " Caminhar no Penhasco", " Passo Largo", " Dente Longo", " Garra de Navalha", " Caçador Selvagem"]
  aux = randrange(0,6)
  person = person + race_fer[aux]

# print(person)
random.seed(a=None, version=2)
clas = ["Bárbaro","Bardo","Clérico","Druida","Lutador","Monge","Paladino","Caçador","Ladino","Feiticeiro","Bruxo","Mago"]
random.shuffle(clas)
num = randrange(0,12)
person = person + ", " + clas[num]

if clas[num] == "Bárbaro":
  clas_barb = [": o Berserker", ": o Totem Guerreiro"]
  aux = randrange(0,2)
  person = person + clas_barb[aux]

elif clas[num] == "Bardo":
  clas_bard = [": o Lore", ": o Valor"]
  aux = randrange(0,2)
  person = person + clas_bard[aux]

elif clas[num] == "Clérico":
  clas_cle = [" do Conhecimento", " da Vida", " da Luz", " da Natureza", " da Tempestarde", " da Trapaça", " da Guerra"]
  aux = randrange(0,7)
  person = person + clas_cle[aux]

elif clas[num] == "Druida":
  clas_dru = [" da Terra", " da Lua"]
  aux = randrange(0,2)
  person = person + clas_dru[aux]

elif clas[num] == "Lutador":
  clas_lut = [" Campeão", " Mestre de Batalha", " Cavaleiro de Eldritc"]
  aux = randrange(0,3)
  person = person + clas_lut[aux]

elif clas[num] == "Monge":
  clas_mon = [" Modo Mãos Livres", " Modo Sombra", " Modo Quatro Elementos"]
  aux = randrange(0,3)
  person = person + clas_mon[aux]

elif clas[num] == "Paladino":
  clas_pala = [" Juramento de Devoção", " Jurado aos Anciões", " Juramento de Vingança"]
  aux = randrange(0,3)
  person = person + clas_pala[aux]

elif clas[num] == "Caçador":
  clas_ca = [": Cão de Caça", ": Mestre das Feras"]
  aux = randrange(0,2)
  person = person + clas_ca[aux]


elif clas[num] == "Ladino":
  clas_lad = [" Criminoso", " Assassino", " Trapaceiro Arcano"]
  aux = randrange(0,3)
  person = person + clas_lad[aux]

elif clas[num] == "Feiticeiro":
  clas_feit = [" de Linhagem Dracônica", " de Magia Selvagem"]
  aux = randrange(0,2)
  person = person + clas_feit[aux]

elif clas[num] == "Bruxo":
  clas_brux = [" Archfey", " Fanático", " Ancião"]
  aux = randrange(0,3)
  person = person + clas_brux[aux]

elif clas[num] == "Mago":
  clas_mag = [" Abjuração", " Conjuração", " Adivinhação", " Encantamento", " Evocação", " Ilusão", " Necromancia", " Transmutação"]
  aux = randrange(0,8)
  person = person + clas_mag[aux]

print(person)