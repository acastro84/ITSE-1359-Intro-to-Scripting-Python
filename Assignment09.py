#Pokemon class definition
class Pokemon:
    # __init__ called AUTOMATICALLY when an object is created.
    def __init__(self, name, ability):
        # Assign argument 'name' to instance variable 'self.__name'
        self.name = name
        #Assign argument 'ability' to instance variable 'self.__ability'
        self.ability  = ability

    # Get INSTANCE variable self.__name
    def get_name(self):
        return name

    # Get INSTANCE variable self.__ability
    def get_ability(self):
        return ability

    


# main() function
def main():
    print('\n################   In main() ###############')
    pokemon_list = []
    #counter used in loop
    pokemon_number = 1


    print("This program keeps track of Pokemon characters, saves the data to a file, and displays the data from a file.")
    more_pokemon  = input("\nDo you have a pokemon to enter? (Y/N) ").lower()

    # open a new file to write.  Use append in case the file does not exist.
    outF = open("YourPokemon.txt", "a")

    while more_pokemon == 'y':
        #Get the name of the pokemon  from user
        pokemon_name = input ('\nEnter name for Pokemon #{}: '
                              .format(pokemon_number))

        #Get the ability of the pokemon from user
        pokemon_ability = input('\nEnter ability for Pokemon #{}: '
                                .format(pokemon_number))

        #Create a new pokemon object with pokemon_name and pokemon_ability
        new_pokemon = Pokemon(pokemon_name, pokemon_ability)

        #Add new_pokemon to list.
        pokemon_list.append(new_pokemon)

        #increment counter
        pokemon_number += 1
        more_pokemon = input("\nAnother pokemon to enter? (y/n) ").lower()

    print("\n")
    #display_pokemon(pokemon_list)
    saveData(pokemon_list, outF)
    outF.close()

    #create inFile
    readFile = open("YourPokemon.txt", "r")

    display_data(readFile)
    readFile.close()
    
    print("I took a while to look into printing statements with objects before starting this assignment. ")
    print("This one worked well after switching to append. I also forgot to close at end when I first wrote.") 


def display_data(reader):
    
    #print Line by line
    for x in reader:
        print(x)
    


def saveData(olist, fName):
    count2 = 1
    for obj in olist:
        fName.writelines("Name of Pokemon #" + str(count2) + ":" + str(obj.name)+
        "\nAbility of Pokemon #" + str(count2) + ":" + str(obj.ability))
        fName.writelines("\n")
        count2 += 1
        



#Determine if program is run as main() or a module.
if __name__ == '__main__':
    main()

else:
    pass
    # Do nothong.  This module has been inmported by anotehr
    # module that wants to make use of the functions,
    # classes and other items that it has defined.

    

    
