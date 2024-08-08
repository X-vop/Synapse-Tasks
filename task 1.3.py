request_spending = {
    "Mahek":{
        "balance":3000.00 ,
        "transactions": [
            {"amount":-9000.000 , "category":"Creatives"},{"amount":7000.00 , "category":"Sponsor"},{"amount":-2000.00 , "category":"Prize-Money"}
        ]
    },
    "Arham":{
        "balance":5000.00 ,
        "transactions": [

            {"amount":8000.00 , "category":"Stalls"},{"amount":7500.00 , "category":"Seminars"}
        ]
    },
    "Unnati":{
        "balance":3500.00 ,
        "transactions": [
            {"amount":-5000.00 , "category":"Attraction"},{"amount":2500.00 , "category":"Promo"},{"amount":-900.00 , "category":"Lighting"},{"amount":-3000.00 , "category":"Games"}
        ]
    },
    "Gaurang":{
        "balance":2000.00 ,
        "transactions": [
            {"amount":-1500.00 , "category":"Website"},{"amount":-1000.00 , "category":"C2C"},{"amount":-500.00 , "category":"Posters"}
        ]
    },
}

def total_spending(request_spending, account_id:str, category:str):
    for transaction in (request_spending[account_id]["transactions"]):
        if category == transaction["category"]:
               return int(transaction["amount"])
#total_spending(request_spending,"Mahek","Creatives")

def account_balance(request_spending, account_id: str):
    z= request_spending[account_id].get("balance")
    return float(z)
#acc_bal= account_balance(request_spending,"Mahek")

def money_owed(request_spending, account_id:str):
    global acc_bal
    acc_bal= account_balance(request_spending, account_id)
    for transaction in request_spending[account_id]["transactions"]:
        part = transaction["amount"]
        acc_bal = part + acc_bal
    return float(acc_bal)


#acc_id = input("Enter name of member: ")
#catgry = input("Enter the category:")
ops = input("Enter number of task to be carried out: 1- find total spending, 2- find account balance, 3- find money owed")
if(ops=="1"):
    acc_id = input("Enter name of member (Mahek , Gaurang, Unnati, Arham): ")
    catgry = input("Enter the category:")
    total_spent = total_spending(request_spending, acc_id, catgry)
    print(total_spent)
elif (ops == "2"):
    acc_id = input("Enter name of member (Mahek , Gaurang, Unnati, Arham): ")
    acc_bal = account_balance(request_spending, acc_id)
    print(acc_bal)
elif (ops == "3"):
    acc_id = input("Enter name of member (Mahek , Gaurang, Unnati, Arham): ")
    total = money_owed(request_spending, acc_id)
    print(total)
else:
    print("Please enter valid number: ")








