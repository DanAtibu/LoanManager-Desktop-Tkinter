#coding: utf-8
import tkinter,threading,sqlite3,time , os , add
from plyer import notification 
import cnnx
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def interfacefirst():
	def cnx():
		user = cnnx.account()
		rep = user.connexioncount(enternameu.get(),enterpsswrd.get(),Combofonction.get())
		if rep == 1:
			root.destroy()
			interfaceadmin() 
		elif rep == 2:
			root.destroy()
			formulairesaveclient(1)
		else:
			messagebox.showerror("Compte","le compte n'existe pas svp")
	def createcount():
		window = tkinter.Toplevel()
		window.title("Creer Un Compte")
		window.geometry("800x300+50+50")
		window.minsize(800,300)
		window.maxsize(800,300)
		window.iconbitmap("icone.ico")
		imgg = tkinter.PhotoImage(file='CREER.png').zoom(10).subsample(10)
		L = tkinter.Label(window,image=imgg)
		L.pack()
		def enter(x,y):
			entre = tkinter.Entry(window,bd=0)
			entre.place(x=x,y=y,width=173,height=29)
			return entre
		account = cnnx.account()
		username = enter(429,102)
		password = enter(429,137)
		recovery = enter(429,171)
		Postcount = ttk.Combobox(window,font=("",10),values=("Administrateur","Facturier"))
		Postcount.set("Administrateur")
		Postcount.place(x=630,y=137,height=29)
		Bttn = tkinter.Button(window,text="Confirmer",font=("",12),command=lambda:account.Saveancount(username.get(),password.get(),Postcount.get(),recovery.get()))
		Bttn.place(x=429,y=218,height=28,width=173)
		window.mainloop()

	root = tkinter.Tk()
	root.title("LoanManager")
	root.geometry("1100x600+50+50")
	root.minsize(1100,600)
	root.maxsize(1100,600)
	root.iconbitmap("icone.ico")

	back = tkinter.PhotoImage(file="4.png").zoom(10).subsample(10)
	img = tkinter.Label(root,image=back)
	img.pack() 
	maintext = tkinter.Text(root)
	enternameu = tkinter.Entry(root,border=0,font=("arial",13),bg="#ffffff")
	enternameu.place(x=687,y=234,width=310,height=48)

	enterpsswrd = tkinter.Entry(root,border=0,font=("arial",13),bg="#ffffff",show="•")
	enterpsswrd.place(x=687,y=318,width=310,height=48)

	cnnxion = tkinter.PhotoImage(file="connexion.png").zoom(10).subsample(13)
	btn = tkinter.Button(root,image=cnnxion,bg="#ffffff",font=("Cambria",12),command=cnx)
	btn.place(x=753,y=409,width=180,height=44)

	creer = tkinter.PhotoImage(file="creeruncompte.png").zoom(10).subsample(10)
	btn = tkinter.Button(root,bg="#ffffff",image=creer,border=0,font=("Cambria",12),command=createcount)
	btn.place(x=35,y=528,width=196,height=33)

	Combofonction = ttk.Combobox(root,values=("Administrateur","Facturier"),font=("Cambria",12))
	Combofonction.set("Administrateur")
	Combofonction.place(x=35,y=160,width=180,height=30)

	root.mainloop()

def interfaceadmin():
	def deptcheking():
		now = datetime.now()
		now = str(now).split(".")
		now = now[0]
		now = now.split() 
		connex , cursor = cnnx.connexion()	
		now = (now[0], )
		cursor.execute(f"SELECT Id_Client FROM Dettetable WHERE Echeance = (?)",now)
		data = cursor.fetchall()
		print(data)
		connex.close()
		items = []
		if len(data) != -1:
			for item in data:
				items.append(item[0])
			notification.notify(title="LoanManager",app_name="LoanManager",message=f"Code D'Identification : {items}",app_icon="icone.ico")
				
		else:
			messagebox.showinfo("Dette Information","Aucune Personne n'est sessée Payée Aujourd'hui !")
	def MouvementProduit():
		window = tkinter.Toplevel()
		window.title("LoanManager")
		window.geometry("1100x600+50+50")
		window.minsize(1100,600)
		window.maxsize(1100,600)
		window.iconbitmap("icone.ico")
		back = tkinter.PhotoImage(file="movement.png").zoom(10).subsample(10)
		img = tkinter.Label(window,image=back)
		img.pack()
		produit = cnnx.produit()
		def nowtime():
			now = datetime.now()
			now = str(now).split(".")
			now = now[0]
			now = now.split()
			DateDo = now[0] 
			heure = now[1]
			return [DateDo,heure]
		def cmbbox(x,y,tupledata):
			Combofonction = ttk.Combobox(window,values=tupledata,font=("Cambria",12))
			Combofonction.set(tupledata[0])
			Combofonction.place(x=x,y=y,width=207,height=37)
			return Combofonction
		def enter(x,y):
			entre = tkinter.Entry(window,bd=0)
			entre.place(x=x,y=y,width=207,height=37)
			return entre
		def bttn(x,y):
			B = tkinter.Button(window,text=" Valider ",bg="#390d0b",fg="white")
			B.place(x=x,y=y,width=158,height=29)
			return B
		x = 50
		VID_client = enter(x,102)
		VUnite = enter(x,165)
		VMessage = enter(x,229)
		VMega = enter(x,289)
		VMontant = enter(x,348)
		VMode_payout = cmbbox(x,410,("Par Cash","Banque","AirtelMoney","M-Pesa","OrageMoney"))
		VReseau = cmbbox(x,470,("Airtel","Vodacom","Orage"))
		VButton = bttn(75,522)
		VButton["command"] = lambda:produit.saveoperation((VID_client.get(),nowtime()[0],nowtime()[1],VUnite.get(),VMessage.get(),VMega.get(),VMontant.get(),"-","vente",VMode_payout.get(),VReseau.get()))
		#===========================================================================
		x,y = 323,541
		REID_client = enter(x,102)
		REUnite = enter(x,165)
		REMessage = enter(x,229)
		REMega = enter(x,289)
		REMontant = enter(y,102)
		REEcheance = enter(y,165)
		REMode_payout = cmbbox(y,229,("Par Cash","Banque","AirtelMoney","M-Pesa","OrageMoney"))
		REReseau = cmbbox(y,289,("Airtel","Vodacom","Orage"))
		REOperation = cmbbox(455,348,("Emprunt","Rembourcement"))
		REButton = bttn(452,522)
		REButton["command"] = lambda:produit.saveoperation((REID_client.get(),nowtime()[0],nowtime()[1],REUnite.get(),REMessage.get(),REMega.get(),REMontant.get(),REEcheance.get(),REOperation.get(),REMode_payout.get(),REReseau.get()))
		#==============================================================================
		x = 843
		AUnite = enter(x,84)
		AMessage = enter(x,147)
		AMega = enter(x,206)
		AMontant = enter(x,265)
		AMode_payout = cmbbox(x,325,("Par Cash","Banque","AirtelMoney","M-Pesa","OrageMoney"))
		AReseau = cmbbox(x,390,("Airtel","Vodacom","Orage"))
		AButton = bttn(860,522)
		AButton["command"] = lambda:produit.saveoperation(("-",nowtime()[0],nowtime()[1],AUnite.get(),AMessage.get(),AMega.get(),AMontant.get(),"-","approvissionement",AMode_payout.get(),AReseau.get()))
		window.mainloop()

	def apprv():
		root = tkinter.Toplevel()
		root.title("LoanManager")
		root.iconbitmap("icone.ico")
		root.config(background="#4c110c")
		root.minsize(800,300)
		root.maxsize(800,300)
		frm = tkinter.Frame(root,border=2,bg="#4c110c")
		croll = tkinter.Scrollbar(frm,orient='vertical')
		zonetextresultat = tkinter.Text(frm,font=("",10),fg="white",bg="#4c110c",yscrollcommand=croll.set)
		croll.config(command=zonetextresultat.yview)
		croll.place(x=765,y=0,height=280)
		zonetextresultat.place(x=5,y=0,width=760,height=280)
		frm.place(x=10,y=10,width=800,height=300)
		connex , cursor = cnnx.connexion()	
		cursor.execute("SELECT DateDo,heure,Quantité_Units,Quantité_mega,Quantité_Megabyte,Montant,Reseau FROM tableauoperationgenerales WHERE operation = 'approvissionement'")
		data = cursor.fetchall()
		connex.close()
		i = len(data)-1
		while i != -1:
			zonetextresultat.insert("end",f"	Date            : {data[i][0]} \n")
			zonetextresultat.insert("end",f"	Heure          : {data[i][1]} \n")
			zonetextresultat.insert("end",f"	Qté Unités   :  {data[i][2]} \n")
			zonetextresultat.insert("end",f"	Qté Msg      :  {data[i][3]} \n")
			zonetextresultat.insert("end",f"	Qté Mega    :  {data[i][4]} \n")
			zonetextresultat.insert("end",f"	Montant      :   {data[i][5]} \n")
			zonetextresultat.insert("end",f"	Reseau       :   {data[i][6]} \n")
			zonetextresultat.insert("end","#============================================================================================#\n")
			i -= 1
		zonetextresultat["state"] = "disabled"
		root.mainloop()

	def viewclienthistory(id_about):
		Client = cnnx.Client()
		data = Client.ClientHistorique(id_about)#3450
		i = len(data)-1
		if i > -1:
			root = tkinter.Toplevel()
			root.title("LoanManager")
			root.iconbitmap("icone.ico")
			root.config(background="#4c110c")
			root.minsize(800,300)
			root.maxsize(800,300)
			frm = tkinter.Frame(root,border=2,bg="#4c110c")
			croll = tkinter.Scrollbar(frm,orient='vertical')
			zonetextresultat = tkinter.Text(frm,font=("",10),fg="white",bg="#4c110c",yscrollcommand=croll.set)
			croll.config(command=zonetextresultat.yview)
			croll.place(x=765,y=0,height=280)
			zonetextresultat.place(x=5,y=0,width=760,height=280)
			frm.place(x=10,y=10,width=800,height=300)

			while i > -1:
				zonetextresultat.insert("end","		Date              		      : "+str(data[i][2] +"  /  Heure : "+data[i][3])+"\n")
				zonetextresultat.insert("end","		Unité           		      : "+str(data[i][4])+ "\n")
				zonetextresultat.insert("end","		Message          		      : "+str(data[i][5])+ "\n")
				zonetextresultat.insert("end","		MegaByte          		      : "+str(data[i][6])+ "\n")
				zonetextresultat.insert("end","		Montant         		      : "+str(data[i][7])+ "\n")
				if data[i][8] != "":
					zonetextresultat.insert("end","		Echeance        		      : "+str(data[i][8])+ "\n")
				zonetextresultat.insert("end","		Operation     		      : "+str(data[i][9])+ "\n")
				zonetextresultat.insert("end","		Moyen De Paiement     : "+str(data[i][10])+ "\n")
				zonetextresultat.insert("end","		Reseau           		      : "+str(data[i][11])+"\n")
				
				zonetextresultat.insert("end","#============================================================================================#\n")
				i -= 1
			zonetextresultat["state"] = "disabled"
			root.mainloop()
		else:
			messagebox.showerror("Données Introuvable !",f"Aucune Données Sur La Personne !")
	def connexion():
		user =str(os.getlogin())
		connexion_database = sqlite3.connect(f"C:/Users/{user}/Documents/DataBaseLoanManager.db")
		manager = connexion_database.cursor()
		return connexion_database,manager

	root = tkinter.Tk()
	root.title("LoanManager")
	root.geometry("1100x600+50+50")
	root.minsize(1100,600)
	root.maxsize(1100,600)
	root.iconbitmap("icone.ico")
	back = tkinter.PhotoImage(file="3.png").zoom(10).subsample(10)
	img = tkinter.Label(root,image=back)
	img.pack()
	#imgg = tkinter.PhotoImage(file="search.png").zoom(10).subsample(9)

	def ch1(event):
		Seach_Button["bg"] = "#fae607"
		Seach_Button["fg"] = "white"
	def ch2(event):
		Seach_Button["bg"] = '#390d0b'
		Seach_Button["fg"] = "white"
	Client = cnnx.Client()
	
	Seach_entry = tkinter.Entry(root,bd=0)
	Seach_entry.place(x=84,y=45,width=210,height=35)
	Seach_Button = tkinter.Button(root,text="Reseach",font=("",8),fg="white",bg='#390d0b',command=lambda:Client.ShowInformationsAboutClient(Seach_entry.get()))
	Seach_Button.place(x=75,y=90,width=70,height=35)
	Delete_Button = tkinter.Button(root,text="Delete",font=("",8),fg="white",bg='#390d0b',command=lambda:Client.DeleteClient(Seach_entry.get()))
	Delete_Button.place(x=240,y=90,width=70,height=35)
	Client_View = tkinter.Button(root,text="View All",font=("",8),fg="white",bg='#390d0b',command=lambda:viewclienthistory(Seach_entry.get()))
	Client_View.place(x=160,y=90,width=70,height=35)
	New_Client = tkinter.Button(root,text="Nouveau Client",font=("",8),fg="white",bg='#390d0b',command=lambda:formulairesaveclient(2))
	New_Client.place(x=75,y=130,width=100,height=35)
	Mouvement_Client_View = tkinter.Button(root,text="Mouvement",font=("",8),fg="white",bg='#390d0b',command=MouvementProduit)
	Mouvement_Client_View.place(x=126,y=289,width=189,height=45)
	ButtonApprov = tkinter.Button(root,text="Historique Approvissionement",font=("",8),fg="white",bg='#390d0b',command=apprv)
	ButtonApprov.place(x=75,y=172,height=40)
	ButtonApprov = tkinter.Button(root,text="Dettes Notification",font=("",8),fg="white",bg='#390d0b',command=deptcheking)
	ButtonApprov.place(x=75,y=220,height=40)
	ButtonInfosClient = tkinter.Button(root,text="...",bd=0,font=("",15),fg="white",bg='#390d0b',command=lambda:add.ClientInformationsDisplay())
	ButtonInfosClient.place(x=663,y=55,height=40)	
	ButtonAlldept = tkinter.Button(root,text="...",bd=0,font=("",15),fg="white",bg='#390d0b',command=lambda:add.deptallinformations())
	ButtonAlldept.place(x=663,y=140,height=40)

	Seach_Button.bind("<Enter>",ch1)
	Seach_Button.bind("<Leave>",ch2)

	def makelabel(x,y,w,h):
		Label = tkinter.Label(root,text="NULL",bg="#390d0b",fg="white",font=("",12))
		Label.place(x=x,y=y,width=w,height=h) 
		return Label
	def updateview():
		while True:
			connect , cursor = connexion()
			number = cursor.execute("SELECT COUNT(*) FROM ClientInformations")
			TTLClient = number.fetchone()[0]
			Totalclients['text'] = TTLClient # Pour la mise du total Client sur l'interface
			#========================================================
			produit = cnnx.produit()
			TTUV = produit.viewdayoper("Quantité_Units","DateDo",1)
			TTUE = produit.viewdayoper("Quantité_mega","DateDo",1)
			TTUR = produit.viewdayoper("Quantité_Megabyte","DateDo",1)
			TTUAirtel = produit.viewdayoper("Airtel_Unit","MouvementCapital",2)
			TTUVoda = produit.viewdayoper("Vodacom_Unit","MouvementCapital",2)
			TTUOrage = produit.viewdayoper("Orage_Unit","MouvementCapital",2)
			LoanOrage = produit.viewdayoper("Orage_loan","MouvementCapital",2)
			LoanAirtel = produit.viewdayoper("Airtel_loan","MouvementCapital",2)
			LoanVod = produit.viewdayoper("Vodacom_loan","MouvementCapital",2)
			#===============================================================================

			now = datetime.now()
			now = str(now).split(".")
			now = now[0]
			now = now.split() 
			now[0] = (now[0], )
			cursor.execute(f"SELECT Id_Client FROM Dettetable WHERE Echeance = (?)",now[0])
			data = cursor.fetchall()
			peopedept = {""}
			for i in data:
				peopedept.add(i[0])
			data = cursor.execute(f"SELECT COUNT(*) FROM Dettetable")# pour avoir le total des toutles les dettes
			#===============================================================================

			Total_dept_airtel["text"] = LoanAirtel
			Total_dept_vodac["text"] = LoanVod
			Total_dept_orage["text"] = LoanOrage

			Total_unit_airtel["text"] = TTUAirtel
			Total_unit_vodac["text"] = TTUVoda
			Total_unit_orage["text"] = TTUOrage
			Totalunits["text"] = int(TTUOrage[0]) + int(TTUVoda[0]) + int(TTUAirtel[0])

			TTL_U_Vendue["text"] = str(TTUV[1]) +" / "+ str(TTUV[0])
			TTL_Msg_Vendue["text"] = str(TTUE[1]) +" / "+ str(TTUE[0]) 
			TTL_Mega_Vendue["text"] = str(TTUR[1]) +" / "+ str(TTUR[0])

			clients_with_dept["text"] = len(peopedept)-1 #pour c qui ont une dette a payer aujourd'hui
			Totaldettes["text"] = data.fetchone()[0] # Total dettes depuis l'ouverture de l'entreprise

			#print(TTUV[1] , TTUE[1] , TTUR[1] , "new :",TTUAirtel , TTUVoda , TTUOrage)
			connect.close()
			time.sleep(10)

	def startall(nomfonction):
		ttlclient = threading.Thread(target=nomfonction).start()

	Totalclients  = makelabel(725,60,211,33)
	clients_with_dept  = makelabel(450,145,211,33)
	Totaldettes  = makelabel(725,145,211,33)
	Totalunits  = makelabel(725,210,211,33)
	Total_unit_airtel  = makelabel(450,300,145,33)
	Total_unit_vodac  = makelabel(630,300,145,33)
	Total_unit_orage  = makelabel(820,300,145,33)
	Total_dept_airtel  = makelabel(450,380,145,33)
	Total_dept_vodac  = makelabel(630,380,145,33)
	Total_dept_orage  = makelabel(820,380,145,33)
	TTL_U_Vendue = makelabel(735,475,200,20)
	TTL_Mega_Vendue = makelabel(735,510,200,20)
	TTL_Msg_Vendue = makelabel(735,540,200,20)

	startall(updateview)
	root.mainloop()

def formulairesaveclient(choix):
	if choix == 1:
		window = tkinter.Tk()
	elif choix == 2:
		window = tkinter.Toplevel()
	window.title("LoanManager")
	window.geometry("1100x600+50+50")
	window.minsize(1100,600)
	window.maxsize(1100,600)
	window.iconbitmap("icone.ico")
	back = tkinter.PhotoImage(file="formulaire.png").zoom(10).subsample(10)
	img = tkinter.Label(window,image=back)
	img.pack()

	def save():
		l = vile.get(),qrtier.get(),avenu.get(),num.get(),uniteday.get(),msgday.get(),megaday.get(),modepaie.get(),waypaie.get()
		m = name.get(),postname.get(),pname.get(),sexe.get(),etatcivil.get(),profession.get(),telep.get(),vendeur.get()
		table_data = m + l

		if "" not in table_data:
			Client = cnnx.Client()
			id_return = Client.SaveClient(table_data)
			l = tkinter.Label(window,text=id_return,fg="white",bg="#4c110c",bd=0,font=("",15))
			l.place(x=800,y=525,width=243,height=29)
			notification.notify(title="LoanManager",app_name="LoanManager",message=f"New User In Data Base {id_return}",app_icon="icone.ico")
		else:
			messagebox.showwarning("Données Incorrectées","Un Champ est Vide")

	def sav():
		threading.Thread(target=save).start()
	def entry(x,y):
		entre = tkinter.Entry(window,bg="#ffffff",bd=0)
		entre.place(x=x,y=y,width=243,height=29)
		return entre

	def Combo(x,y,w):
		Combo = ttk.Combobox(window,values=w,font=("",10))
		Combo.set(w[0])
		Combo.place(x=x,y=y,width=242,height=25)
		return Combo

	posx = 270
	name = entry(posx,115)
	postname = entry(posx,157)
	pname = entry(posx,197)
	sexe = entry(posx,237)
	etatcivil = entry(posx,278)
	profession = entry(posx,318)
	telep = entry(posx,361)	
	vendeur = Combo(posx,403,("Oui","Non"))
	#====================================
	posx = 800
	vile = entry(posx,114)
	qrtier = entry(posx,156)
	avenu = entry(posx,197)
	num = entry(posx,237)
	uniteday = entry(803,278)
	msgday = entry(803,318)
	megaday = entry(803,360)
	modepaie = Combo(803,404,("Par Totalité","Par Tranche","Le Deux par Interminence","Par Cash"))
	waypaie = Combo(803,446,("Banque","AirtelMoney","M-Pesa","OrageMoney"))
	#====================================

	valider = tkinter.PhotoImage(file="valider.png").zoom(7).subsample(10)
	b = tkinter.Button(window,border=0,image = valider ,bg="#ffffff" , command=sav)
	b.place(x=430,y=525,width=230,height=31)

	window.mainloop()
def nowtime():
		now = datetime.now()
		now = str(now).split(".")
		now = now[0]
		now = now.split()
		DateDo = now[0] 
		heure = now[1]
		return [DateDo,heure]
days = ["2020-09-18","2020-09-19","2020-09-20","2020-09-21","2020-09-22"]


if nowtime()[0]:
# if nowtime()[0] not in days:
#listeimage = ["3.png","4.png","CREER.png","connexion.png","creeruncompte.png","formulaire.png","icone.ico","movement.png","valider.png"]
	if os.path.exists("CREER.png") and os.path.exists("creeruncompte.png") and os.path.exists("icone.ico") and os.path.exists("connexion.png") and os.path.exists("3.png") and os.path.exists("valider.png") and os.path.exists("movement.png") and os.path.exists("3.png") and os.path.exists("4.png") and os.path.exists("formulaire.png"):
		interfacefirst()
		#interfaceadmin()
	else:
		cnnx.image(2)
		interfacefirst()	
else:
	notification.notify(title="LoanManager",app_name="LoanManager",message=f"Vous Avez pas l'accés",app_icon="icone.ico")