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
    more_pokemon  = input("\nDo you have a pokemon to enter? (Y/N) ").lower()

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
    display_pokemon(pokemon_list)
    print("This one tested my OOP concepts.")
    print("I handled my memory resolution printing problem by using obj in my for loop instead of another variable." ) 


def display_pokemon(plist):
    count = 1
    for obj in plist: 
        print("Name of Pokemon #" + str(count) + ":", obj.name,
        "\nAbility of Pokemon #" + str(count) + ":", obj.ability, sep =' ' )
        print("\n")
        count +=1
        
    
    



#Determine if program is run as main() or a module.
if __name__ == '__main__':
    main()

else:
    pass
    # Do nothong.  This module has been inmported by anotehr
    # module that wants to make use of the functions,
    # classes and other items that it has defined.

    

    
