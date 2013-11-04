#timothy s brower
#cipher
#11.4.13

phr = raw_input('Please input text to encript:   ')
shft = input('and shift value')
encrpt = []
encrpt_out=''

for c in phr:
    if c.isalpha() == True:
        if c.isupper() == True:
            ascii= ord(c) + shft
            if ascii >= 91:
                ascii = ascii - 26
            encrpt.append(ascii)
        if c.islower() == True:
            ascii= ord(c) + shft
            if ascii >= 123:
                ascii = ascii - 26
            encrpt.append(ascii)
    else:
        ascii= ord(c)
        encrpt.append(ascii)
        
for i in encrpt:
    encrpt_out += chr(i)
print 'the encripted text is:   ', encrpt_out
