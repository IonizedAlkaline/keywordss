bill = 100
print(bill)
amountpaid = 0


def calcdue(bill, amountpaid):
    return bill - amountpaid


while True:
    print("current total bill", bill)
    print("amount paid", amountpaid)
    payment = int(input("how much are you going to pay: "))
    amountpaid += payment
    dueamount = calcdue(bill, amountpaid)
    if dueamount > 0:
        print("you still owe", dueamount)
    elif dueamount < 0:
        print("you have overpaid", dueamount)
    else:
        print("the bill is fully paid")
        break
