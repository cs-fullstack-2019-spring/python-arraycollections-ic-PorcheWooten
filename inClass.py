def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()
    problem5()


# Create a function that returns an array from 0 to 100. Print the array in another function.
def problem1():
    list = []
    for x in range (0,100):
        list.append(x)
    print (list)
    
def problem2():
    userInput = ""
    while(userInput != "q"):
        userInput = input("Enter something ")



# Create a function with the variable below. After you create the variable do the instructions below that.
# 
# 
# a) Print Pete’s name from the list
# 
# b) Change Pete’s name to ‘Ringo’, print the list
# 
# c) Add the name ‘Yoko’ to the list and print


def problem3():
    listNames = ["John","Paul","George","Pete"]
    print(listNames[3])
    listNames[3]="Ringo"
    print(listNames)
    listNames.append("Yoko")
    print(listNames)


# Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
# 
# Vocals/Robert
# Guitar/Jimmy
# Bass/John
# Drums/Bonzo
# a) Print the collection
# 
# b) Print who plays guitar

def problem4():
    list = {"Vocals": "Robert", "Guitar": "Jimmy", "Bass": "John", "Drums": "Bonzo"}
    print(list)
    print(list["Guitar"])


# Create a function that will have a hard coded array of Kenn, Kevin, and Erin several times in the array. Print out how many times Kenn, Kevin, or Erin appears in an array.    
def problem5():
    names = ["Kenn","Kevin", "Erin","Kenn","Erin","Kenn","Kevin"]
    print(names.count("Kenn"))
    print(names.count("Kevin"))
    print(names.count("Erin"))
    
    

        
if __name__ == '__main__':
    main()