import datetime
import os

class account:
    def __init__(self,an,n,pn,b=0):
        self.an = an
        self.n = n
        self.pn = pn
        self.b = b
    def create_account(self):
        try:
            with open(f"{self.an}_passbook.txt","w+") as f:
                f.write('Bank Name : Virtual Bank of Silicon Valley\n')
                f.write(f'Account Number : {self.an}\n')
                f.write(f'Name : {self.n}\n')
                f.write(f'Phone number : {self.pn}\n')
                f.write('Bank IFSC Code : BANK0000\n')
                f.write(f"Account Balance : {self.b}\n")
                f.write('All Transactions :\n')
                f.write(f"Transaction           | DATE       | Balance")
            print('Account created successfully !!')
        except Exception:
            print("Couldn't create your account !!")
    def manage_transactions(self,credit=None,debit=None):
        try:
            with open(f"{self.an}_passbook.txt", "r") as f:
                lines = f.readlines()
            if credit:
                for i, line in enumerate(lines):
                    if line.startswith('Account Balance :'):
                        self.b = float(line.split(":")[1].strip())
                        lines[i] = f'Account Balance : {self.b+credit}\n'
                print(f"Amount {credit}Rs credited successfully to account number {self.an} !")
            if debit:
                for i, line in enumerate(lines):
                    if line.startswith('Account Balance :'):
                        self.b = float(line.split(":")[1].strip())
                        lines[i] = f'Account Balance : {self.b-debit}\n'
                print(f"Amount {debit}Rs debited from account number {self.an} !")
            with open(f"{self.an}_passbook.txt", "w") as f:
                f.writelines(lines)
            if credit:
                with open(f"{self.an}_passbook.txt", "a") as f:
                    f.write(f"\nCredit : Rs{credit} | {datetime.date.today()} | {self.b + credit}")
            else:
                with open(f"{self.an}_passbook.txt", "a") as f:
                    f.write(f"\nDebit  : Rs{debit} | {datetime.date.today()} | {self.b - debit}")
        except Exception:
            print("Transaction Unsuccessful !!")
    def print_passbook(self):
        try:
            with open(f"{self.an}_passbook.txt", "r") as f:
                passbook_content = f.read()
                print("Passbook for Account Number:", self.an)
                print(passbook_content)
        except FileNotFoundError:
            print("Passbook not found for the account. Please create an account first.")
        except Exception as e:
            print("Error occurred while printing passbook:", str(e))
    def update_details(self, new_name=None, new_num=None):
        try:
            with open(f"{self.an}_passbook.txt", "r") as f:
                lines = f.readlines()
            if new_name:
                for i, line in enumerate(lines):
                    if line.startswith('Name :'):
                        lines[i] = f'Name : {new_name}\n'
            if new_num:
                for i, line in enumerate(lines):
                    if line.startswith('Phone number :'):
                        lines[i] = f'Phone number : {new_num}\n'
            with open(f"{self.an}_passbook.txt", "w") as f:
                f.writelines(lines)
            print('Account details updated successfully !!')
        except Exception:
            print("Couldn't update your account details !!")

def new_account():
    global count
    print('New account entry -')
    while True:
        acc_num = input('Enter 5 digit account number: ')
        if len(str(acc_num)) != 5 or not acc_num.isdigit():
            print('Account number must have 5 digits!')
        else: break
    while True:
        name = input('Enter full name of account holder : ')
        if not name:
            print('Please enter your name !')
        else: break
    while True:
        phone_num = input('Enter phone number: ')
        if len(str(phone_num)) != 10 or not phone_num.isdigit():
            print('Enter a valid 10-digit phone number!')
        else: break
    new = account(acc_num,name.title(),phone_num)
    new.create_account()

def account_transactions():
    print("Transaction request - ")
    acc_num = int(input('Enter account number : '))
    acc_transaction = account(acc_num, "", "")
    command = input("Enter 'c' to credit money or 'd' to debit money : ")
    if command == 'c':
        cred_amt = float(input('Enter amount to credit : Rs'))
        acc_transaction.manage_transactions(credit=cred_amt)
    elif command == 'd':
        deb_amt = float(input('Enter amount to debit : Rs'))
        acc_transaction.manage_transactions(debit=deb_amt)
    else:
        print('Invalid command !!')

def print_account_passbook():
    print("Passbook print request - ")
    acc_num = int(input('Enter account number : '))
    acc = account(acc_num, "", "")
    acc.print_passbook()

def change_details():
    print('Account details change request -')
    acc_num = int(input('Enter account number : '))
    acc_update = account(acc_num, "", "")
    command = input("Enter 'n' to change name or 'p' to change phone number : ")
    if command=='n':
        new_name = input('Enter new name : ')
        acc_update.update_details(new_name=new_name)
    elif command=='p':
        new_num = input('Enter new phone number : ')
        acc_update.update_details(new_num=new_num)
    else: print('Invalid command !!')

def delete_account():
    print("Account deletion request -")
    acc_num = int(input("Enter account number to delete: "))
    passbook_file = f"{acc_num}_passbook.txt"
    try:
        os.remove(passbook_file)
        print(f"Account with account number {acc_num} has been deleted successfully!")
    except FileNotFoundError:
        print(f"Account {acc_num} not found.")
    except Exception as e:
        print("Error occurred while deleting the account:", str(e))

def search_disp_accounts(x):
    try:
        dir_path = r'A:\programming\Python\pycharm projects\Virtual Bank'
        accounts = []
        for file in os.listdir(dir_path):
            if file.endswith('.txt'):
                accounts.append(file)
            else:
                continue
        accounts.sort()
        if x=='s':
            print('Yet to code !!')
        elif x=='d':
            for account in accounts: print(account)
    except Exception as e:
        print("An error occurred:", str(e))

print('Virtual Bank of Silicon Valley')
print("""ADMIN's Window -
1. Create new account (enter n)
2. Manage account transactions (enter t)
3. Print passbook (enter p)
4. Update account details (enter u)
5. Delete an account (enter d)
6. Search an account (enter s)
7. Display all accounts (enter a)
8. Exit menu (enter e)""")
command = input('Enter command : ')
while command!='e':
    if command=='n':
        new_account()
    elif command=='t':
        account_transactions()
    elif command=='p':
        print_account_passbook()
    elif command=='u':
        change_details()
    elif command=='d':
        delete_account()
    elif command=='s':
        search_disp_accounts('s')
    elif command=='a':
        search_disp_accounts('d')
    else:
        print('Invalid command !!')
    command = input('Enter command : ')
print('Goodbye !')