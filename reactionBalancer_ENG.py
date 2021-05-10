#            88         
#            88         
#            88         
# ,adPPYba,  88   ,d8   
#a8"     "8a 88 ,a8"    
#8b       d8 8888[      
#"8a,   ,a8" 88`"Yba,   
# `"YbbdP"'  88   `Y8a  

#--Variabili e librerie utili--#
import random
Stato = 'n' #Variabile che userò per determinare la fine di un ciclo
Contatore1 = 0 #Variabile che userò per contare i cicli
Contatore2 = 0 #Un'altra variabile che userò per contare cicli che avvengo in contemporanea a quelli contati da "Contatore1"

##-------------------------Prelievo input-----------------------------##
#--Determinazione degli elementi della reazione--#
Elementi = [] #Lista degli elementi che reagiranno
while Stato != 'S': #Ciclo di registrazione degli elementi coinvolti
	Elemento = input("What element is present in this equation?")
	Elementi += [Elemento]
	Stato = input("Was this the last element? (Y/n)")
print("In total, here are the elements that you selected:")
print(Elementi)

#--Assegnazione degli atomi alle molecole--#
#Molecole dalla parte sinistra dell'uguale
print("Now you have to insert the molecules present on the left hand side of the equals sign.")
MolecoleSinistra = []
while Stato != 'n': #Ciclo di creazione delle molecole all'interno di "MolecoleSinistra"
	Nome = input("What is the name of this molecule?")
	MolecoleSinistra += [Nome] #Il nome della molecola servirà a fornire l'output della risposta
	Contatore1 = 0
	while Contatore1 < len(Elementi) : #Ciclo di inserimento degli atomi in ogni molecola
		Elemento = input("How many atoms of " + Elementi[Contatore1] + " does this molecule have?") #Riciclo della variabile "Elemento" per contare la quantita di elementi presente in ogni molecola
		MolecoleSinistra += [int(Elemento)]
		Contatore1 += 1
	Stato = input("Is there another molecule to consider? (Y/n)")
print(MolecoleSinistra)

#Molecole dalla parte destra dell'uguale
print("Now you have to insert the molecules present on the right hand side of the equals sign.")
Stato = 'S'
MolecoleDestra = []
while Stato != 'n': #Ciclo di creazione delle molecole all'interno di "MolecoleDestra"
	Nome = input("What is the name of this molecule?")
	MolecoleDestra += [Nome] #Il nome della molecola servirà a fornire l'output della risposta
	Contatore1 = 0
	while Contatore1 < len(Elementi): #Ciclo di inserimento degli atomi in ogni molecola
		Elemento = input("How many atoms of " + Elementi[Contatore1] + " does this molecule have?") #Riciclo della variabile "Elemento" per contare la quantita di elementi presente in ogni molecola
		MolecoleDestra += [int(Elemento)]
		Contatore1 += 1
	Stato = input("Is there another molecule to consider? (Y/n)")
print(MolecoleDestra)

##-------Creazione di funzioni e variabili che serviranno dopo--------##
#--Funzione che calcola il numero totale di elementi presente in una lista--#
def Prelevatore(NumeroElemento, lista):
	Contatore2 = 0
	Prelevatore = NumeroElemento
	ElementiTotali = 0
	while Prelevatore < len(lista):
		Elemento = lista[Prelevatore] #Prelevazione dell'elemento di una molecola dalla lista
		ElementiTotali += Elemento #Somma dell'elemento della molecola agli altri raccolti
		Contatore2 += 1
		Prelevatore = Contatore2 * (len(Elementi) + 1) + NumeroElemento #Passaggio ad un altra molecola
	return ElementiTotali

#--Variabili che rappresentano il numero di molecole contenuto dalle 2 parti dell'uguale--#
NumeroMolecoleSinistra = len(MolecoleSinistra) / (len(Elementi) + 1)
NumeroMolecoleDestra = len(MolecoleDestra) / (len(Elementi) + 1)

##-------------Effettuazione di tentativi di risoluzione--------------##
FattoreMassimo = int(input("What is the maximum coefficient?"))

Stato = 'Attempt failed!'
while Stato == 'Attempt failed!': #Ciclo di generazione e validazione dei tentativi
	#--Generazione di fattori di molecole--#
	FattoriSinistra = []
	Contatore1 = 0
	while Contatore1 < NumeroMolecoleSinistra:
		FattoriSinistra += [random.randint(1, FattoreMassimo)]
		Contatore1 += 1
	FattoriDestra = []
	Contatore1 = 0
	while Contatore1 < NumeroMolecoleDestra:
		FattoriDestra += [random.randint(1, FattoreMassimo)]
		Contatore1 += 1
	#P.S. Mi rendo conto che questo metodo di generazione di fattori è assai rozzo, per questo sono ben accette idee migliori

	#--Creazione di molecole per testare il bilanciamento--#
	#Molecole dalla parte sinistra dell'uguale
	MolecoleVirtualiSinistra = [] #Molecole create per testare il bilanciamento elaborato precedentemente
	Contatore1 = 0
	while Contatore1 < NumeroMolecoleSinistra: #Ciclo di scrittura delle molecole
		MolecoleVirtualiSinistra += [MolecoleSinistra[Contatore1 * (len(Elementi) + 1)]] #Scrittura del nome della molecola nella molecola virtuale
		Contatore2 = 1
		Fattore = FattoriSinistra[Contatore1] #Prelievo del fattore di moltiplicazione della molecola
		while Contatore2 <= len(Elementi): #Ciclo di moltiplicazione di ogni molecola
			MolecoleVirtualiSinistra += [MolecoleSinistra[Contatore1 * (len(Elementi) + 1) + Contatore2] * Fattore] #Riscrittura della quantità dell'elemento moltiplicata per il fattore
			Contatore2 += 1 #Passaggio all'elemento successivo
		Contatore1 += 1 #Passaggio alla molecola successiva
	print(MolecoleVirtualiSinistra)

	#Molecole dalla parte destra dell'uguale
	MolecoleVirtualiDestra = [] #Molecole create per testare il bilanciamento elaborato precedentemente
	Contatore1 = 0
	while Contatore1 < NumeroMolecoleDestra: #Ciclo di scrittura delle molecole
		MolecoleVirtualiDestra += [MolecoleDestra[Contatore1 * (len(Elementi) + 1)]] #Scrittura del nome della molecola nella molecola virtuale
		Contatore2 = 1
		Fattore = FattoriDestra[Contatore1] #Prelievo del fattore di moltiplicazione della molecola
		while Contatore2 <= len(Elementi): #Ciclo di moltiplicazione di ogni molecola
			MolecoleVirtualiDestra += [MolecoleDestra[Contatore1 * (len(Elementi) + 1) + Contatore2] * Fattore] #Riscrittura della quantità dell'elemento moltiplicata per il fattore
			Contatore2 += 1 #Passaggio all'elemento successivo
		Contatore1 += 1 #Passaggio alla molecola successiva
	print(MolecoleVirtualiDestra)

	#--Validazione del lavoro prodotto--#
	Stato = 'Balacing completed successfully!'
	Contatore1 = 1
	while Contatore1 <= len(Elementi): #Ciclo di controllo, elemento per elemento
		if Prelevatore(Contatore1, MolecoleVirtualiSinistra) != Prelevatore(Contatore1, MolecoleVirtualiDestra): #Confronto
			Stato = 'Attempt failed!'
		Contatore1 += 1 #Passaggio all'elemento successivo
	print(Stato)

#--Stampaggio su schermo della risposta--#
Contatore1 = 0
while Contatore1 < NumeroMolecoleSinistra:
	if(Contatore1 != 0):
		print('+ ', sep = '', end = "")
	print(FattoriSinistra[Contatore1], sep = '', end = "")
	print(MolecoleSinistra[Contatore1 * (len(Elementi) + 1)], sep = '', end = "")
	print(' ', sep = '', end = "")
	Contatore1 += 1
print('= ', end = "")
Contatore1 = 0
while Contatore1 < NumeroMolecoleDestra:
	print(FattoriDestra[Contatore1], sep = '', end = "")
	print(MolecoleDestra[Contatore1 * (len(Elementi) + 1)], sep = '', end = "")
	print(' ', sep = '', end = "")
	Contatore1 += 1
