#coding: utf-8
import cnnx , tkinter
from datetime import datetime
from tkinter import messagebox
#[deptallinformations , AllClientInformations]

def datetoday():
	now = datetime.now()
	now = str(now).split(".")
	now = now[0]
	now = now.split() 
	return now[0]

def deptallinformations():
	root = tkinter.Tk()
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
	#==================================================================
	connexion , cursor = cnnx.connexion()
	data = (datetoday(), )#datetoday() "2020-09-19"
	peoples = cursor.execute("SELECT Id_Client,Echeance FROM Dettetable WHERE Echeance = ?", data)
	peoples = peoples.fetchall()
	if peoples == []:
		zonetextresultat["font"] = ("",16)
		zonetextresultat.insert("end","\n\n\n\n\n#=================== [ AUCUNE INFORMATION ] ===================#\n\n")
	for item in peoples:
		idabout = (item[0], )
		infos = cursor.execute("SELECT Name,PostName,Prename,NumberPhone,Vile,Quatier,Avenu,NumHome FROM ClientInformations WHERE Id_Client = ?",idabout)
		infos = infos.fetchone()
		try:
			if len(infos) != -1:
				zonetextresultat.insert("end",f"		ID Client 			:  {item[0]} \n")
				zonetextresultat.insert("end",f"		Nom       			:  {infos[0]} \n")
				zonetextresultat.insert("end",f"		Postnom   			:  {infos[1]} \n")
				zonetextresultat.insert("end",f"		Prenom   			:  {infos[2]} \n")
				zonetextresultat.insert("end",f"		Téléphone			:  {infos[3]} \n")
				zonetextresultat.insert("end",f"		Ville - Quatier - Avenu - N°    :  {infos[4]} - {infos[5]} - {infos[6]} - {infos[7]}\n\n")
				
				zonetextresultat.insert("end","#============================================================================================#\n\n")
			else:
				zonetextresultat["font"] = ("",16)
				zonetextresultat.insert("end","\n\n\n\n\n#=================== [ AUCUNE INFORMATION ] ===================#\n\n")
		except:
			zonetextresultat["font"] = ("",16)
			zonetextresultat.insert("end","\n\n\n\n\n#=================== [ AUCUNE INFORMATION ] ===================#\n\n")
	#==================================================================
	zonetextresultat["state"] = "disabled"
	root.mainloop()
def ClientInformationsDisplay():
	root = tkinter.Tk()
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
	#==================================================================
	Client = cnnx.Client()
	peoples_desc = Client.ShowInformationsAboutAllClient()
	print(peoples_desc[0])
	i = len(peoples_desc)-1
	peoples = []
	while i > -1:
		peoples.append(peoples_desc[i])
		i -= 1
	if peoples == []:
		zonetextresultat["font"] = ("",16)
		zonetextresultat.insert("end","\n\n\n\n\n#=================== [ AUCUNE INFORMATION ] ===================#\n\n")
	for item in peoples:
		try:
			zonetextresultat.insert("end",f"		ID Client 			:  {item[0]} \n")
			zonetextresultat.insert("end",f"		Nom       			:  {item[1]} \n")
			zonetextresultat.insert("end",f"		Postnom   			:  {item[2]} \n")
			zonetextresultat.insert("end",f"		Prenom   			:  {item[3]} \n")
			zonetextresultat.insert("end",f"		Sexe	   		:  {item[4]} \n")
			zonetextresultat.insert("end",f"		Etat-Civil   			:  {item[5]} \n")
			zonetextresultat.insert("end",f"		Profession   			:  {item[6]} \n")
			zonetextresultat.insert("end",f"		Téléphone   			:  {item[7]} \n")
			zonetextresultat.insert("end",f"		Vendeur			:  {item[8]} \n")
			zonetextresultat.insert("end",f"		Ville - Quatier - Avenu - N°    :  {item[9]} - {item[10]} - {item[11]} - {item[12]}\n")			
			zonetextresultat.insert("end",f"		Unité/Jour   			:  {item[13]} \n")
			zonetextresultat.insert("end",f"		Msg/Jour   			:  {item[14]} \n")
			zonetextresultat.insert("end",f"		Mega/Jour   			:  {item[15]} \n")
			zonetextresultat.insert("end",f"		Mode De Payement   			:  {item[16]} \n")			
			zonetextresultat.insert("end",f"		Moyen De Payement   			:  {item[17]} \n")					
			zonetextresultat.insert("end","#============================================================================================#\n\n")
			#else:
			#	zonetextresultat["font"] = ("",16)
			#	zonetextresultat.insert("end","\n\n\n\n\n#=================== [ AUCUNE INFORMATION ] ===================#\n\n")
		except:
			zonetextresultat["font"] = ("",16)
			zonetextresultat.insert("end","\n\n\n\n\n#=================== [ AUCUNE INFORMATION ] ===================#\n\n")
	#==================================================================
	zonetextresultat["state"] = "disabled"
	root.mainloop()

#ClientInformationsDisplay()
#deptallinformations()