import random

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
    specificcases = "y" in input("test specific cases? (y/n)").lower()
    flag = any([("#" in alg) for alg in algs])
    if not specificcases:  
        print("testing all cases")
    elif flag:
        print("testing specific cases")
    else:
        print("no tagged cases found in algs, please tag cases or test all cases")
        exit()
    while True:
        alg = (algs[random.randint(0, (len(algs)-1))])
        if flag and specificcases and not alg.startswith("#"):
            continue 
        print(alg.split(":")[0][-2:])
        answer = input("\n")
        if answer.lower() == "n":
            print(alg)