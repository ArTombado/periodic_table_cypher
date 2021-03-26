from elements import ELEMENTS

text = input("Write a text: ").lower()

new_text = ""

while( text != "" ):
	if( text[0] == " " ):
		# "/" will space the words
		new_text += "/ "
		text = text[1:]
	elif( ELEMENTS.get(text[0]) ):
		# get an equivalent element for each letter
		new_text += f"{ELEMENTS[text[0]]} "
		text = text[1:]
	elif( ELEMENTS.get(text[0:2]) ):
		# if don't exist the equivalent for a letter, get an equivalent element for the next two letters
                new_text += f"{ELEMENTS[text[0:2]]} "
                text = text[2:]
	else:
		# if there is no element equivalent and is not space, then write the letter with parentheses
		new_text += f"({text[0]}) "
		text = text[1:]

print(new_text)
