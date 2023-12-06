#Kieran Yalla
#7/19/23
#Professor Phong Banh
#CMSC 135

a_price = 20
b_price = 15
c_price = 10

a_tickets = float(input("Enter count of A seats: "))
b_tickets = float(input("Enter count of B seats: "))
c_tickets = float(input("Enter count of C seats: "))

a_income = a_tickets * a_price
b_income = b_tickets * b_price
c_income = c_tickets * c_price
print("Income from class A seats:","$",format(a_income,'.2f'))
print("Income from class B seats:","$",format(b_income,'.2f'))
print("Income from class C seats:","$",format(c_income,'.2f'))

def show_income ():
    total_income = a_income + b_income + c_income
    print("Total income:","$",format(total_income,'.2f'))

show_income()
