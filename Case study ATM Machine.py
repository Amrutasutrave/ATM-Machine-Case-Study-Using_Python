'''
ATM Machine case study

1.Deposit Money
2.Withraw cash
3.View balance
4.Exit

1.Deposit money
2.Withdraw money
3.View balance
4.Exit

1.Deposit money:
a)amount to be deposited
b)increment the balance

2.Withdraw money:
a)amount to be withdrawn
b)Check bal
c)decrement the balance
'''
#code
print("ATM MAchine Task!!!")
print("Enter your choice")
ch=int(input("Press \n 1 to Deposit Money,\n 2 to Withdraw Money, \n 3 to View Balance, \n 4 to Exit \n"))
bal=100000
if ch==1: #deposit money
    amt=int(input("\n Enter Amont To Deposit"))
    bal=bal+amt
    print(bal)
    print("Amount Deposited Successfully!!!")
    ch=int(input("Press \n 1 to Deposit Money,\n 2 to Withdraw Money, \n 3 to View Balance, \n 4 to Exit \n"))
elif ch==2: #withdraw money
    amt=int(input("\n Enter Amount To Withdraw"))
    if amt>bal:
        print("Amount Exceeding Balance!!!")
    else:
        bal=bal-amt
        print("Amount Debited Successfully!!!")
        #print(bal)
elif ch==3: #view balance
    print("You Balance is:", bal)
elif ch==4: #exit
    #print("Byeee!!!")
    exit() #directly Throw You out Of Console
else:
    print("Invalid input")
     
