import data_load
import matplotlib.pyplot as plt
import numpy as np

df=data_load.data_load('spojeno.csv')
# ova funkcija vraca recnik  kluc je vrsta podloge na kojoj se turnir igra i broj odigranih turnira na podlozi
def podloge(godina,naziv_fajla=df):
    atp_podloge={}
    for row in df[1:]:
         if row[1][0:4]==str(godina):
             if row[2][0:4]!='Davi':
                 atp_podloge[row[2]]=row[3]
    lista_turnira=[]
    for x in atp_podloge:
        if atp_podloge[x] not in lista_turnira:
            lista_turnira.append(atp_podloge[x])
    podloge_broj={}
    for x in lista_turnira:
        broj=0
        for turnir in atp_podloge:
            if atp_podloge[turnir]==x:
                broj+=1
        podloge_broj[x]=broj
    return podloge_broj

