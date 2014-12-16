## Program to recover the sequence header of fasta files

exit = 0

## Get the name of the fasta file and test it

while exit == 0:
    user_inp = raw_input("Enter the name of the fasta file: ")
    if user_inp == "done":
        print "See you later!"
        break
    try:
        file = open(user_inp)
        exit = 1
    except:
        print "Sorry, can't find this file. \nTry another name or type \"done\" to finish the program ;)"
        continue

## Recover the header of the sequences and save it in the chosen output

if exit == 1:
    user_out = raw_input("Enter the name of the output file: ")    
    output = open(user_out,"w")
    for line in file:
        if line.startswith(">"):
            output.write(line)
    output.close()
