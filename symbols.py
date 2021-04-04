'''
To print a symbol on the terminal e.g. a Naira symbol, you need 
it's hex value. The Naira symbol has a hex value of 20A6. To print 
it on the terminal, first convert the hex value to int and then 
apply the chr() method on the int to return the symbol

Hex Value references:
currency symbols -> https://www.w3schools.com/charsets/ref_utf_currency.asp
letter like symbols -> https://www.w3schools.com/charsets/ref_utf_letterlike.asp
General punctuation -> https://www.w3schools.com/charsets/ref_utf_letterlike.asp
'''

def convert_hex_to_symbol(hex_string: str) -> chr:
    '''
    Takes in a hex value and returns a symbol
    '''
    
    hex_int = int(hex_string, 16)
    return chr(hex_int)


# the lambda equivalent of the above function is:
processed_symbol = lambda value: chr(int(value, 16))


if __name__ == "__main__":

    naira_symbol1 = convert_hex_to_symbol("20A6")
    print(naira_symbol1)

    naira_symbol2 = processed_symbol("20A6")
    print(naira_symbol2)


