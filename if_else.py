cp=int(input("Enter cost price of product "))
sp=int(input("Enter selling price of product "))
if cp<sp:
    profit=sp-cp
    print('Profit amount is ',profit)
elif sp<cp:
    loss=cp-sp
    print('Loss amount is ',loss)
else:
    print('There is no profit and loss')
