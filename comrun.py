import random
import time

tested = 0
failed = 0
failedcoms = []

def chooseset():
    state = input("input C for corners, E for edges\n")
    if "C" in state.upper():
        print("testing corners")
        return "corners.txt"
    else:
        print("testing edges")
        return "edges.txt"

with open(chooseset(), "r") as f:
    algs = f.readlines()
    while len(algs) > 0:
        alg = algs[random.randint(0, len(algs)-1)]
        print(alg.split(":")[0] + "\n")
        algs.remove(alg)
        answer = input("\n")
        tested += 1
        if answer.lower() == "n":
            print(alg)
            failed += 1
            failedcoms.append(alg)
    
    print("com run completed! " + "\n" + str(378-failed + " coms successfully recalled"))
    time.sleep(5)
    print(failedcoms)