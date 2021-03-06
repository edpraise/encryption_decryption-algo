import binascii

def createDict():
    Dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper = alphabet.upper()
    symbols = [" ",".",",","?","!",'"',";",":","(",")","-",'\n']
    for i in range(64):
        if i < 26:
            Dict[alphabet[i]] = bin(i)[2:].zfill(6)
        elif i >= 26 and i < 52:
            Dict[upper[i-len(alphabet)]] = bin(i)[2:].zfill(6)
        elif i >= 52:
            pos = i - 52
            Dict[symbols[pos]] = bin(i)[2:].zfill(6)
    return Dict


def createDict2():
    Dict = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper = alphabet.upper()
    symbols = [" ",".",",","?","!",'"',";",":","(",")","-",'/']
    for i in range(64):
        if i < 26:
            Dict[alphabet[i]] = bin(i)[2:].zfill(6)
        elif i >= 26 and i < 52:
            Dict[upper[i-len(alphabet)]] = bin(i)[2:].zfill(6)
        elif i >= 52:
            pos = i - 52
            Dict[symbols[pos]] = bin(i)[2:].zfill(6)
    return Dict

def readDoc(txtfile):
    file = open(txtfile,'r')
    outtext = ""
    lines = file.readlines()
    for line in lines:
        outtext = outtext + line
    #for line in file:
     #   newline = line.strip("\n")
      #  newline = newline.replace("\'","'")
       # outtext = outtext+newline+" "
    return outtext

def eMain(key,plaintext):
    binaryDict = createDict()
    newKey = keyLengthen(key,plaintext)
    binarylistKey = binaryConversion(newKey,binaryDict)
    binarylistPlaintext = binaryConversion(plaintext,binaryDict)
    binarylistCipher = xorfunc2(binarylistKey,binarylistPlaintext)
    return textConversion(binarylistCipher,binaryDict)

def eMain2(key,plaintext):
    binaryDict = createDict2()
    newKey = keyLengthen(key,plaintext)
    binarylistKey = binaryConversion(newKey,binaryDict)
    binarylistPlaintext = binaryConversion(plaintext,binaryDict)
    binarylistCipher = xorfunc2(binarylistKey,binarylistPlaintext)
    return textConversion(binarylistCipher,binaryDict)

def dMain(key,ciphertext):
    binaryDict = createDict()
    newKey = keyLengthen(key,ciphertext)
    binarylistKey = binaryConversion(newKey,binaryDict)
    binarylistCiphertext = binaryConversion(ciphertext,binaryDict)
    binarylistDecrypted = xorfunc2(binarylistKey, binarylistCiphertext)
    return textConversion(binarylistDecrypted,binaryDict)

def dMain2(key,ciphertext):
    binaryDict = createDict2()
    newKey = keyLengthen(key,ciphertext)
    binarylistKey = binaryConversion(newKey,binaryDict)
    binarylistCiphertext = binaryConversion(ciphertext,binaryDict)
    binarylistDecrypted = xorfunc2(binarylistKey, binarylistCiphertext)
    return textConversion(binarylistDecrypted,binaryDict)

def keyLengthen(key,plaintext):
    keyLen = len(key)
    messageLen = len(plaintext)
    repetition = messageLen // keyLen
    remainder = messageLen % keyLen
    newKey = key * repetition + key[0:remainder]
    return newKey

def binaryConversion(text,dict):
    outlist = []
    for char in text:
        if char in "1234567890'&":
            outlist.append(char)
        else:
            binarynum = dict[char]
            outlist.append(binarynum)
    return outlist

def textConversion(binarylist,dict):
    outString = ""
    newDict = {}
    for (k,v) in dict.items():
        newDict[v] = k
    for binNum in binarylist:
        if binNum in "1234567890'&":
            outString = outString + binNum
        else:
            char = newDict[binNum]
            outString = outString + char
    return outString

def xorfunc2(binaryKey, binaryTxt):
    '''This is the xor function, should be applicable for both encrypt and decrypt'''
    binLen=len(binaryKey)
    acc=[]
    for i in range(binLen):
        if binaryTxt[i] in "1234567890'&":
            acc.append(binaryTxt[i])
        else:
            y = int(binaryKey[i],2) ^ int(binaryTxt[i],2)
            binTemp=(bin(int(y))[2:].zfill(6))
            acc.append(binTemp)
    return acc