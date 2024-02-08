# import datetime 

# print(datetime.datetime.now())


import datetime 

hoy = datetime.datetime.now()

print(hoy.day)
print(hoy.month)
print(hoy.microsecond)

s = datetime.datetime.strptime("2012/01/17", "%Y/%m/%d")

print(s + datetime.timedelta(days=100))
                        
