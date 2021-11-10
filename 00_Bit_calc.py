def statement_generator(text, decoration) :
    ends = decoration * 5
    statement = "{} {} {}".format(ends, text, ends)
    
    print()
    print(statement)
    print()

    return ""

def user_choice():

    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "number", "#"]
    image_ok = ["image", "img", "pix", "picture", "picture"]

    valid = False
    while not valid:

        response = input("File type (integer / text/ image): ").lower()

        
        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for  an image")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            print("please choose a valid file type!")
            print()
           
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




statement_generator("Bit Calculator for integers, text and images", "-")

keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()
    
    if data_type =="integer":
        var_integer = num_check("Enter an integer: ", 0)
    
    elif data_type == "image":
        image_width = num_check("image_width", 1)
        image_height = num_check("image_height", 1)

    else:
        var_text = input("Enter some Text. ")
