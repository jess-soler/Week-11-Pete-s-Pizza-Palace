"""
    name: utils.py
    author: Jessica Soler
    created: 3/28/24
    purpose: a utility module with commonly used functions
"""

#-------------------------------TITLE-------------------------------#
def title(statement):
    """ takes in string argument, return string with ascii decorations """
    
    #get the length of the statement
    text_length = len(statement)
    
    #initialize the result string variable
    title_string = ""
    title_string = title_string + " +--" + "-" * text_length + "--+\n"
    title_string = title_string + " |  " + statement + "  |\n"
    title_string = title_string + "+--" + "-" * text_length + "--+"
    
    #return the contatenated title string
    return title_string

#-------------------------------GET INT-------------------------------#
def get_int(prompt):
    """ 
        get an integer from the user with try catch
        the prompt string parameter is used to ask the user
        for the type of input needed
    """
    
    #ask the user for an input based on the prompt: string parameter
    num = input(prompt)
    
    #if the input is numeric, convert to int and return value
    try:
        return int(num)
    
    #if the input is not numeric,
    #inform the user and ask for input agian
    except ValueError:
        print(f"You entered: {num}, which is not a whole number.")
        print(f"Let's try that again.\n")
        
        #call function again, this is a recursive function call
        return get_int(prompt)
    
#-------------------------------GET FLOAT-------------------------------#
def get_float(prompt):
    """
        get a number from the user with try catch
        the prompt string parameter is used to ask the user
        for the type of input needed
     """
        
    #ask the user for an input based on the what parameter
    num = input(prompt)
    
    #if the input is numeric, convert to float and return value
    try:
        return float(num)
    
    #if the input is not numeric
    #inform the user and ask for input again
    except ValueError:
        print(f"You entered: {num}, which is not a number.")
        print(f"Let's try that again.\n")
    
        #call function again, this is a recursive function call
        return get_float(prompt)
    
#-------------------------------MAIN-------------------------------#
def main():
    """ place code here to test the module """
    print(title("Test the utils module"))
    int_num = get_int("Please enter a whole number: ")
    print(f"Your whole number is: {int_num}")
    float_num = get_float("Please enter any number: ")
    print(f"Your number is: {float_num}")
    
#if standalone program, call the main function
#else use as a module
if __name__ == "__main__":
    main()
        