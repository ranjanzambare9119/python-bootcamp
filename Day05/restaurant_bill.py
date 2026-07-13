def calculate_total(price, quantity):
    return price*quantity
def calculate_gst(total):
    return total*0.18
print('==========')
print('Restaurant Bill')
print('==========')
price= int(input('Enter the price:'))
quantity= int(input('Enter the quantity:'))
amount= calculate_total(price, quantity)
print('Amount:', amount)
gst= calculate_gst(amount)
print('GST:', gst)
final_bill= amount+gst
print('Final bill:', final_bill)
