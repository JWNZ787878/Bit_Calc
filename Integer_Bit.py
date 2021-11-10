def num_check(question, low):


    valid = False 
    while not valid:

        error = "Please enter an integer that is more than 0"
        "(or equal to) {}".format(low)

        try:

            response = int(input(question))

            if response >= low:
                num = response
                return response 

            else:
                print(error)
                print()

        except ValueError:
           print(error)
def int_bits():
    var_integer = num_check("Please enter an integer: ", 0)
    var_binary =  "{0:b}".format(var_integer)
    num_bits = len(var_integer)
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))

    return ""

int_bits