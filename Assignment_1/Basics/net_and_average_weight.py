#Program to find net and average weight
net_weight=0
for i in range(1,6):
    weight=float(input(f"Enter the weight of person {i} in kg: "))
    net_weight+=weight
    average_weight=net_weight/5
print(f"Net Weight: {net_weight} kg")
print(f"Average Weight:{average_weight} kg")