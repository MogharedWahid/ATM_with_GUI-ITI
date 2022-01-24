#**********************************  Moghared Wahid  ************************************/
#******************************  mogharedwahid@gmail.com  *******************************/
#*********************************  ATM project - ITI  **********************************/
#****************************************************************************************/

from distutils import command
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
	passLabel=tkinter.Label(text="Please enter your password")
	passLabel.place(x=20, y=80)
	passAttempts=tkinter.Label(text=str(attempts)+" attempts left")
	passAttempts.place(x=50, y=120)
	global enteredPass
	enteredPass=tkinter.Entry(root,show='*')
	enteredPass.place(x=50, y=100)
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
	client_pass = int(enteredPass.get())
	if(check_password(client_id,client_pass)):
			Enter_Button.destroy()
			Close_Button.destroy()
			IDLabel.destroy()
			passLabel.destroy()
			enteredID.destroy()
			enteredPass.destroy()
			passAttempts.destroy()

			cashWithdraw=tkinter.Button(root,height=5,width=20,text="Cash Withdraw",bg='black',fg='white',command=check_id_gui)
			cashWithdraw.place(x=800,y=100)

			balanceInquiry=tkinter.Button(root,height=5,width=20,text="Balance Inquiry",bg='black',fg='white',command=check_id_gui)
			balanceInquiry.place(x=800,y=200)

			passwordChange=tkinter.Button(root,height=5,width=20,text="Password Change",bg='black',fg='white',command=check_id_gui)
			passwordChange.place(x=800,y=300)

			fawryService=tkinter.Button(root,height=5,width=20,text="Fawry Service",bg='black',fg='white',command=check_id_gui)
			fawryService.place(x=800,y=400)

			exit=tkinter.Button(root,height=5,width=20,text="Exit",bg='black',fg='white',command=check_id_gui)
			exit.place(x=800,y=500)

			welcomeLabel=tkinter.Label(root,text="Welcome "+myDict[client_id]['Name'],font=("Arial", 25))
			welcomeLabel.place(x=200, y=100)
			
	


  			
			  	
#function that display balance
def check_id_gui():
  global client_id
  client_id = int(enteredID.get())
  idFlag=check_id(client_id)
  if(idFlag):
    show_password_field()
  else:
    show_invalidID_field()
  


#main program
# Window Configuration
root= tkinter.Tk()
root.geometry("1000x720+250+60")
root.resizable(False,False)
root.title("Welcome to ITI bank")

IDLabel=tkinter.Label(root,text="Please enter your ID")
IDLabel.place(x=20, y=20)
enteredID=tkinter.Entry(root,text=20)
enteredID.place(x=50, y=50)


Enter_Button=tkinter.Button(root,height=2,width=10,text="Enter",bg='green',fg='black',command=check_id_gui)
Close_Button=tkinter.Button(root,height=2,width=10,text="Cancel",bg='red',fg='black',command=root.destroy)

Enter_Button.place(x=900,y=670)
Close_Button.place(x=20,y=670)



root.mainloop()

passFlag=0
