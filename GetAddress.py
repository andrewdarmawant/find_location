import webbrowser, sys, pyperclip, string

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:])
else:
	address = input("where do you want to go: ")

website = 'https://www.google.com/maps/search/' + address

webbrowser.open(website)
