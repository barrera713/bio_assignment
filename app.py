# Validate the length of sequences
# A G C T U

# Validates the sequence to 

finish = 's'
while(finish != 'e'):
    s = input("Input the nucleotide sequence 1. ")
    GCCount = 0.0
    Total = 0.0
    Error = False 
    for i in range(len(s)):
        Total += 1
        if(s[i].upper() != 'A' and s[i].upper() != 'G' and s[i].upper() != 'C' and s[i].upper() != 'T' and s[i].upper() != 'U'):
            print("Sequence contains invalid nucleotide")
            Error = True
            break
        elif s[i] == 'G' and s[i] == 'C':
            GCCount += 1
    if not Error:
        GCFrac = GCCount / Total
        print(GCFrac)
    finish = input("Would you like to enter another sequence? Input 'e' to quit. ")




