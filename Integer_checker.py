def num_check(question, low):

    valid = False 
    while not valid:

        error = "Please enter an integer that is more than "
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

keep_going = ""
while keep_going == "":

    var_integer =  num_check("Enter an integer: ", 0)

    image_width = num_check("Image width", 1)

    image_height = num_check("Image height ", 1)
    

