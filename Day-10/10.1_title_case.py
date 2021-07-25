def title_case(fName,lName):
    if fName == "" or lName == "":
        return "Invalid Inputs"
    
    fName = fName.title()
    lName = lName.title()

    return f"{fName} {lName}"

print(title_case(input("Enter your first name :  "),input("Enter your last name: ")))