import sys

def usage():
    message = '''Usage:
    {} ARGUMENT...'''.format(sys.argv[0])
    print(message, file=sys.stderr)

def animalPrint(items):
    animals = [ "😸", "🐶", "🐸" ]
    for i in range(len(items)):
        print(animals[i % len(animals)], items[i])
