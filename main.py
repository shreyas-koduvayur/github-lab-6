#Shreyas Koduvayur
def encoded(digit):
    change=""
    for i in digit:
        added= (int(i)+3)%10
        change+= str(added)
    return change

def decoder(digits):
    variable = ""
    for i in digits:
        addition_password = (int(i) - 3) % 10
        variable += str(addition_password)
    return variable




def main():
    print("Menu")
    print("-------------")
    print("1.Encode")
    print("2.Decode")
    print("3.Quit")

    while True:
        choices= int(input("Please enter an option:"))
        if choices ==1:
            question = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
        elif choices ==2:
            print(f"The encoded password is {encoded(question)}, and the original password is {question}")
        elif choices ==3:
            break


if __name__ =="__main__":
    main()

