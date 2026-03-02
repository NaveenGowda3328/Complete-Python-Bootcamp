try:
   a = 345/10 # we put here 0 and gets output division by zero.

except Exception as e:
   print(e)

# Gets executed when there is no error in the try block

else:
   print("Hey I am good")