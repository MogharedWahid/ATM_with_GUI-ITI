#***********************************************************************************#
#*************************| Author	  : Moghared Wahid           |******************#
#*************************|  Email	  : mogharedwahid@gmail.com  |******************#
#*************************|  Project  : ATM - ITI  			     |******************#
#***********************************************************************************#

from distutils import command
from faulthandler import disable
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
	topLevelVar.configure(bg='red')
	topLevelVar.geometry("300x300+600+350")
	tkinter.Label(topLevelVar, text='Your account has been blocked !').place(x=70,y=120)

#function that checks the entered password
def check_password(client_id,client_pass):
	global attempts
	if(client_pass == myDict[client_id]['Password']):
		return 1
	elif(attempts == 1):
		Enter_Button.destroy()
		myDict[client_id]['Locked'] = 1
		show_invalidPass_field()
	else:
		attempts -= 1
		passAttempts.configure(text="Wrong password "+str(attempts) + " attempts left")

  		
def check_password_gui():
	global Enter2_Button
	client_pass = int(enteredPass.get())
	if(check_password(client_id,client_pass)):
			Enter_Button.destroy()
			Close_Button.destroy()
			IDLabel.destroy()
			passLabel.destroy()
			enteredID.destroy()
			enteredPass.destroy()
			passAttempts.destroy()

			cashWithdraw=tkinter.Button(root,height=3,width=15,text="Cash Withdraw",font=("Arial", 15),bg='black',fg='white',command=show_cash_field)
			cashWithdraw.place(x=800,y=100)

			balanceInquiry=tkinter.Button(root,height=3,width=15,text="Balance Inquiry",font=("Arial", 15),bg='black',fg='white',command=show_balance)
			balanceInquiry.place(x=800,y=200)

			passwordChange=tkinter.Button(root,height=3,width=15,text="Password Change",font=("Arial", 15),bg='black',fg='white',command=show_change_password)
			passwordChange.place(x=800,y=300)

			fawryService=tkinter.Button(root,height=3,width=15,text="Fawry Service",font=("Arial", 15),bg='black',fg='white',command=check_id_gui)
			fawryService.place(x=800,y=400)

			exit=tkinter.Button(root,height=3,width=15,text="Exit",font=("Arial", 15),bg='black',fg='white',command=root.destroy)
			exit.place(x=800,y=500)

			welcomeLabel=tkinter.Label(root,text="Welcome "+myDict[client_id]['Name'],font=("Times new roman", 30))
			welcomeLabel.place(x=135, y=80)

			Enter2_Button=tkinter.Button(root,height=2,width=10,text="Enter",bg='green',fg='white')
			Cancel_Button=tkinter.Button(root,height=2,width=10,text="Cancel",bg='crimson',fg='white')

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
	tkinter.Label(topLevelBalance, text='Your balance is '+str(myDict[client_id]['Balance'])+' L.E',fg='green').place(x=70,y=100)
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
		myDict[client_id]['Password']=enteredPass1.get()
		topLevelPassword.destroy()
		

#main program
# Main Window Configuration
root= tkinter.Tk()
root.geometry("1000x720+250+60")
root.resizable(False,False)
root.title("Welcome to ITI bank")

IDLabel=tkinter.Label(root,text="Please enter your ID",font=("Arial", 15)) #middle position
IDLabel.place(x=390, y=200)
enteredID=tkinter.Entry(root,width=30,text=40)
enteredID.place(x=395, y=230)


Enter_Button=tkinter.Button(root,height=2,width=10,text="Enter",bg='green',fg='white',command=check_id_gui)
Close_Button=tkinter.Button(root,height=2,width=10,text="Cancel",bg='crimson',fg='white',command=root.destroy)

Enter_Button.place(x=900,y=670)
Close_Button.place(x=20,y=670)



root.mainloop()

passFlag=0
