import random
valid = []

def chooseset():
    state = input("input C for corners, E for edges\n")
    if "C" in state.upper():
        print("testing corners")
        return "corners.txt"
    else:
        print("testing edges")
        return "edges.txt"
    
def chooseletter():
    coms = f.readlines()
    sl = input("What starting letter? \n")
    for com in coms:
        if com[0] == sl:
            valid.append(com)

with open(chooseset(), "r") as f:
    chooseletter()
    while True:
        try:
            current = valid[random.randint(1, len(valid)-1)]
            print(current.split(":")[0])
            input()
            print(current)
            valid.remove(current)
        except:
            chooseletter()