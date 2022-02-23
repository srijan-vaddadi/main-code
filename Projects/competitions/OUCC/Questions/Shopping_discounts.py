money_spent = int(input())
money_taken = money_spent
if 50 < money_spent <= 100:
    money_taken = round(money_spent*0.9)
if 100 < money_spent <= 200:
    money_taken = round(money_spent*0.85)
if 200 < money_spent:
    money_taken = round(money_spent*0.8)

print(money_taken)
