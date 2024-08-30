def date_search(transaction,target):
    for n in transaction:
        target=input("enter the target ")
        if n["date"]==target:
            return n
def bubble_sort(transaction):
    n=len(transaction)
    for i in range (n):
        for j in range (0,n-1): 
            if int(transaction[j]["amount"])>transaction[j+1]["amount"]:
                transaction[j],transaction[j+1]=transaction[j+1],transaction[j]
    return transaction
# deleting the data of the particular date by taking the input
def delete_data(transaction,date):
    for i in transaction:
        if i["date"]==date:
            transaction.remove(i)
        return transaction

def add_data(transaction):
    date=input("enter the date ")
    amount=int(input("enter the amount"))
    description=input("enter the description")
    new_transaction={"date":date,"amount":amount,"description":description}
    transaction.append(new_transaction)
    return transaction
def add_amount (transaction):
    year=input("enter the year")
    intsum=0
    for i in transaction:
        if i["date"][0:4]==year:
            intsum+=i['amount']
    return intsum
