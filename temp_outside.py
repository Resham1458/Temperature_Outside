temperature= int(input("Enter the outside temperature"))
if temperature > 60 and temperature < 90:
    print("It is warm outside")
elif temperature >= 90:
    print("It is hot outside")
elif temperature < 60:
    print("It is chilly outside")