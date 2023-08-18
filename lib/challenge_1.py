# Challenge 1: Converting 12-hour time to 24-hour time


# def to_24h(hour, minute, period):
#     if period == "am":
#         return str(hour) + "0" + str(minute) + "0" + str(period)
#     elif period == "pm":
#         return str(hour) + "0" + str(minute) + "0" + str(period)
#     else:
#         return str(hour) + " " + str(minute) + " " + str(period)

# print(to_24h("8:", "", "am")) 
# print(to_24h("11:", "", "pm")) 


def to_24hr(str1):
     
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]  
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]
       
print(to_24hr("10:56:34 PM"))
