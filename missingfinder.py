letters = "ABDEFGHIKLNOPQRSTUVWX"
pieces = ["ARE", "BQN", "DFI", "GLU", "KPV", "OTW", "SHX"]

allcoms =[]

missingcoms = []

foundcoms = []

missinginverses = []

for letter1 in letters:
    for letter2 in letters:
        if letter1 != letter2:
            for piece in pieces:
                if (not (letter1 in piece and letter2 in piece)) and (letter1 in piece or letter2 in piece) and ((letter1 + letter2) not in allcoms):
                    allcoms.append(letter1 + letter2)


with open("corners.txt", "r") as f:
    algs = f.readlines()
    for alg in algs:
        for com in allcoms:
            if alg.startswith(com) or alg.startswith("#" + com):
                (foundcoms.append(com))


for com in allcoms:
    if com not in foundcoms and com not in missingcoms:
        missingcoms.append(com)


print("there are " + str(len(missingcoms)) + " missing comms:" + str(missingcoms)) 
#print missing comms

for com in missingcoms:
    if not ("N" in com or "U" in com or "V" in com or "W" in com or "X" in com):
        print(com)


for i in missingcoms:
    if (i[1] + i[0]) not in missingcoms:
        missinginverses.append(i[0] + i[1])


print(str(len(set(missinginverses))) + " missing inverses: " + str(missinginverses))
#print missing inverses
