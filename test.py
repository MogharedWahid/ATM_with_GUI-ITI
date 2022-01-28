#***********************************************************************************#
#*************************|  Author	  : Moghared Wahid           |******************#
#*************************|  Email	  : mogharedwahid@gmail.com  |******************#
#*************************|  Project  : ATM - ITI  			     |******************#
#***********************************************************************************#

from distutils import command
from faulthandler import disable
from random import vonmisesvariate
import tkinter

#My client_ids List
myDict={215321701332:{'Name':'Ahmed Abdelrazek','Password':1783 ,'Balance':3500166 ,'Locked':0},
		203659302214:{'Name':'Salma Mohamed'   ,'Password':1390 ,'Balance':520001  ,'Locked':0},
		126355700193:{'Name':'Adel Khaled'	   ,'Password':1214 ,'Balance':111000  ,'Locked':0},
		201455998011:{'Name':'Saeed Amin'	   ,'Password':2001 ,'Balance':1200    ,'Locked':0},
		201122369851:{'Name':'Amir Salama'	   ,'Password':8935 ,'Balance':178933  ,'Locked':0},
		201356788002:{'Name':'Wael Mohamed'	   ,'Password':3420 ,'Balance':55000   ,'Locked':0},
		203366789564:{'Name':'Mina Sameh'	   ,'Password':1179 ,'Balance':18000   ,'Locked':0},
		201236787812:{'Name':'Omnia Ahmed'	   ,'Password':1430 ,'Balance':180350  ,'Locked':0}}


def Back_to_entery():
	cashWithdraw.destroy()
	balanceInquiry.destroy()
	passwordChange.destroy()
	fawryService.destroy()
	exit.destroy()
	Enter2_Button.destroy()
	Cancel_Button.destroy()
	welcomeLabel.destroy()
	Entry_point()


def Entry_point():
	global IDLabel
	global enteredID
	global Enter_Button
	IDLabel=tkinter.Label(root,text="Please enter your ID",font=("Arial", 15)) #middle position
	IDLabel.place(x=390, y=200)
	enteredID=tkinter.Entry(root,width=30,text=40)
	enteredID.place(x=395, y=230)
	Enter_Button=tkinter.Button(root,height=2,width=10,text="Enter",bg='green',fg='white',command=check_id_gui)
	Enter_Button.place(x=900,y=670)

attempts=3
#function that checks whether it's on the system or not
def check_id(client_id):
	if(client_id in myDict):
		if(myDict[client_id]['Locked']==1):
			print("Sorry your account has been locked, please head to the bank")
			return 0
		else:
			return 1
	else:
		return 0

#function that show password field
def show_password_field():
	global passLabel
	global passAttempts
	global attempts
	passLabel=tkinter.Label(text="Please enter your password",font=("Arial", 15))
	passLabel.place(x=390, y=260)
	passAttempts=tkinter.Label(text=str(attempts)+" attempts left")
	passAttempts.place(x=395, y=315)
	global enteredPass
	enteredPass=tkinter.Entry(root,width=30,show='*')
	enteredPass.place(x=395, y=295)
	Enter_Button.configure(command=check_password_gui)

#function that show invalid ID
def show_invalidID_field():
	topLevelVar=tkinter.Toplevel()
	topLevelVar.configure(bg='red')
	topLevelVar.geometry("300x300+600+350")
	tkinter.Label(topLevelVar, text='Invalid ID !').place(x=70,y=120)

#function that show invalid ID
def show_invalidPass_field():
	topLevelVar=tkinter.Toplevel()
	topLevelVar.geometry("300x250+600+350")
	tkinter.Label(topLevelVar, text='Your account has been blocked !',font=("Arial", 15),fg='red').place(x=67,y=100)

#function that checks the entered password
def check_password(client_id,client_pass):
	global attempts
	if(client_pass == myDict[client_id]['Password']):
		return 1
	elif(attempts == 1):
		myDict[client_id]['Locked'] = 1
		show_invalidPass_field()
	else:
		attempts -= 1
		passAttempts.configure(text="Wrong password "+str(attempts) + " attempts left")

  		
def check_password_gui():
	global cashWithdraw
	global balanceInquiry
	global passwordChange
	global fawryService
	global exit
	global Enter2_Button
	global Cancel_Button
	global welcomeLabel
	client_pass = int(enteredPass.get())
	if(check_password(client_id,client_pass)):
			Enter_Button.destroy()
			IDLabel.destroy()
			passLabel.destroy()
			enteredID.destroy()
			enteredPass.destroy()
			passAttempts.destroy()

			global cashWithdraw
			cashWithdraw=tkinter.Button(root,height=3,width=15,text="Cash Withdraw",font=("Arial", 15),bg='black',fg='white',command=show_cash_field)
			cashWithdraw.place(x=800,y=100)

			global balanceInquiry
			balanceInquiry=tkinter.Button(root,height=3,width=15,text="Balance Inquiry",font=("Arial", 15),bg='black',fg='white',command=show_balance)
			balanceInquiry.place(x=800,y=200)
			
			global passwordChange
			passwordChange=tkinter.Button(root,height=3,width=15,text="Password Change",font=("Arial", 15),bg='black',fg='white',command=show_change_password)
			passwordChange.place(x=800,y=300)

			global fawryService
			fawryService=tkinter.Button(root,height=3,width=15,text="Fawry Service",font=("Arial", 15),bg='black',fg='white',command=fawry)
			fawryService.place(x=800,y=400)

			global exit
			exit=tkinter.Button(root,height=3,width=15,text="Exit",font=("Arial", 15),bg='black',fg='white',command=Back_to_entery)
			exit.place(x=800,y=500)

			global welcomeLabel
			welcomeLabel=tkinter.Label(root,text="Welcome "+myDict[client_id]['Name'],font=("Times new roman", 30))
			welcomeLabel.place(x=135, y=80)

			global Enter2_Button
			global Cancel_Button
			Enter2_Button=tkinter.Button(root,height=2,width=10,text="Enter",bg='green',fg='white')
			Cancel_Button=tkinter.Button(root,height=2,width=10,text="Cancel",bg='crimson',fg='white',command=close_withdraw)

			Enter2_Button.place(x=600,y=600)
			Cancel_Button.place(x=100,y=600)


def check_id_gui():
  global client_id
  client_id = int(enteredID.get())
  idFlag=check_id(client_id)
  if(idFlag):
    show_password_field()
  else:
    show_invalidID_field()

#Cash withdraw show and check
def show_cash_field():

	global cashLabel
	global maxTransaction
	global multipleHundred
	global noSufficient

	global maxTrans
	global multipleHund
	global noSufficin
	

	maxTrans=0
	multipleHund=0
	noSufficin=0
	cashLabel=tkinter.Label(root,text="Please enter cash amount",font=("Arial", 15))
	cashLabel.place(x=250, y=200)
	global enteredCash
	enteredCash=tkinter.Entry(root,width=30)
	enteredCash.place(x=260, y=240)
	Enter2_Button.configure(command=cash_check)
	maxTransaction=tkinter.Label(text="- Max. trasnaction is 5000 L.E !",fg='black')
	maxTransaction.place(x=250, y=270)
	multipleHundred=tkinter.Label(text="- The allowed values are only multiples of 100 L.E !",fg='black')
	multipleHundred.place(x=250, y=290)
	noSufficient=tkinter.Label(text="- Balance should be more than your amount !",fg='black')
	noSufficient.place(x=250, y=310)

def close_withdraw():
	cashLabel.destroy()
	enteredCash.destroy()
	maxTransaction.destroy()
	multipleHundred.destroy()
	noSufficient.destroy()

def cash_check():
	client_entered_cash = int(enteredCash.get())
	if (client_entered_cash<5000):
		maxTrans=1
		maxTransaction.configure(fg='green')
	else:
		maxTrans = 0
		maxTransaction.configure(fg='red')
	if (client_entered_cash%100 ==0):
		multipleHund=1
		multipleHundred.configure(fg='green')
	else:
		multipleHund=0
		multipleHundred.configure(fg='red')
	if (myDict[client_id]['Balance']>client_entered_cash):
		noSufficin=1
		noSufficient.configure(fg='green')
	else:
		noSufficin=0
		noSufficient.configure(fg='red')
	if (maxTrans==1 and multipleHund==1 and noSufficin==1):
		cashLabel.destroy()
		enteredCash.destroy()
		maxTransaction.destroy()
		multipleHundred.destroy()
		noSufficient.destroy()
		ATM_Actuator_Out()
		myDict[client_id]['Balance']-=client_entered_cash
		topLevelTransaction=tkinter.Toplevel()
		Return=tkinter.Button
		topLevelTransaction.geometry("300x250+600+350")
		tkinter.Label(topLevelTransaction, text='Transaction done. Thank you :)',fg='green').place(x=70,y=100)
		ReturnButton=tkinter.Button(topLevelTransaction, text='Return',fg='white',bg='black',command=topLevelTransaction.destroy)
		ReturnButton.place(x=125,y=150)
	
# Cash withdraw function (HW part)
def ATM_Actuator_Out():
	print("ATM Actuatuor Out")

# Show balance function
def show_balance():
	topLevelBalance=tkinter.Toplevel()
	Return=tkinter.Button
	topLevelBalance.geometry("300x250+600+350")
	tkinter.Label(topLevelBalance, text='Your balance is '+str(myDict[client_id]['Balance'])+' L.E',font=("Arial", 10)).place(x=70,y=100)
	ReturnButton=tkinter.Button(topLevelBalance, text='Return',fg='white',bg='black',command=topLevelBalance.destroy)
	ReturnButton.place(x=125,y=150)
	

# Show change password function
def show_change_password():
	global passMatch
	global passLen
	passMatch=0
	passLen=0
	global passCondition1
	global passCondition2
	global enteredPass1
	global enteredPass2
	global topLevelPassword
	topLevelPassword=tkinter.Toplevel()
	Return=tkinter.Button
	topLevelPassword.geometry("300x250+600+350")
	PassLabel=tkinter.Label(topLevelPassword,text="Enter new password   ",font=("Arial", 10))
	PassLabel.place(x=20, y=30)
	enteredPass1=tkinter.Entry(topLevelPassword,width=10,show='*')
	enteredPass1.place(x=170, y=32)
	PassLabe2=tkinter.Label(topLevelPassword,text="Re-enter new password",font=("Arial", 10))
	PassLabe2.place(x=20, y=55)
	enteredPass2=tkinter.Entry(topLevelPassword,width=10,show='*')
	enteredPass2.place(x=170, y=57)
	ReturnButton=tkinter.Button(topLevelPassword, text='Confirm',fg='white',bg='black',command=check_change_password)
	ReturnButton.place(x=125,y=175)
	passCondition1=tkinter.Label(topLevelPassword,text="- Password should be four digits !",fg='black')
	passCondition1.place(x=30, y=100)
	passCondition2=tkinter.Label(topLevelPassword,text="- The two passwords should match !",fg='black')
	passCondition2.place(x=30, y=120)

def check_change_password():
	if (len(enteredPass1.get())==4):
		if(len(enteredPass2.get())==4):
			passLen=1
			passCondition1.configure(fg='green')
		else:
			passLen=0
			passCondition1.configure(fg='red')
	else:
		passLen=0
		passCondition1.configure(fg='red')
	
	if((enteredPass1.get()) == (enteredPass2.get())):
		passMatch=1
		passCondition2.configure(fg='green')
	else:
		passMatch=0
		passCondition2.configure(fg='red')
	if (passMatch==1 and passLen==1):
		myDict[client_id]['Password']=int(enteredPass1.get())
		topLevelPassword.destroy()


def fawry():
	global Vo
	Vo=0
	global Or
	Or=0
	global Et
	Et=0
	global We
	We=0
	global topLevelFawry
	topLevelFawry=tkinter.Toplevel()
	topLevelFawry.geometry("300x250+600+350")
	PassLabel=tkinter.Label(topLevelFawry,text="Choose your network:",font=("Arial", 10))
	PassLabel.place(x=15, y=10)
	Vodafone=tkinter.Button(topLevelFawry,height=1,width=6,text="Vodafone",font=("Arial", 10),bg='white',fg='red',command=vodafone_chosen)
	Vodafone.place(x=15,y=40)
	Etisalat=tkinter.Button(topLevelFawry,height=1,width=6,text="Etisalat",font=("Arial", 10),bg='white',fg='green',command=etisalat_chosen)
	Etisalat.place(x=85,y=40)
	Orange=tkinter.Button(topLevelFawry,height=1,width=6,text="Orange",font=("Arial", 10),bg='white',fg='orange',command=orange_chosen)
	Orange.place(x=155,y=40)
	We=tkinter.Button(topLevelFawry,height=1,width=6,text="We",font=("Arial", 10),bg='white',fg='purple',command=we_chosen)
	We.place(x=225,y=40)
	confirmButton=tkinter.Button(topLevelFawry, text='Confirm',fg='white',bg='black',command=check_fawry)
	confirmButton.place(x=200,y=190)
	cancelButton=tkinter.Button(topLevelFawry, text='Cancel',fg='white',bg='black',command=topLevelFawry.destroy)
	cancelButton.place(x=70,y=190)

def vodafone_chosen():
	global Vo
	Vo=1
	global enteredcashV 
	global enterednumV 
	vodafone_Label=tkinter.Label(topLevelFawry,text="Enter your phone number :",font=("Arial", 10))
	vodafone_Label.place(x=15, y=70)
	vodafone_initial=tkinter.Label(topLevelFawry,text="010",font=("Arial", 10))
	vodafone_initial.place(x=70, y=90)
	enterednumV=tkinter.Entry(topLevelFawry,width=8)
	enterednumV.place(x=95, y=91)
	cashV_Label=tkinter.Label(topLevelFawry,text="Enter recharge amount :",font=("Arial", 10))
	cashV_Label.place(x=15, y=110)
	enteredcashV=tkinter.Entry(topLevelFawry,width=8)
	enteredcashV.place(x=95, y=130)

def etisalat_chosen():
	global Et
	Et=1
	global enteredcashEt 
	global enterednumEt
	etisalat_Label=tkinter.Label(topLevelFawry,text="Enter your phone number :",font=("Arial", 10))
	etisalat_Label.place(x=15, y=70)
	etisalat_initial=tkinter.Label(topLevelFawry,text="011")
	etisalat_initial.place(x=70, y=90)
	enterednumEt=tkinter.Entry(topLevelFawry,width=8)
	enterednumEt.place(x=95, y=91)
	cashEt_Label=tkinter.Label(topLevelFawry,text="Enter recharge amount :",font=("Arial", 10))
	cashEt_Label.place(x=15, y=110)
	enteredcashEt=tkinter.Entry(topLevelFawry,width=8)
	enteredcashEt.place(x=95, y=130)

def orange_chosen():
	global Or
	Or=1
	global enteredcashOr
	global enterednumOr
	orange_Label=tkinter.Label(topLevelFawry,text="Enter your phone number :",font=("Arial", 10))
	orange_Label.place(x=15, y=70)
	orange_initial=tkinter.Label(topLevelFawry,text="012")
	orange_initial.place(x=70, y=90)
	enterednumOr=tkinter.Entry(topLevelFawry,width=8)
	enterednumOr.place(x=95, y=91)
	cashOr_Label=tkinter.Label(topLevelFawry,text="Enter recharge amount :",font=("Arial", 10))
	cashOr_Label.place(x=15, y=110)
	enteredcashOr=tkinter.Entry(topLevelFawry,width=8)
	enteredcashOr.place(x=95, y=130)
	

def we_chosen():
	global We
	We=1
	global enteredcashWe
	global enterednumWe
	we_Label=tkinter.Label(topLevelFawry,text="Enter your phone number :",font=("Arial", 10))
	we_Label.place(x=15, y=70)
	we_initial=tkinter.Label(topLevelFawry,text="015")
	we_initial.place(x=70, y=90)
	enterednumWe=tkinter.Entry(topLevelFawry,width=8)
	enterednumWe.place(x=95, y=91)
	cashWe_Label=tkinter.Label(topLevelFawry,text="Enter recharge amount :",font=("Arial", 10))
	cashWe_Label.place(x=15, y=110)
	enteredcashWe=tkinter.Entry(topLevelFawry,width=8)
	enteredcashWe.place(x=95, y=130)

def check_fawry():
	global Vo
	global We
	global Or
	global Et
	if (Vo==1):
		if (len(enterednumV.get()) == 8 and (int(enteredcashV.get())) < myDict[client_id]['Balance']):
			myDict[client_id]['Balance']-=(int(enteredcashV.get()))
			Vo=0
			topLevelFawry.destroy()
		if (len(enterednumV.get()) != 8):
			numV=tkinter.Label(topLevelFawry,text="Invalid phone number !",fg='red')
			numV.place(x=15, y=150)
		if ((int(enteredcashV.get())) > myDict[client_id]['Balance']):
			cashV=tkinter.Label(topLevelFawry,text="Not enough balance !",fg='red')
			cashV.place(x=15, y=165)

	elif (Et==1):
		if (len(enterednumEt.get()) == 8 and (int(enteredcashEt.get())) < myDict[client_id]['Balance']):
			myDict[client_id]['Balance']-=(int(enteredcashEt.get()))
			Et=0
			topLevelFawry.destroy()
		if (len(enterednumEt.get()) != 8):
			numEt=tkinter.Label(topLevelFawry,text="Invalid phone number !",fg='red')
			numEt.place(x=15, y=150)
		if ((int(enteredcashEt.get())) > myDict[client_id]['Balance']):
			cashEt=tkinter.Label(topLevelFawry,text="Not enough balance !",fg='red')
			cashEt.place(x=15, y=165)
	elif (Or==1):
		if (len(enterednumOr.get()) == 8 and (int(enteredcashOr.get())) < myDict[client_id]['Balance']):
			myDict[client_id]['Balance']-=(int(enteredcashOr.get()))
			Or=0
			topLevelFawry.destroy()
		if (len(enterednumOr.get()) != 8):
			numOr=tkinter.Label(topLevelFawry,text="Invalid phone number !",fg='red')
			numOr.place(x=15, y=150)
		if ((int(enteredcashOr.get())) > myDict[client_id]['Balance']):
			cashV=tkinter.Label(topLevelFawry,text="Not enough balance !",fg='red')
			cashV.place(x=15, y=165)
	elif (We==1):
		if (len(enterednumWe.get()) == 8 and (int(enteredcashWe.get())) < myDict[client_id]['Balance']):
			myDict[client_id]['Balance']-=(int(enteredcashWe.get()))
			We=0
			topLevelFawry.destroy()
		if (len(enterednumWe.get()) != 8):
			numWe=tkinter.Label(topLevelFawry,text="Invalid phone number !",fg='red')
			numWe.place(x=15, y=150)
		if ((int(enteredcashWe.get())) > myDict[client_id]['Balance']):
			cashWe=tkinter.Label(topLevelFawry,text="Not enough balance !",fg='red')
			cashWe.place(x=15, y=165)



#main program
# Main Window Configuration
root= tkinter.Tk()
root.geometry("1000x720+250+60")
root.resizable(False,False)
root.title("Welcome to ITI bank")

Entry_point()

root.mainloop()

passFlag=0
