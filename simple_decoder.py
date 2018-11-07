# this is a simple decoder that decodes Unicode- encoded messages
def decoder():
	print("Enter the message to be decoded")
	message = input("Your messager :- ")
	final_message = ""
	for num in message.split():
		decoded_chr = chr(int(num))
		final_message = final_message + str(decoded_chr)
	print("Your decoded message is as follows:- \n")
	print(final_message)

decoder()
