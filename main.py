
def encrypt(plaintext, onetimepad, mycipherdict):
    plain = list(plaintext)
    otp = list(onetimepad)

    plainList = []
    cipherList = []
    outputList = []

    for i in plain:
        plainList.append(mycipherdict.get(i))

    for i in otp:
        cipherList.append(mycipherdict.get(i))

    for i in range(len(plainList)):
        outputList.append((plainList[i]+cipherList[i])%46)

    return outputList


def decrpyt(cipher, onetimepad, mycipherdict, mydecryptdict):
    outList = []
    cipherList = []
    outstr = ''
    iter = 0
    for i in onetimepad:
        cipherList.append(mycipherdict.get(i))

    for i in cipher:
        if i-cipherList[iter] >= 0:
            outList.append((i - cipherList[iter]))
        else:
            temp = cipherList[iter]
            outList.append(46+i-temp)   #TODO
        iter+=1

    for i in outList:
        outstr+=mydecryptdict[i]

    return outstr

def main():
    cipher = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?,-:;\'()'
    mycipher = list(cipher)
    mycipher.insert(0, ' ')
    f1data = ''
    f2data = ''
    # print(mycipher[38])

    mycipherdict = {}
    mydecryptdict = {}

    iter = 0
    for i in mycipher:
        mycipherdict[i]=iter
        mydecryptdict[iter]=i
        iter+=1

    # print(mycipherdict.get(' '))

    data = encrypt("ITA SOFTWARE", "9KS;UENFN068", mycipherdict) #returns list
    print(decrpyt(data, "9KS;UENFN068", mycipherdict,mydecryptdict))

    with open('c1.txt', 'r+') as f:
        f1data = f.read()

    with open('c2.txt', 'r+') as f:
        f2data = f.read()

    print(f1data[:100])
    print(f2data[:100])

if __name__ == "__main__":
    main()