def computepay(hours,rate):
    if hours <= 40:
        pay = hours*rate
    else:
        pay =(40*rate)+((hours-40)*(1.5 * rate))
    return pay
        
hours = float(input("Enter total number of hours: "))
rate = float(input("Enter rate per hour: "))
total = computepay(hours,rate)
print("Pay",total)
