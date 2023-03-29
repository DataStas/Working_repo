#TODO: Create a letter using starting_letter.docx 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
names = []
with open("D:\Pyhton_Dir\Projects\Working_repo\RememberOOPBasics\mailMergeProject\Input\\Names\invited_names.txt", mode='r') as names_file:
    names = names_file.readlines()

print(names)

with open("D:\Pyhton_Dir\Projects\Working_repo\RememberOOPBasics\mailMergeProject\Input\Letters\starting_letter.docx", mode='r') as letter_file:
    letter_content = letter_file.read()
    for name in names:
        letter_content = letter_content.replace(PLACEHOLDER, name.strip())
        print(letter_content)
        with open(f'D:\Pyhton_Dir\Projects\Working_repo\RememberOOPBasics\mailMergeProject\Output\ReadyToSend\invite_for_{name.strip()}.docx', mode='w') as out_file:
            out_file.write(letter_content)