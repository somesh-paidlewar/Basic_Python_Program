# simple encoder to encrpyt messages
# this program takes a string input message from the user 
# and copies the encoded message to the clipboard of the user

def main():
	import pyperclip
	print("Enter your message to encode ")
	message = input("Your message :- ")
	code = []
	for ch in message:
		code.append(str(ord(ch)))
	pyperclip.copy(" ".join(code))
	print("Your message Succesfully encoded and copied to ")
	print("your clipboard!!")

main()