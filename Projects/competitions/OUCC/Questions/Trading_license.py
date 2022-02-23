cash = int(input())
three_town_license_cost = input().split()
if int(cash/2) < int(three_town_license_cost[0]):
    cash = int(cash/2) + int(three_town_license_cost[0])
if int(cash/2) < int(three_town_license_cost[1]):
    cash = int(cash/2) + int(three_town_license_cost[1])
if int(cash/2) < int(three_town_license_cost[2]):
    cash = int(cash/2) + int(three_town_license_cost[2])
print(cash)
