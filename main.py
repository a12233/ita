
import random

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

def generateOTP(length, cipherList):
    otp = []

    for i in range(length):
        otp.append(cipherList[random.randrange(0, 46)])

    return ('').join(otp)

def exploitotpreuse(enc1, enc2):

    return True

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

    # data = encrypt("ITA SOFTWARE", "9KS;UENFN068", mycipherdict) #returns list
    # print(decrpyt(data, "9KS;UENFN068", mycipherdict,mydecryptdict))

    testopt = generateOTP(301,mycipher)

    # print(testopt)

    testString= 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, \'and what is the use of a book,\' thought Alice \'without pictures or conversations?'
    testString2 = 'The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well. Either the well was very deep, or she fell very slowly, for she had and to wonder'


    encString1 = encrypt(testString.upper(), testopt, mycipherdict)
    encString2 = encrypt(testString2.upper(), testopt, mycipherdict)

    exploitotpreuse(encString1, encString2)


    # print(decrpyt(encString1, testopt, mycipherdict, mydecryptdict))
    # print(decrpyt(encString2, testopt, mycipherdict, mydecryptdict))


    # print(str(len(testString))+"\t"+str(len(testString2)))

    # with open('c1.txt', 'r+') as f:
    #     f1data = f.read()
    #
    # with open('c2.txt', 'r+') as f:
    #     f2data = f.read()


    # print(f1data[:100]+"\t"+str(len(f1data)))
    # print(f2data[:100]+"\t"+str(len(f2data)))

if __name__ == "__main__":
    main()