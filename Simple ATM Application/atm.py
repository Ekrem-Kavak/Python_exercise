print("""
\t\t****** Welcome to XBANK ******
\tPlease insert your card. """)

atm_server = {"Ekrem_account":{
    "name": "Ekrem",
    "surname": "Kvk",
    "password": "3456",
    "balance": 20000,
    "debt": 3000,
    "debt_date": "23.09.2024"},
        "Mehmet_account":{
    "name": "Mehmet",
    "surname": "Dağ",
    "password": "1234",
    "balance": 50000,
    "debt": 40000,
    "debt_date": "28.07.2024"}
}

card = dict(atm_server["Ekrem_account"])

claim = 2
for i in range(0,3):
    password = input("Please, enter your 4 digit password")
    if (password == card.get("password")):
        print("""Welcome {} please, select the account action you want to make.""".format(card.get("name"),card.get("surname")))
    enter = input("""
    [1]- Account balance inquiry 
    [2]- Credit card debt inquiry
    [3]- Withdraw money
    [4]- Deposit money
    [Q]- return card"""
    )



