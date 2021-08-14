with open("Input/Names/invited_names.txt" , "r") as names:
    list_of_names = names.readlines()

    for name in list_of_names:

        with open("Input/Letters/starting_letter.txt", "r") as starting_file:
            contents = starting_file.read()

        name = name.strip("\n")
        contents = contents.replace("[name]", name)

        with open(f"Output/ReadyToSend/{name}.txt", "w") as ready_to_send:
            ready_to_send.write(contents)