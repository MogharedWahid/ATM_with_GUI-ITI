#**********************************  Moghared Wahid  ************************************/
#******************************  mogharedwahid@gmail.com  *******************************/
#*********************************  ATM project - ITI  **********************************/
#****************************************************************************************/

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
#kosm el khara
#function that checks the entered password
def check_password(client_id):
	password,attempts=0,0
	while password != myDict[client_id]['Password'] and attempts<3:
		password=int(input("Enter your password:"))
		attempts+=1
		if(password != myDict[client_id]['Password']):
			print("Wrong password, ",end=' ')
	if(password == myDict[client_id]['Password'] and attempts <= 3 ):
		return 1
	else:
		myDict[client_id]['Locked']=1
		return 0
		
#function that display balance
def check_id_gui():
	client_id=int(enteredID.get())
	idFlag=check_id(client_id)
	if(idFlag==1):
		# passFlag=check_password(client_id)
		print("true")
	else:
		print("false")
	# 	print("Welcome "+myDict[client_id]['Name'])
	# print("End")
	# print(myDict[client_id]['Locked'])


#main program
# Window Configuration
root= tkinter.Tk()
root.geometry("1000x720+250+60")
root.resizable(False,False)
root.title("Welcome to ITI bank")

IDLabel=tkinter.Label(text="Please enter your ID").place(x=20, y=20)
enteredID=tkinter.Entry(root,text=20)
enteredID.place(x=50, y=50)

# nameLabel=tkinter.Label(text="Please enter your password").place(x=20, y=80)
# enteredPass=tkinter.Entry(root,show='*')
# enteredPass.place(x=50, y=100)

Enter_Button=tkinter.Button(root,height=2,width=10,text="Enter",bg='green',fg='black',command=check_id_gui)
Close_Button=tkinter.Button(root,height=2,width=10,text="Cancel",bg='red',fg='black',command=root.destroy)

Enter_Button.place(x=900,y=670)
Close_Button.place(x=20,y=670)



root.mainloop()

passFlag=0
