#Assignment 06

print("This is Program06 - Armando Castro")

print("This program uses lists, strings, tuples, and dictionaries.")

# Two Tuples

weeks = ('Week One', 'Week Two')
days = ('Thursday', 'Friday', 'Saturday')

# Sales reps names and locations
sales_rep_names = ['Frank Fleming', 'Domingo Depue', 'Ema Endicott']
sales_rep_locations = ['Austin', 'Dallas', 'Houston']



# get names and locations
# create 3 lists
boats_sold_thursday = []
boats_sold_friday = []
boats_sold_saturday = []

boats_sold_thursday2 = []
boats_sold_friday2 = []
boats_sold_saturday2 = []



# Populate boats sold list
# Enter Sales Results

print('\n-----Entering boats sold for :', weeks[0], '-----')

for items in sales_rep_names:
        boats_sold_thursday.append(int(input(
                '\nThursday boats sold by ' + items + ':')))
        boats_sold_friday.append(int(input(
                '\nFriday boats sold by :' + items + ':')))
        boats_sold_saturday.append(int(input(
                '\nSaturday boats sold by :' + items + ':')))

print('\n-----Entering boats sold for :', weeks[1], '-----')

for items in sales_rep_names:
        boats_sold_thursday2.append(int(input(
                '\nThursday boats sold by ' + items + ':')))
        boats_sold_friday2.append(int(input(
                '\nFriday boats sold by :' + items + ':')))
        boats_sold_saturday2.append(int(input(
                '\nSaturday boats sold by :' + items + ':')))

# Print Sales Results

print("\n-----", weeks[0], "Results -----")     

for y in range(3):
        print(sales_rep_names[y], "sold ", boats_sold_thursday[y], "on Thursday")
        print(sales_rep_names[y], "sold ", boats_sold_friday[y], "on Friday")
        print(sales_rep_names[y], "sold ", boats_sold_saturday[y], "on Saturday")

print("\n")
print("-----", weeks[1], "Results -----")  

for z in range(3):
        print(sales_rep_names[y], "sold ", boats_sold_thursday2[z], "on Thursday")
        print(sales_rep_names[y], "sold ", boats_sold_friday2[z], "on Friday")
        print(sales_rep_names[y], "sold ", boats_sold_saturday2[z], "on Saturday")




# Create a dictionary to store the website URL's for each boat dealer
dealer_URLs = []
name1 = 'frank_flemming'
name2 = 'domingo_depue'
name3 = 'ema_endicott'

#populate the dictionary

print("\n")

urlOne = input("Enter the URL for " + sales_rep_locations[0] + ": ")
urlTwo = input("Enter the URL for " + sales_rep_locations[1] + ": ")
urlThree = input("Enter the URL for " + sales_rep_locations[2] + ": ")


#Print sales reps email addresses

print("\n------ Contact sales reps are their email addresses ------\n")
print(name1 + "@" + urlOne)
print(name2 + "@" + urlTwo)
print(name3 + "@" + urlThree)

print("\nI had some issues here pairing the key pairs to the dictionary. ")
print("The dictionary was seen as a tuple, which has immutable items. ")
print("I had to convert the dictionary to a list to get it to work. ")
print("I am still unsure how to use both the dictionary and get the correct output.")
print("Could you please tell me how in your feedback? ")


	
