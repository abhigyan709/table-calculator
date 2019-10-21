# Program to print the table:
keep_running = 'y'
while keep_running == 'y':
    n = int(input("Please enter the number you want to print the Table: "))
    for i in range(1, 11):
        print("{} x {} =  {}".format((n),(i),(n * i)))
    keep_running = str(input("Do you want to print more table: "))
    if keep_running == 'n':
        print("Program finished with exit code 0")




