from replit import clear

bids_total = []
while True:
    name = str(input("What is your name: "))
    bid = int(input("What is your bid: "))

    bids = {
        name: bid,
    }
    bids_total.append(bids)

  

    answer = input("Is there any other user? y/n")

    if answer == "n":
        high = 0
        name = ""
        for person in bids_total:
            for item in person:
                if person[item] > high:
                    high = person[item]
                    name = item
        print(f"{name} a bidder le plus haut avec {high}")
        break

    clear()