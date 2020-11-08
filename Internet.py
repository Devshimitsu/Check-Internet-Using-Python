import wikipedia
import pyfiglet

main=pyfiglet.figlet_format("Devshimitsu")
print(main)


try:
	result=wikipedia.summary("India")
	print("Connected")
except:
	print("NO Internet!!!")
