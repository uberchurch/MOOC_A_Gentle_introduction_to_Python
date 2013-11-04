#timothy s brower
#zeller algorithm

a = (input('What month were you born in. In numarick format please  ')) -2
b = input('What day of the month were you born?  ')
yr_str = raw_input('What year were you born in?  ')
c = int( yr_str[2:])   # get decade from year
d = int( yr_str[:2])  #get century
day = 'Sunday',  'Monday' , 'Teusday', 'Wednesday' , 'Thursady' , 'Friday', 'Saturday'

# if month is Jan or Feb goes on previous year
if a <= 0 :
    c = c - 1
    
if a == 0:   #set febuary 
     a = 12

if a== -1:  #set January
    a = 11
    
w = (13*a - 1) / 5
x = c / 4
y = d / 4
z = w + x + y + b + c - 2*d
r = z % 7

print 'You were born on a', day[r]



          
