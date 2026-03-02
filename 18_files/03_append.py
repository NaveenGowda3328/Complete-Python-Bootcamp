# Append to an existing file called John Doe.txt
# It should add data about John Doe's Hometown

f = open("John Doe.txt", "a")

string = ''' 
John Doe intially live in Pheonix, Arizona. He is a very nice guy 
'''
f.write(string)

f.close()