#trying to think of errors I might come across, I chose the file not found error to work with...
filename = 'fb_manager_registry.txt'

try: #try to open the file
    f = open(filename)
except FileNotFoundError: #If the file doesn't exist, the following will occur
    print('The file you are searching for does not exist.')
else: #If the file does exist, the following will occur
    print('The file exists and can be opened.')