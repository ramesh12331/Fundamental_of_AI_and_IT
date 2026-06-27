days_of_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

print(days_of_week)
print(days_of_week[2])

months_of_year = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
print(months_of_year[5])

#TypeError: 'tuple' object does not support item assignment
# print(months_of_year[1]["FEBRUARY"])

#Valid (using a list instead)
months = ['January', 'February', 'March']

months[1] = 'FEBRUARY'

print(months)
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    
    
