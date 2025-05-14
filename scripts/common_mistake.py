def apply_discount(code=None):  
    if code is not None:  # Fix!  
        print(f"Applying discount: {code}")  
    else:  
        print("No discount applied.")  

apply_discount("")  
# Oops! Empty string is falsy, but not None!

