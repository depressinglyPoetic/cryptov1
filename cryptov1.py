def customEncrypt(input, key):
    if (len(input))!=(len(key)):
        if (len(input))>(len(key)):
            key = key * 999
    output = []
    output2 = []
    for char in input:
        number = ord(char) - 96
        output.append(number)
    for char in key:
        number = ord(char) - 96
        output2.append(number)
    x = 0
    finalOutput = []
    while (x!=len(output)):
        ans = output[x] + output2[x]
        finalOutput.append(ans)
        x += 1
    finalString = ''
    for x in finalOutput:
        while x>26:
            x -= 26
        finalString += chr((x-1) + ord('a'))
    return finalString
def customDecrypt(input, key):
    if (len(input))!=(len(key)):
        if (len(input))>(len(key)):
            key = key * 999
    output = []
    output2 = []
    for char in input:
        number = ord(char) - 96
        output.append(number)
    for char in key:
        number = ord(char) - 96
        output2.append(number)
    x = 0
    finalOutput = []
    while (x!=len(output)):
        ans = output[x] - output2[x]
        finalOutput.append(ans)
        x += 1
    finalString = ''
    for x in finalOutput:
        while x<1:
            x += 26
        finalString += chr((x-1) + ord('a'))
    return finalString
def compare(preDecrypt, postDecrypt):
    output = []
    output2 = []
    for char in preDecrypt:
        number = ord(char) - 96
        output.append(number)
    for char in postDecrypt:
        number = ord(char) - 96
        output2.append(number)
    x = 0
    finalOutput = []
    while (x!=len(output)):
        if (output2[x] > output[x]):
            output[x] += 26;
        ans = output[x] - output2[x]
        finalOutput.append(ans)
        x += 1
    finalString = ''
    for x in finalOutput:
        while x<1:
            x += 26
        finalString += chr((x-1) + ord('a'))
    return finalString
print("Welcome to FreeCom1!");
print ''
input = raw_input("Input text to be encrypted: ");
while input =="":
    print ''
    print 'You must input text!'
    input = raw_input('Write Text: ')
key = raw_input("Input text to be used as custom encryption key: ")
while key =="":
    print ''
    print 'You must input a key!'
    key = raw_input('Input text to be used as custom encryption key: ')
print ''
print 'Encrypted text is: ' + customEncrypt(key, input)
encryptStage1 = customEncrypt(input, key)
print ''
print 'Encrypted key now communicated to second party'
print ''
print '----------COMPUTER 2----------'
print ''
print 'Encrypted key recieved'
a = raw_input('Please enter custom key for encryption purposes: ')
while a =="":
    print ''
    print 'You must input a key!'
    a = raw_input('Input text to be used as custom encryption key: ')
print ''
print 'Newly encrypted key is: ' + customEncrypt(encryptStage1, a)
encryptStage2 = customEncrypt(encryptStage1, a)
print ''
print 'Encrypted text now returned to initial party'
print ''
print '----------COMPUTER 1----------'
print ''
print 'Encrypted key recieved'
print ''
print 'Decryption attempted, new text is: ' + customDecrypt(encryptStage2, key)
decryptStage1 = customDecrypt(encryptStage2, key)
print ''
print 'Semi-decrypted text now recommunicated to second party'
print ''
print '----------COMPUTER 2----------'
print ''
print 'Semi-decrypted text now recieved, running comparison to obtain initial party encryption code'
print ''
print 'Initial Party Encryption Key: ' + compare(encryptStage2, decryptStage1)
initialEncryptionKey = compare(encryptStage2, decryptStage1)
print ''
print 'Final decrypted text: ' + customDecrypt(encryptStage1, initialEncryptionKey)
