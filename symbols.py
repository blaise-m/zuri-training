'''
The Naira symbol is a hex value of 20A6, to be able to parse this, 
you need to understand ASCII and UTF8. what you can do is convert 
hex to int and then find the ascii value of it, from yesterday's class, 
we did functions, so we can write a simple function for this. 
I won't include exception handling because we haven't learnt it.
'''

def convert_hex_to_symbol(hex_string: str) -> chr:
    return chr(int(hex_string, 16))

# call it
naira_symbol = convert_hex_to_symbol("20A6")


'''
or use a lambda to do this
'''

symbol_processed = lambda value: chr(int(value, 16))

# call your lambda
naira_symbol = symbol_processed("20A6")



'''
then you can print naira_symbol or use it the way you want
the cool thing is, we can also process other symbols not just naira, as long as you know the hex values, now here is a link of hex values for the symbols you need:
currency symbols -> https://www.w3schools.com/charsets/ref_utf_currency.asp
letter like symbols -> https://www.w3schools.com/charsets/ref_utf_letterlike.asp
General punctuation -> https://www.w3schools.com/charsets/ref_utf_letterlike.asp
'''

'''
The function can throw an exception when you are trying to parse what the 
interpreter does not understand, and I purposely made it simple and did 
not code defensively, this if fine this example, but if you are going to 
use it for a production base application, then do this
'''

def convert(hex_value: str) -> chr:
    int_representation_of_hex = ""

    if hex_value is not None and isinstance(hex_value, str):
        try:
            int_representation_of_hex = int(hex_value, 16)
        except ValueError as _:
            return "invalid function argument passed, can't convert hex value to integer"
        
        return chr(int_representation_of_hex)
    
    return int_representation_of_hex


if __name__ == "__main__":

	print(naira_symbol)
