Amount_Due = 50

while Amount_Due > 0:
    
    print(f"Amount Due: {Amount_Due}")
    coin = int(input("Insert Coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        Amount_Due = Amount_Due - coin

print(f"Change Owed: {-Amount_Due}")
