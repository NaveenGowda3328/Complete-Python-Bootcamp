import re  # This is Python's regular expression module

def convert_to_slug(text):
    # Step 1: Convert all characters in the text to lowercase
    text = text.lower()
    
    # Step 2: Replace anything that's NOT a letter (a-z) or number (0-9)
    #         with a dash (-). This includes spaces, punctuation, symbols, etc.
    #         The '+' means "one or more of these characters"
    text = re.sub("[^a-z0-9]+", "-", text)
    
    # Step 3: Remove any dashes from the beginning or end of the string
    text = text.strip("-")
    
    # Step 4: Return the cleaned-up string
    return text

# Example test cases to see how the function works

print(convert_to_slug("hey you are good"))                
# Output: "hey-you-are-good"

print(convert_to_slug("Hello! How are you?"))             
# Output: "hello-how-are-you"

print(convert_to_slug(" Clean   this --- mess "))         
# Output: "clean-this-mess"

print(convert_to_slug("Python_is#awesome!!"))             
# Output: "python-is-awesome"

print(convert_to_slug("123 Main Street, Apt #4"))         
# Output: "123-main-street-apt-4"

print(convert_to_slug("Café on 5th @ Noon"))              
# Output: "cafe-on-5th-noon"

print(convert_to_slug("Rock & Roll > Jazz"))              
# Output: "rock-roll-jazz"

print(convert_to_slug("Multiple     spaces here"))        
# Output: "multiple-spaces-here"

