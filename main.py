from features import date_search,bubble_sort,delete_data,add_data,add_amount
transaction=[{"date":"2024-08-2","amount":2000,"description":"fruits"},
             {"date":"2024-7-20","amount":3000,"description":"current bill"},
             {"date":"2024-3-24","amount":10000,"description":"home rent"},
             {"date":"2024-4-18","amount":5000,"description":"EMI"},
              {"date":"2024-8-6","amount":5000,"description":"monthly shooping"}]
flag=True
while flag:
    print("1.add")
    print("2.search")
    print("3.sort")
    print("4.delete")
    print("5.display")
    print("6.stop")
    print("7.sum amount")
    

    a=int(input("enter the value"))
    if a==1:
        print("-"*50)
        print("adding data ")
        transaction=add_data(transaction)
        print("-"*50)
    elif a==2: 
        print("-"*50)
        print("searching data ")
        transaction=date_search(transaction)
        print("-"*50)
    elif a==3: 
        print("-"*50)
        print("sorting data ")
        transaction=bubble_sort(transaction)
        print("-"*50)
    elif a==4: 
        print("-"*50)
        print("deleting data ")
        transaction=delete_data(transaction)
        print("-"*50)
    elif a==5:
        print(transaction)
    elif a==6:
        flag=False
    elif a==7:
        print("-"*50)
        print("adding amount")
        print(add_amount(transaction))

    else:
        print("please enter the valid choice")
