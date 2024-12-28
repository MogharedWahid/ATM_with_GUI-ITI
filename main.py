#***************************************************************************************#
#*************************|  Author	  : Moghared Wahid           |******************#
#*************************|  Email	  : mogharedwahid@gmail.com  |******************#
#*************************|  Project  	  : ATM - ITI  		     |******************#
#***************************************************************************************#

import tkinter as tk

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x720+250+60")
        self.root.resizable(False, False)
        self.root.title("Welcome to ITI bank")
        
        self.myDict = {
            215321701332: {'Name': 'Moghared Wahid', 'Password': 1783, 'Balance': 3500166, 'Locked': 0},
            203659302214: {'Name': 'Salma Mohamed', 'Password': 1390, 'Balance': 520001, 'Locked': 0},
            126355700193: {'Name': 'Adel Khaled', 'Password': 1214, 'Balance': 111000, 'Locked': 0},
            201455998011: {'Name': 'Saeed Amin', 'Password': 2001, 'Balance': 1200, 'Locked': 0},
            201122369851: {'Name': 'Amir Salama', 'Password': 8935, 'Balance': 178933, 'Locked': 0},
            201356788002: {'Name': 'Wael Mohamed', 'Password': 3420, 'Balance': 55000, 'Locked': 0},
            203366789564: {'Name': 'Mina Sameh', 'Password': 1179, 'Balance': 18000, 'Locked': 0},
            201236787812: {'Name': 'Omnia Ahmed', 'Password': 1430, 'Balance': 180350, 'Locked': 0}
        }
        
        self.attempts = 3
        self.client_id = None
        self.Entry_point()

    def Entry_point(self):
        self.welcomeBank = tk.Label(self.root, text="Welcome to ITI bank", font=("Times new roman", 40))
        self.welcomeBank.place(x=250, y=80)
        
        self.IDLabel = tk.Label(self.root, text="Please enter your ID", font=("Arial", 15))
        self.IDLabel.place(x=390, y=250)
        
        self.enteredID = tk.Entry(self.root, width=30)
        self.enteredID.place(x=395, y=280)
        
        self.Enter_Button = tk.Button(self.root, height=2, width=10, text="Enter", bg='green', fg='white', command=self.check_id_gui)
        self.Enter_Button.place(x=900, y=670)

    def check_id(self, client_id):
        if client_id in self.myDict:
            if self.myDict[client_id]['Locked'] == 1:
                return 2
            else:
                return 1
        else:
            return 0

    def show_password_field(self):
        self.passLabel = tk.Label(self.root, text="Please enter your password", font=("Arial", 15))
        self.passLabel.place(x=390, y=310)
        
        self.passAttempts = tk.Label(self.root, text=f"{self.attempts} attempts left")
        self.passAttempts.place(x=395, y=365)
        
        self.enteredPass = tk.Entry(self.root, width=30, show='*')
        self.enteredPass.place(x=395, y=345)
        
        self.Enter_Button.configure(command=self.check_password_gui)

    def show_invalidID_field(self):
        topLevelID = tk.Toplevel()
        topLevelID.geometry("300x250+600+350")
        tk.Label(topLevelID, text='Invalid ID!', font=("Arial", 15), fg='red').place(x=100, y=100)
        OKButton = tk.Button(topLevelID, text='Confirm', fg='white', bg='black', command=topLevelID.destroy)
        OKButton.place(x=200, y=190)

    def show_invalidPass_field(self):
        topLevelVar = tk.Toplevel()
        topLevelVar.geometry("300x250+600+350")
        tk.Label(topLevelVar, text='Your account has been blocked!', font=("Arial", 13), fg='red').place(x=20, y=100)
        OKButton = tk.Button(topLevelVar, text='Confirm', fg='white', bg='black', command=topLevelVar.destroy)
        OKButton.place(x=200, y=190)

    def show_Locked_field(self):
        topLevelLocked = tk.Toplevel()
        topLevelLocked.geometry("300x250+600+350")
        tk.Label(topLevelLocked, text='Sorry your account has been locked!', font=("Arial", 13), fg='red').place(x=10, y=90)
        tk.Label(topLevelLocked, text='Please head to the bank!', font=("Arial", 13), fg='red').place(x=50, y=120)
        OKButton = tk.Button(topLevelLocked, text='Confirm', fg='white', bg='black', command=topLevelLocked.destroy)
        OKButton.place(x=200, y=190)

    def check_password(self, client_id, client_pass):
        if client_pass == self.myDict[client_id]['Password']:
            return 1
        elif self.attempts == 1:
            self.myDict[client_id]['Locked'] = 1
            self.destroy_entry()
            self.Entry_point()
            self.show_invalidPass_field()
        else:
            self.attempts -= 1
            self.passAttempts.configure(text=f"Wrong password {self.attempts} attempts left")

    def check_password_gui(self):
        try:
            client_pass = int(self.enteredPass.get())
            if self.check_password(self.client_id, client_pass):
                self.show_main_menu()
        except ValueError:
            self.passAttempts.configure(text="Invalid password format")

    def show_main_menu(self):
        self.Enter_Button.destroy()
        self.IDLabel.destroy()
        self.passLabel.destroy()
        self.enteredID.destroy()
        self.enteredPass.destroy()
        self.passAttempts.destroy()
        self.welcomeBank.destroy()

        self.cashWithdraw = tk.Button(self.root, height=3, width=15, text="Cash Withdraw", font=("Arial", 15), bg='black', fg='white', command=self.show_cash_field)
        self.cashWithdraw.place(x=270, y=280)

        self.balanceInquiry = tk.Button(self.root, height=3, width=15, text="Balance Inquiry", font=("Arial", 15), bg='black', fg='white', command=self.show_balance)
        self.balanceInquiry.place(x=600, y=280)

        self.passwordChange = tk.Button(self.root, height=3, width=15, text="Password Change", font=("Arial", 15), bg='black', fg='white', command=self.show_change_password)
        self.passwordChange.place(x=270, y=380)

        self.fawryService = tk.Button(self.root, height=3, width=15, text="Fawry Service", font=("Arial", 15), bg='black', fg='white', command=self.fawry)
        self.fawryService.place(x=600, y=380)

        self.exit = tk.Button(self.root, height=3, width=15, text="Exit", font=("Arial", 15), bg='black', fg='red', command=self.Back_to_entery)
        self.exit.place(x=435, y=480)

        self.welcomeLabel = tk.Label(self.root, text=f"Welcome {self.myDict[self.client_id]['Name']}", font=("Times new roman", 40))
        self.welcomeLabel.place(x=210, y=80)

        self.serviceLabel = tk.Label(self.root, text="Choose your service:", font=("Times new roman", 15))
        self.serviceLabel.place(x=425, y=200)

    def check_id_gui(self):
        try:
            self.client_id = int(self.enteredID.get())
            idFlag = self.check_id(self.client_id)
            if idFlag == 1:
                self.show_password_field()
            elif idFlag == 0:
                self.show_invalidID_field()
            elif idFlag == 2:
                self.destroy_entry()
                self.Entry_point()
                self.show_Locked_field()
        except ValueError:
            self.show_invalidID_field()

    def show_cash_field(self):
        self.topLevelWithdraw = tk.Toplevel()
        self.topLevelWithdraw.geometry("300x250+600+350")

        self.cashLabel = tk.Label(self.topLevelWithdraw, text="Please enter cash amount:", font=("Arial", 10))
        self.cashLabel.place(x=15, y=10)
        
        self.enteredCash = tk.Entry(self.topLevelWithdraw, width=10)
        self.enteredCash.place(x=30, y=40)
        
        self.maxTransaction = tk.Label(self.topLevelWithdraw, text="- Max. transaction is 5000 L.E!", fg='black')
        self.maxTransaction.place(x=15, y=70)
        
        self.multipleHundred = tk.Label(self.topLevelWithdraw, text="- The allowed values are only multiples of 100 L.E!", fg='black')
        self.multipleHundred.place(x=15, y=90)
        
        self.noSufficient = tk.Label(self.topLevelWithdraw, text="- Balance should be more than your amount!", fg='black')
        self.noSufficient.place(x=15, y=110)
        
        confirmButton = tk.Button(self.topLevelWithdraw, text='Confirm', fg='white', bg='black', command=self.cash_check)
        confirmButton.place(x=200, y=190)
        
        cancelButton = tk.Button(self.topLevelWithdraw, text='Cancel', fg='white', bg='black', command=self.topLevelWithdraw.destroy)
        cancelButton.place(x=70, y=190)

    def cash_check(self):
        try:
            client_entered_cash = int(self.enteredCash.get())
            maxTrans = client_entered_cash <= 5000
            multipleHund = client_entered_cash % 100 == 0
            noSufficin = self.myDict[self.client_id]['Balance'] > client_entered_cash

            self.maxTransaction.configure(fg='green' if maxTrans else 'red')
            self.multipleHundred.configure(fg='green' if multipleHund else 'red')
            self.noSufficient.configure(fg='green' if noSufficin else 'red')

            if maxTrans and multipleHund and noSufficin:
                self.topLevelWithdraw.destroy()
                self.ATM_Actuator_Out()
                self.myDict[self.client_id]['Balance'] -= client_entered_cash
                self.show_transaction_done()
        except ValueError:
            self.maxTransaction.configure(fg='red')
            self.multipleHundred.configure(fg='red')
            self.noSufficient.configure(fg='red')

    def ATM_Actuator_Out(self):
        print("ATM Actuator Out")

    def show_transaction_done(self):
        topLevelTransaction = tk.Toplevel()
        topLevelTransaction.geometry("300x250+600+350")
        tk.Label(topLevelTransaction, text='Transaction done. Thank you :)', fg='green').place(x=70, y=100)
        ReturnButton = tk.Button(topLevelTransaction, text='Return', fg='white', bg='black', command=topLevelTransaction.destroy)
        ReturnButton.place(x=125, y=150)

    def show_balance(self):
        topLevelBalance = tk.Toplevel()
        topLevelBalance.geometry("300x250+600+350")
        tk.Label(topLevelBalance, text=f'Your balance is {self.myDict[self.client_id]["Balance"]} L.E', font=("Arial", 10)).place(x=70, y=100)
        ReturnButton = tk.Button(topLevelBalance, text='Return', fg='white', bg='black', command=topLevelBalance.destroy)
        ReturnButton.place(x=200, y=190)

    def show_change_password(self):
        self.passMatch = 0
        self.passLen = 0

        self.topLevelPassword = tk.Toplevel()
        self.topLevelPassword.geometry("300x250+600+350")
        
        PassLabel = tk.Label(self.topLevelPassword, text="Enter new password", font=("Arial", 10))
        PassLabel.place(x=20, y=30)
        
        self.enteredPass1 = tk.Entry(self.topLevelPassword, width=10, show='*')
        self.enteredPass1.place(x=170, y=32)
        
        PassLabe2 = tk.Label(self.topLevelPassword, text="Re-enter new password", font=("Arial", 10))
        PassLabe2.place(x=20, y=55)
        
        self.enteredPass2 = tk.Entry(self.topLevelPassword, width=10, show='*')
        self.enteredPass2.place(x=170, y=57)
        
        confirmButton = tk.Button(self.topLevelPassword, text='Confirm', fg='white', bg='black', command=self.check_change_password)
        confirmButton.place(x=200, y=190)
        
        cancelButton = tk.Button(self.topLevelPassword, text='Cancel', fg='white', bg='black', command=self.topLevelPassword.destroy)
        cancelButton.place(x=70, y=190)
        
        self.passCondition1 = tk.Label(self.topLevelPassword, text="- Password should be four digits!", fg='black')
        self.passCondition1.place(x=30, y=100)
        
        self.passCondition2 = tk.Label(self.topLevelPassword, text="- The two passwords should match!", fg='black')
        self.passCondition2.place(x=30, y=120)

    def check_change_password(self):
        pass1 = self.enteredPass1.get()
        pass2 = self.enteredPass2.get()

        self.passLen = len(pass1) == 4 and len(pass2) == 4
        self.passMatch = pass1 == pass2

        self.passCondition1.configure(fg='green' if self.passLen else 'red')
        self.passCondition2.configure(fg='green' if self.passMatch else 'red')

        if self.passMatch and self.passLen:
            self.myDict[self.client_id]['Password'] = int(pass1)
            self.topLevelPassword.destroy()

    def fawry(self):
        self.Vo = 0
        self.Or = 0
        self.Et = 0
        self.We = 0

        self.topLevelFawry = tk.Toplevel()
        self.topLevelFawry.geometry("300x250+600+350")
        
        PassLabel = tk.Label(self.topLevelFawry, text="Choose your network:", font=("Arial", 10))
        PassLabel.place(x=15, y=10)
        
        Vodafone = tk.Button(self.topLevelFawry, height=1, width=6, text="Vodafone", font=("Arial", 10), bg='white', fg='red', command=self.vodafone_chosen)
        Vodafone.place(x=15, y=40)
        
        Etisalat = tk.Button(self.topLevelFawry, height=1, width=6, text="Etisalat", font=("Arial", 10), bg='white', fg='green', command=self.etisalat_chosen)
        Etisalat.place(x=85, y=40)
        
        Orange = tk.Button(self.topLevelFawry, height=1, width=6, text="Orange", font=("Arial", 10), bg='white', fg='orange', command=self.orange_chosen)
        Orange.place(x=155, y=40)
        
        We = tk.Button(self.topLevelFawry, height=1, width=6, text="We", font=("Arial", 10), bg='white', fg='purple', command=self.we_chosen)
        We.place(x=225, y=40)
        
        confirmButton = tk.Button(self.topLevelFawry, text='Confirm', fg='white', bg='black', command=self.check_fawry)
        confirmButton.place(x=200, y=190)
        
        cancelButton = tk.Button(self.topLevelFawry, text='Cancel', fg='white', bg='black', command=self.topLevelFawry.destroy)
        cancelButton.place(x=70, y=190)

    def vodafone_chosen(self):
        self.Vo = 1
        self.setup_fawry_interface("010")

    def etisalat_chosen(self):
        self.Et = 1
        self.setup_fawry_interface("011")

    def orange_chosen(self):
        self.Or = 1
        self.setup_fawry_interface("012")

    def we_chosen(self):
        self.We = 1
        self.setup_fawry_interface("015")

    def setup_fawry_interface(self, prefix):
        self.fawry_Label = tk.Label(self.topLevelFawry, text="Enter your phone number:", font=("Arial", 10))
        self.fawry_Label.place(x=15, y=70)
        
        self.fawry_initial = tk.Label(self.topLevelFawry, text=prefix, font=("Arial", 10))
        self.fawry_initial.place(x=70, y=90)
        
        self.enterednum = tk.Entry(self.topLevelFawry, width=8)
        self.enterednum.place(x=95, y=91)
        
        cash_Label = tk.Label(self.topLevelFawry, text="Enter recharge amount:", font=("Arial", 10))
        cash_Label.place(x=15, y=110)
        
        self.enteredcash = tk.Entry(self.topLevelFawry, width=8)
        self.enteredcash.place(x=95, y=130)

    def check_fawry(self):
        try:
            phone_number = self.enterednum.get()
            recharge_amount = int(self.enteredcash.get())

            if len(phone_number) == 8 and recharge_amount < self.myDict[self.client_id]['Balance']:
                self.myDict[self.client_id]['Balance'] -= recharge_amount
                self.topLevelFawry.destroy()
            else:
                self.show_fawry_error(phone_number, recharge_amount)
        except ValueError:
            self.show_fawry_error("", 0)

    def show_fawry_error(self, phone_number, recharge_amount):
        if len(phone_number) != 8:
            num_label = tk.Label(self.topLevelFawry, text="Invalid phone number!", fg='red')
            num_label.place(x=15, y=150)
        if recharge_amount > self.myDict[self.client_id]['Balance']:
            cash_label = tk.Label(self.topLevelFawry, text="Not enough balance!", fg='red')
            cash_label.place(x=15, y=165)

    def destroy_entry(self):
        self.IDLabel.destroy()
        self.enteredID.destroy()
        self.passLabel.destroy()
        self.enteredPass.destroy()
        self.passAttempts.destroy()

    def Back_to_entery(self):
        self.cashWithdraw.destroy()
        self.balanceInquiry.destroy()
        self.passwordChange.destroy()
        self.fawryService.destroy()
        self.exit.destroy()
        self.welcomeLabel.destroy()
        self.serviceLabel.destroy()
        self.Entry_point()

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
