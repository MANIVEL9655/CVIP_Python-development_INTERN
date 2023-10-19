cost_per_packet=float(input("enter the input cost per packet"))
num_packets=int(input("enter the input number of packet"))
total_cost=cost_per_packet*num_packets
given_amount=20
change=given_amount-total_cost
print("The shopkeeper will you give us",change)
