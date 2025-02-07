#lets create a journal

with open("journal.text.", "a") as journal: #opening the file for writing
    while True: # infinite loop until q is pressed
        text = input("Enter a journal entry:(press q to quit): ")
        if text == "q":
            break
        journal.write(text.capitalize()+"\n") # need to add a new line