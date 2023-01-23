#Country Made by Alon Rehin for CIS 261

def countries():

    List = {
       "USA" : "United States",
       "RUS" : "Russia",
       "ISR" : "Israel",
       "BRA" : "Brazil",
       "GER" : "Germany",
        }

    return List




def intro():

    print("COUNTRIES \n\n\n")
    print("COMMANDS: \n")
    print("list - List all countries")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit the program")


def display(List):
        Number = 0

        for country in List:
            Number += 1
            print(str(Number) + ".",country)#, "-", (List[country]))
   
        View = input("\nWhich country you want to see? ").upper()
        print(List[View])
        return Number
  

def delete(List,Number):

    DelCode = input("\nWhich country code you want to delete? ").upper()

    if not DelCode in List:
        print("\nNot found in list")

    else:           
            del List[DelCode]
            print("\nDeleted")
    return List


        
def add(List):

    AddInput = input("\nWhich country you want to add? ")
    AddCode = input("\nWhat is the country code ").upper()
    if len(AddCode) != 3 and len(AddCode) != 2:
        print("\nAdd only country codes")

    elif AddInput and AddCode in List:
        print("\nAlready exists")

    else:
        List[AddCode] = AddInput
        print("\nAdded")
    return List


intro()

List=countries()

Command = input("\nWhat do you want to do? ")

while Command.lower() != "exit":


    if Command.lower() == "list":
        print("\nYour countries:\n")
        Number=display(List)
        Command = input("\nWhat do you want to do? ")

    elif Command.lower() == "del":
        delete(List,Number)
        Command = input("\nWhat do you want to do? ")

    elif Command.lower() == "add":
        add(List)
        Command = input("\nWhat do you want to do? ")

    else:
        print("Invalid input\n")
        intro()
        Command = input("\nWhat do you want to do? ")

print("\nGoodbye!\n")



