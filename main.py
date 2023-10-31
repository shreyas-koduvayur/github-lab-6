#Shreyas Koduvayur
def encoded(digit):
    change=""
    for i in digit:
        added= (int(i)+3)%10
        change+= str(added)
    return change

