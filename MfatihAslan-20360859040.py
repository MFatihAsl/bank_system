# Muhammed Fatih Aslan


import json

class Account:
    def __init__(self, account_type, account_name, amount):
        self.account_type = account_type
        self.account_name = account_name
        self.amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Hesap açıldığında negatif para miktarı girilemez.")
        self._amount = value

class Transaction:
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

class SavingAccount(Account):
    def close_account(self):
        self.amount -= self.amount * 0.1
        print(f"Hesap adı: {self.account_name}, Miktar: {self.amount}")
        return self.amount

class NormalAccount(Account):
    def close_account(self):
        print(f"Hesap adı: {self.account_name}, Miktar: {self.amount}")
        return self.amount

accounts = {}

def create_account(account_type, account_name, amount):
    if account_type == "SavingAccount":
        accounts[account_name] = SavingAccount(account_type, account_name, amount)
    elif account_type == "NormalAccount":
        accounts[account_name] = NormalAccount(account_type, account_name, amount)

def close_account(account_name):
    return accounts[account_name].close_account()

def save_accounts():
    with open('accounts.json', 'w') as f:
        json.dump(accounts, f, default=serialize_accounts)
        print("Kaydetme ve yükleme başarılı...")

def serialize_accounts(obj):
    if isinstance(obj, (SavingAccount, NormalAccount)):
        return obj.__dict__
    else:
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def load_accounts():
    global accounts
    try:
        with open('accounts.json', 'r') as f:
            accounts_data = json.load(f)
            accounts.clear()
            for account_name, account_info in accounts_data.items():
                if account_info["account_type"] == "SavingAccount":
                    accounts[account_name] = SavingAccount(account_type=account_info["account_type"],
                                                           account_name=account_info["account_name"],
                                                           amount=account_info["_amount"])
                elif account_info["account_type"] == "NormalAccount":
                    accounts[account_name] = NormalAccount(account_type=account_info["account_type"],
                                                           account_name=account_info["account_name"],
                                                           amount=account_info["_amount"])
    except FileNotFoundError:
        accounts = {}






def transaction(account_name, amount):
    accounts[account_name].amount += amount

def show_accounts():
    for account_name, account in accounts.items():
        print(f"{account_name} : {account.amount}")

while True:
    print(">>>>>>İŞLEM MENÜSÜ<<<<<<")
    print("1. Hesap oluştur. ")
    print("2. Hesap kapat. ")
    print("3. Kaydet ve yükle")
    print("4. Para çek ")
    print("5. Para yükle ")
    print("6. Göster")
    choice = input("Seçiminizi yapınız: ")

    if choice == "1":
        account_name = input("Hesap ismi giriniz: ")
        account_type = input("Hesap türü giriniz (SavingAccount veya NormalAccount): ")
        amount = float(input("Para miktarı giriniz: "))
        create_account(account_type, account_name, amount)

    elif choice == "2":
        account_name = input("Hesap ismi giriniz: ")
        print(close_account(account_name))

    elif choice == "3":
        save_accounts()
        load_accounts()

    elif choice == "4":
        try:
          account_name, amount = input("Hesap adı : miktar giriniz: ").split(" : ")
          transaction(account_name, -float(amount))
        except ValueError :
            account_name, amount = input("Hatalı tuşlama! Lütfen bu formatta yazınız...(Hesap adı : miktar): ").split(" : ")
            transaction(account_name, -float(amount))


    elif choice == "5":
        try:
          account_name, amount = input("Hesap adı : miktar giriniz: ").split(" : ")
          transaction(account_name, float(amount))
        except:
            account_name, amount = input("Hatalı tuşlama! Lütfen bu formatta yazınız...(Hesap adı : miktar): ").split(" : ")
            transaction(account_name, float(amount))

    elif choice == "6":
        show_accounts()