old_price=[23,4,5,80,2,60,78,92,678,90]
rs=5
def add_price(no):
    return no+5
new_price=map(add_price,old_price)
new_price1=list(map(lambda n:n+rs,old_price))
print(new_price1)