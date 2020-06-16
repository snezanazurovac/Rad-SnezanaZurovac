import data_load
import recnik_turnira
import matplotlib.pyplot as plt


df=data_load.data_load('spojeno.csv')

def turniri_po_mesecima(godina,ime_fajla):
    ime_recnika={}
    #ova funkcija vraca recnik turnira u kome je kljuc ima turnira,a vrednost mesec u kome se turnir odrzava"
    recnik_meseci={'01':'Januar','02':'Februar','03':'Mart','04':'April','05':'Maj','06':'Jun','07':'Jul','08':'Avgust','09':'Septembar','10':'Oktobar','11':'Novembar','12':'Decembar'}
    for row in ime_fajla[1:]:
        if row[1][0:4]==str(godina) and row[2][0:4]!='Davi':
            if row[2] not in ime_recnika:
                ime_recnika[row[2]]=recnik_meseci[row[6][4:6]]
    return ime_recnika

recnik=turniri_po_mesecima(2006,df)
print("Ime turnira","         ","Mesec turnira")
for x in recnik:
    print('{:25}{:25}'.format(x,recnik[x]))

def broj_apt_po_mesecima(recnik_po_mesecima):
    broj_apt_po_mesecima={}
    recnik_meseci={'01':'Januar','02':'Februar','03':'Mart','04':'April','05':'Maj','06':'Jun','07':'Jul','08':'Avgust','09':'Septembar','10':'Oktobar','11':'Novembar','12':'Decembar'}
    for mesec in recnik_meseci:
        broj_turnira=0
        for turnir in recnik_po_mesecima:
            if recnik_po_mesecima[turnir]==recnik_meseci[mesec]:
                broj_turnira+=1
            broj_apt_po_mesecima[recnik_meseci[mesec]]=broj_turnira
    return broj_apt_po_mesecima

atp=broj_apt_po_mesecima(recnik)
print()
print("Mesec","           ","Broj atp turnira")
print("___________________________________")
for x in atp:
    print('{:10}{:15}'.format(x,atp[x]))


#plt.figure(figsize=(10,30))
#recnik=broj_apt_po_mesecima(turniri_po_mesecima(2004,df))
#for x in recnik:
    #plt.bar(x,recnik[x])
    
#plt.show()

        
    



    

