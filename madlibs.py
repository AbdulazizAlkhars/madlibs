from unicodedata import name


def main():
	# write your code here

	time =input("Enter a number from 1 to 12:") 
	items = input("Enter a noun (plural):")
	name = input("Enter a name:")
	scream = input("Enter any sentence:")
	scream1 = scream.upper()
	action =input("Enter a verb:")

	print("The story goes...")
	print("It was ",time,"o'clock when I heard a knock at the door.")
	print("I opened the door and there was a box full of ",items, " with a note saying From Mr." ,name)
	print("Just as I closed the door I heard a scream ",scream1)
	print("I froze in place and all I python3could do was ",action) 



if __name__ == '__main__':
	main()
	