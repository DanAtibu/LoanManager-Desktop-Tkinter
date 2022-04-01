#coding: utf-8
import sqlite3 , time , random , os
from datetime import datetime
from tkinter import messagebox

def image(op):
	connex = sqlite3.connect("images.db")
	cursor = connex.cursor()
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS Images(
		id integer PRIMARY KEY NOT NULL,
		nom varchar NOT NULL,
		image  LONGBLOB NOT NULL
		)
		""")
	listeimage = ["3.png","4.png","CREER.png","connexion.png","creeruncompte.png","formulaire.png","icone.ico","movement.png","valider.png"]
	if op == 1:
		for name in listeimage:
			with open(name,"rb") as file:
				filecontent = file.read()
				data = (file.name,filecontent,)
				cursor.execute("INSERT INTO Images (nom,image) VALUES(?,?)",data)
				connex.commit()
	elif op == 2:
		data = cursor.execute("SELECT * FROM Images")
		data = data.fetchall()
		i = 0
		for name in listeimage:
			with open(data[i][1],"wb") as file:
				filecontent = file.write(data[i][2])
			i += 1

	connex.close()
def connexion():
	user =str(os.getlogin())
	connexion_database = sqlite3.connect(f"C:/Users/{user}/Documents/DataBaseLoanManager.db")
	#print("fait...")
	manager = connexion_database.cursor()
	return connexion_database,manager

def CreateTables():
	user =str(os.getlogin())
	connexion = sqlite3.connect(f"C:/Users/{user}/Documents/DataBaseLoanManager.db")
	cursor = connexion.cursor()
	ClientInformations = """
	CREATE TABLE IF NOT EXISTS ClientInformations(
	Id_Client integer PRIMARY KEY NOT NULL,
	Name varchar NOT NULL, 
	PostName varchar NOT NULL,
	Prename varchar NOT NULL,
	Sexe varchar NOT NULL,
	Etat_Civil varchar NOT NULL,
	Profession varchar NOT NULL,
	NumberPhone varchar NOT NULL,
	ApprovisionementExterieur smallint NOT NULL,
	Vile varchar NOT NULL,
	Quatier varchar NOT NULL,
	Avenu varchar NOT NULL,
	NumHome smallint not null,
	Unit_Day int NOT NULL,
	Msg_Day int NOT NULL,
	Megabyte_Day int NOT NULL,
	Payout_per varchar NOT NULL,
	Way_payout varchar NOT NULL
	);
	"""
	MouvementCapital = """
	CREATE TABLE IF NOT EXISTS MouvementCapital(
	Airtel_Unit INT NOT NULL,
	Vodacom_Unit INT NOT NULL,  
	Orage_Unit INT NOT NULL,
	Airtel_loan INT NOT NULL,
	Vodacom_loan INT NOT NULL,
	Orage_loan INT NOT NULL
	)
	"""

	tableauoperationgenerales = """
	CREATE TABLE IF NOT EXISTS tableauoperationgenerales(
	Id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	Id_Client int NOT NULL,
	DateDo DATE NOT NULL, 
	heure varchar NOT NULL,
	Quantité_Units int NOT NULL,
	Quantité_mega int NOT NULL,
	Quantité_Megabyte int NOT NULL,
	Montant int NOT NULL,
	Echeance DATE NOT NULL,
	operation varchar NOT NULL,
	way_Paiement int NOT NULL, 
	Reseau varchar not null
	);
	"""
	Dettetable = """
	CREATE TABLE IF NOT EXISTS Dettetable(
	Id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	Id_Client integer NOT NULL,
	Echeance date not null
	)
	"""
	CreateTableCountSoft = """
	CREATE TABLE IF NOT EXISTS CreateTableCountSoft(
	Id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
	UserName varchar NOT NULL, 
	PassWord varchar NOT NULL,
	NumberCompte smallint NOT NULL,
	ForgetRecover varchar NOT NULL
	);
	"""
	cursor.execute(ClientInformations)
	cursor.execute(MouvementCapital)
	cursor.execute(tableauoperationgenerales)
	cursor.execute(Dettetable)
	cursor.execute(CreateTableCountSoft)
	datas = cursor.execute(f"SELECT * FROM MouvementCapital")
	if datas.fetchone() == None:
		data = (0,0,0,0,0,0,)
		montant_now = "INSERT INTO MouvementCapital (Airtel_Unit,Vodacom_Unit,Orage_Unit,Airtel_loan,Vodacom_loan,Orage_loan) VALUES (?,?,?,?,?,?)"
		cursor.execute(montant_now,data)
		connexion.commit()
	connexion.close()

class account():
	def __init__(self):
		pass

	def connexion(): 
		user =str(os.getlogin())
		connexion_database = sqlite3.connect(f"C:/Users/{user}/Documents/DataBaseLoanManager.db")
		manager = connexion_database.cursor()
		return connexion_database,manager

	def connexioncount(self,count,pssw,poste):
		cnnx , cursor = connexion()
		datas = (count,pssw,poste)
		cmd = """
		SELECT * FROM CreateTableCountSoft WHERE UserName = ? AND PassWord = ? AND NumberCompte = ?
		"""
		counts = cursor.execute(cmd,datas)
		resultat = counts.fetchall()
		if len(resultat) != 0:
			if resultat[0][3] == "Administrateur":
				return 1
			elif resultat[0][3] == "Facturier":
				return 2
			else:
				return 0
		else:
			return 0

	def Saveancount(self,count,pssw,poste,recove):
		datas = (count,pssw,poste,recove)
		#print(datas)
		if "" not in datas and poste in ("Administrateur","Facturier"):
			reponse = messagebox.askyesno("Confirmation","Voulez Vous Ajouter Le Compte ?")
			if reponse == True:
				cnnx , cursor = connexion()
				cmd = """
				INSERT INTO CreateTableCountSoft (UserName,PassWord,NumberCompte,ForgetRecover) 
				VALUES (?,?,?,?)
				"""
				cursor.execute(cmd,datas)
				cnnx.commit()
		else:
			messagebox.showerror("Formulaire Incorrecté "," Données Refusées ?")
	Saveancount = classmethod(Saveancount)
	def alldata(self):
		cnnx , cursor = connexion()
		r = cursor.execute("SELECT * FROM CreateTableCountSoft")
	alldata = classmethod(alldata)
	def Recovecount():
		pass

class Client:
	def __init__(self):
		pass

	def SaveClient(self,Informations):
		connect , cursor = connexion()
		Id_now = cursor.execute("SELECT Id_Client FROM ClientInformations")
		Id_Random = random.randint(1000,10000)
		Id_now = [i[0] for i in Id_now.fetchall()]
		while Id_Random in Id_now:
			Id_Random = random.randint(1000,10000)
		Informations = (Id_Random,) + Informations
		#print(Informations) 
		cursor.execute("INSERT INTO ClientInformations (Id_Client,Name,PostName,Prename,Sexe,Etat_Civil,Profession,NumberPhone,ApprovisionementExterieur,Vile,Quatier,Avenu,NumHome,Unit_Day,Msg_Day,Megabyte_Day,Payout_per,Way_payout) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",Informations)
		connect.commit()
		connect.close()
		return Id_Random
	SaveClient = classmethod(SaveClient)

	def ShowInformationsAboutAllClient(self):
		connect , cursor = connexion() #connexion au file.db à partir d'une fonction deja faite
		cursor.execute("SELECT * FROM ClientInformations")
		#for info in cursor.fetchall():
		#	print(info)
		return cursor.fetchall()
	ShowInformationsAboutAllClient = classmethod(ShowInformationsAboutAllClient)

	def ShowInformationsAboutClient(self,Id_Reseach):#Id_Reseach
		Id_Reseach = (Id_Reseach,)
		connect , cursor = connexion() #connexion au file.db à partir d'une fonction deja faite
		cursor.execute("SELECT * FROM ClientInformations WHERE Id_Client = (? )",Id_Reseach)
		ClientInfos = cursor.fetchall()
		try:
			corp = f"""\nID : {ClientInfos[0][0]}\nNom : {ClientInfos[0][1]}\nPost Nom : {ClientInfos[0][2]}\nPrenom : {ClientInfos[0][3]}\nSexe : {ClientInfos[0][4]}\nEtat Civil : {ClientInfos[0][5]}\nProfession : {ClientInfos[0][6]}\nTelephone : {ClientInfos[0][7]}\nVendeur : {ClientInfos[0][8]}\nVille : {ClientInfos[0][9]}\nQuartier : {ClientInfos[0][10]}\nAvenue : {ClientInfos[0][11]}\nN° : {ClientInfos[0][12]}\nUnité/jour : {ClientInfos[0][13]}\nMsg/jour : {ClientInfos[0][14]}\nMega/jour: {ClientInfos[0][15]}\nMode de payment    : {ClientInfos[0][16]}\nMoyen de Payement : {ClientInfos[0][17]}\n"""
			given = str.upper(ClientInfos[0][1])
			messagebox.showinfo(f"Informations About {given} ",corp)
		except:
			messagebox.showerror("Erreur Recheche","Aucune Donnée Sur la Personne !")
		finally:
			connect.close()
	ShowInformationsAboutClient = classmethod(ShowInformationsAboutClient)

	def ClientHistorique(self,Id_Histor):
		if Id_Histor != "":
			try : 
				connex , cursor = connexion()	
				cursor.execute(f"SELECT * FROM tableauoperationgenerales WHERE Id_Client = {Id_Histor}")
				data = cursor.fetchall()
				connex.close()
				return data
			except:
				return data
		else:
			messagebox.showerror("Compte Introuvable !",f"La personne n'existe pas svp !")
			return []
	ClientHistorique = classmethod(ClientHistorique)
	def DeleteClient(self,Informations):
		Informations = (Informations , )
		connect , cursor = connexion() #connexion au file.db à partir d'une fonction deja faite
		Id_del = cursor.execute("SELECT Id_Client,Name,PostName,Prename FROM ClientInformations WHERE Id_Client = (?)",Informations)

		try:
			personne = Id_del.fetchone()
			reponse = messagebox.askyesno("Suppresion",f"Suppimer [ {personne[1]} {personne[2]} {personne[3]} ]")
			#print(reponse)
			if reponse == True:
				cursor.execute("DELETE FROM ClientInformations WHERE Id_Client = (?)",Informations)
				connect.commit()
		except Exception as erreur:
			messagebox.showerror("Compte Introuvable !",f"La personne n'existe pas svp !")
		finally:
			connect.close()
class produit:
	def __init__(self):
		pass
	def saveoperation(self,listeelement):
		for element in [listeelement[3],listeelement[4],listeelement[5],listeelement[6]]:
			liste = ["-","A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","%","W","X","C","V","B","N","?",".","/","<",">","&","(",'"',"!","_","ç"," ","à","@","{","}",";",":","=","a","z","e","r","y","u","i","o","p","^","m","l","k","h","j","g","f","d","s","q","w","x","c","v","b","n",",",""]
			for lettre in element:
				if lettre in liste:
					messagebox.showerror("Incorrect Code","Verifié Vos Données")
					return False
		def aftercheking():
			cmd = """
			INSERT INTO tableauoperationgenerales (Id_Client,DateDo,heure,Quantité_Units,Quantité_mega,Quantité_Megabyte,Montant,Echeance,operation,way_Paiement,Reseau) 
			VALUES (?,?,?,?,?,?,?,?,?,?,?)
			"""
			cursor.execute(cmd,listeelement)
			cnnex.commit()
			messagebox.showinfo("Donnée","Operation Réussie !")
		cnnex , cursor = connexion()
		idnow = cursor.execute("SELECT Id_Client FROM ClientInformations")
		idnow = idnow.fetchall()
		idnow = [ str(people[0]) for people in idnow]
		produi = produit()
		if listeelement[8] in ["Emprunt","Rembourcement"]:
			if "" not in listeelement:
				if listeelement[0] in idnow:
					if listeelement[8] == "Emprunt":
						if produi.Updatestock(str(listeelement[10]+"_Unit"),int(listeelement[3]),"-") == True:
							produi.Updatestock(str(listeelement[10]+"_loan"),int(listeelement[3]),"+")
							datafiltre = (listeelement[0] , listeelement[7],) 
							cursor.execute("INSERT INTO Dettetable (Id_Client,Echeance) VALUES(?,?)",datafiltre)
							aftercheking()
					elif listeelement[8] == "Rembourcement":
						if produi.Updatestock(str(listeelement[10]+"_loan"),int(listeelement[3]),"-") == True:
							aftercheking()
				else:
					messagebox.showerror("Incorrect Code","Donnée Non Trouvée !")
					cnnex.close()
					return False
			else:
				messagebox.showerror("Incorrect Code","Données Incompletes")
				return False
		elif listeelement[8] == "vente":
			if listeelement[0] != "":
				if listeelement[0] in idnow:
					if produi.Updatestock(str(listeelement[10]+"_Unit"),int(listeelement[3]),"-") == True:
						aftercheking()
				else:
					messagebox.showerror("Incorrect Code","Donnée Non Trouvée !")
			else:
				for i in range(1,11):
					if listeelement[i] == "":
						messagebox.showerror("Incorrect Code","Donnée Non Trouvée !")
						cnnex.close()
						return False
				if produi.Updatestock(str(listeelement[10]+"_Unit"),int(listeelement[3]),"-") == True:
					aftercheking()
		elif listeelement[8] == "approvissionement":
			if produi.Updatestock(str(listeelement[10]+"_Unit"),int(listeelement[3]),"+") == True:
				messagebox.showinfo("Succes ","Opération D'Approvissionement Réussie !")
				aftercheking()
			else:
				messagebox.showerror("Erreur","Verifier Vos Données Entrées !")
		else:
			messagebox.showerror("Erreur","Verifier Vos Données Entrées !")
		cnnex.close()
	saveoperation = classmethod(saveoperation)
	def viewdayoper(self,element_db,colonne_db,choiceop):
		date = datetime.now()
		date = str(date).split(".")
		date = date[0].split()
		date = (date[0],)
		cnnx , cursor = connexion()
		self.element = element_db
		self.colonne = colonne_db
		if choiceop == 1:
			unit = cursor.execute(f"SELECT {self.element} FROM tableauoperationgenerales WHERE {self.colonne} = (?)",date)#date
			unit = unit.fetchall()
			sommation = 0
			for value in unit:
				if value[0] != "":
					sommation = int(value[0]) + sommation
			cnnx.close()
			return len(unit) , sommation
		elif choiceop == 2:
			unit = cursor.execute(f"SELECT {self.element} FROM {self.colonne}")
			unit = unit.fetchall()
			cnnx.close()
			return unit[0]
		elif choiceop == 3:
			unit = cursor.execute(f"SELECT * FROM {self.colonne}")
			#print(unit.fetchall())

	viewdayoper = classmethod(viewdayoper)
	def Updatestock(self,colonne_db,data,signe):
		cnnx , cursor = connexion()
		if signe == "+":
			montant_now = cursor.execute(f"SELECT {colonne_db} FROM MouvementCapital")
			montant_reel = montant_now.fetchone()[0]
			cursor.execute(f"UPDATE MouvementCapital SET {colonne_db} = {data+montant_reel}")
			cnnx.commit()
			cnnx.close()
			return True
		elif signe == "-":
			montant_now = cursor.execute(f"SELECT {colonne_db} FROM MouvementCapital")
			montant_reel = montant_now.fetchone()[0]
			if montant_reel > data or montant_reel == data:
				cursor.execute(f"UPDATE MouvementCapital SET {colonne_db} = {montant_reel-data}")
				cnnx.commit()
				cnnx.close()
				return True 
			elif montant_reel == 0:
				messagebox.showwarning("Somme Insiffisante","Balance Insiffisante !")
				cnnx.close()
			else:
				messagebox.showwarning("Somme Insiffisante",f"Vous N'avez Pas Assez Des Credit ! [   {montant_reel} Unité(s)   ]")
				cnnx.close()
	Updatestock = classmethod(Updatestock)
CreateTables()