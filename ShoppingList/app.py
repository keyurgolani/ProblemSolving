import os

# List to hold the list items
items_list = []

# Function that clears the screen.
def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


# Function that will show the items.
def show_list():
	clear_screen()
	# Print out the list to show the user.
	print("\n\n\n============= Your List Items ==============\n")
	for idx, item in enumerate(items_list):
		print("{}. {}".format(str(idx + 1), item))
	print("\n" + "=" * 20 + "\n")

def show_help():
	clear_screen()
	# Instructions for using and seeing the list and quit the app.
	print("\n\n================= Instructions ======================\n")
	print("Let's add all the items to the TODO list.")
	print("Enter 'SHOW' at any time to see the list and continue adding the items.")
	print("Enter 'HELP' at any time to see instructions again.")
	print("Enter 'DONE' or 'QUIT' at any time to see the list and quit the app.")
	print("Enter 'REMOVE' to remove an item from the list.")
	print("\n======================================================\n")

def add_to_list(list_item):
	show_list()
	# Get the position user wants to add the item at.
	position = None
	if items_list:
		try:
			position = int(input("Where do you want to add {}?\n"
			"Press ENTER to add to end of the list.\n"
			"> ".format(list_item)))
		except NameError:
			print("Bad Place. Defaulting to the end of the list.")
		except SyntaxError:
			print("Bad Place. Defaulting to the end of the list.")
		except TypeError:
			print("Bad Place. Defaulting to the end of the list.")
	# Add the item to list
	if position:
		items_list.insert(position - 1, list_item)
	else:
		items_list.append(list_item)
	show_list()

def remove_from_list():
	show_list()
	remove_item = None
	try:
		remove_item = str(raw_input("What item from the list do you want to remove?\n"
		"> "))
		items_list.remove(remove_item)
	except ValueError:
		print("The item {} is not on the list.".format(remove_item))
	else:
		print("Item {} successfully removed.".format(remove_item))
		show_list()


def main():
	# Show the instructions
	show_help()

	# Loop for the items
	while True:
		# Get the items from user
		list_item = str(raw_input("> "))

		#Check if the user wants to perform any action or add the item to list.
		if list_item.upper() == "DONE" or list_item.upper() == "QUIT":
			# In case of exit, break the loop
			break
		elif list_item.upper() == "SHOW":
			# If the user wants to see the list in middle of adding items
			show_list()
		elif list_item.upper() == "HELP":
			# In case the user wants to see instructions for using the application
			show_help()
		elif list_item.upper() == "REMOVE":
			# In case the user wants to remove items from the list
			remove_from_list()
		else:
			# If user added an item instead of QUIT, add it to the list.
			add_to_list(list_item)

	# Show the List
	show_list()

main()
