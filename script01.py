def steamy(x):
    sword = "-]"
    for i in range(x):
        sword += "="
    sword += ">"
    return print(sword)
length = int(input("How many pieces in your sword? "))
steamy(length)