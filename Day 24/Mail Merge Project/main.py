#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = '[name]'
names = []
with open('Input/Names/invited_names.txt') as file:
    txt = file.readlines()
    for name in txt[:-1]:
        names.append(name[:-1])
    names.append(txt[-1])

with open('Input/Letters/starting_letter.txt') as file:
    message = file.readlines()
    template = message[0]
    print(template)
    for name in names:
        with open(f'Output/ReadyToSend/{name} Invite.txt', 'w') as output:
            output.write(template.replace(PLACEHOLDER, f'{name}'))
        with open(f'Output/ReadyToSend/{name} Invite.txt', 'a') as outbound:
            outbound.write(''.join(message[1:]))
