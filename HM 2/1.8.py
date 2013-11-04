Timothy S Brower
HM 1.8

print "1.8.1___________________________________________________________________"

for i in range (1,11):
    #n = float i
    print "1/", i,"= ",1.0/i
    i =+ 1

print "1.8.2________________________________5___________________________________"

num = input("Type a number please")
if num < 0:
    print "I see you entered a negitive numper I have made it positive"
    num = num * -1
    
while num >0:
    print num
    num = num - 1

print 0

print "1.8.3___________________________________________________________________"

base = input("please type base value")
exp = input("please type exponent value")
pr = base

for i  in range (1,exp):
    pr = pr * base
    
print pr

print "1.8.4___________________________________________________________________"

num = input("please enter a number that is devisibal by 2")

while num % 2 != 0:
    print num, "is not divisibal by two please try again"
    num = input("please enter a number that is devisibal by 2")

print num, 'is divisibal by 2'
            
