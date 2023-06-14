print('Hi ha 15 preguntes que les has de respondre correctament,per cada pregunta hi ha 3 intents.Si la pregunta es respon correctament es restableixen els intents. Molta sort!')

import random

preguntes = {'Em porten al damunt i cada poble ni te un, que es?':'Gegant', 'És petit, petit,no té cap moneda i diu que és ric,ric.Qué és?':'Llagost','És petit com una nou,porta banyes i no és bou,no té peus,pero es mou.Qué és?':'Caragol','Pel que porta molta pressa m op i tanc i don pas.Com que ja t he dit qui puc ser,Qué soc?':'Porta','Qui és el qui es lleva més de matí del món i de vespre és el primer que es dorm?':'Sol','Quin més pot fer un any bisiest?':'Febrer','Origen de la pasta?':'Italia','Qui va ser el creador de Phyton?':'Guido','Quina és la capital de Brasil? ':'Brassilia','Quin és el riu més llarg del món? ':'Nil', 'Quina au possa els ous més grans? ':'Estruç','Quin animal és el més perillòs del món? ':'Hipopotam','Quin animal causa més morts per any? :':'Mosquit','Quin és el sinònim de redò? ':'Ovalat','Quina és la marca de cotxe més popular del món? ':'Tesla'}
x = 0 #(nombre d'intents)
X =2 #(variable global d´intents)
y =0#(nombre de preguntes)
Y = 15 #(variable global de preguntes)
joc= 0
def pintarPista(x, correcte): #s'utilitza per mostrar s'ajuda en els dos primers intents)
  if x == X:
    print(correcte[0] + (('.')*(len(correcte)-2)) + correcte[-1])
  if x == X-1: #si es respon malament amb aquest if surtiràn les pistes, hi ha els menys 2 i menys 1 degut a que es cerquen la primera lletra i la darrera.
    missatge = ''
    i = 0 
    for lletra in correcte:
      if random.randint(0,99) >= 30 and i>0 and i<len(correcte)-1: # el 85% de les vegades es sustitueix sa lletra per punt.
        lletra = '.'
    #És la variable que s'utilitza per a accedir a cadascuna de les lletres de la resposta. Normalment se'n diu índex, d'aquí la lletra i
      i=i+1
      missatge = missatge + lletra
    print(missatge)
x = 1
while y!=Y and joc!= 1: #mentres ses preguntes no arribin a 15, seguiran apareguent preguntes
  x=X
  pregunta = list(preguntes)
  resposta = input(pregunta[y])
  correcte = preguntes[pregunta[y]]
  while resposta != correcte and x != 0:
    pintarPista(x, correcte)
    print('un altre intent')
  
    if x==1:
      print('(Darrera oportunitat)')
    resposta = input(pregunta[y])
    x = x-1
  if x == 0 and resposta != correcte:
    print('Has perdut') 
    print('Joc acabat')
    joc = 1
  if resposta == preguntes[pregunta[y]]:
        print('Correcte')
        y = y+1
  if y>14:
    print('Has guanyat')
