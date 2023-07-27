def usage():
    print("Please give some arguments")

def animalPrint(items):
    animals = [ "😸", "🐶", "🐸" ]
    for i in range(len(items)):
        print(animals[i % len(animals)], items[i])
