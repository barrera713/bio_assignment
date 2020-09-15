# For this problem you will write a very simple sequence 
# identity calculator. The user will input 2 DNA/RNA sequences 
# which must be of the same length. Once both sequences have been 
# input then the program will compute the fraction of nucleotides in 
# both sequences that are shared.



# Validate the length of sequences
# A G C T U
# --------- validate the sequence  --------- 
def validateSeq(s):
    for i in range(len(s)):
        if(s[i].upper() != 'A' and s[i].upper() != 'G' and s[i].upper() != 'C' and s[i].upper() != 'T' and s[i].upper() != 'U'):
            return False 
    return True # Returning True will indicate that there were no validation errors

# Test 1
# GCGTTAGCTAAAGCC
# CCGTAAGCTATACCG        

# Test 2
# AGCCGCGCTA
# UGcCTCGCug

# Test 3
# TATAT
# UAUAT

# ---------- Main Program ------------
finish = 's'
while(finish != 'e'):
    # strip() to remove spaces
    s1 = input("Input the nucleotide sequence 1. ").strip()
    s2 = input("Input the nucleotide sequence 2. ").strip()

    # Validate the lengths of both sequences
    if(len(s1) != len(s2)): 
        print("ERROR: Sequence lengths do not match.")
        break

    # We call our validation function on both sequences
    # We break and print error message if there are invalid nucleotides in a sequence
    # if(validateSeq(s1) != True):
    #     print("ERROR: Sequence 1 contains invalid nucleotides.")
    #     break

    elif(validateSeq(s1) != True or validateSeq(s2) != True):
        print("ERROR: Sequence contains invalid nucleotides.")
        break
    else:
        # If there our zero errors we continue and calculate the identity
        shared = 0
        for i in range(len(s1)): 
            # If nucleotides match in the same position of their sequence
            # Increment shared 
            if(s1[i].upper() == s2[i].upper()):
                shared += 1

            # In addition, we also want to increment if U and T
            # share their position in their sequence
            elif (s1[i].upper() == "T" and s2[i].upper() == "U" or s1[i].upper() == "U" and s2[i].upper() == "T"):
                shared += 1

        # We divide the total amount of shared nucleotides
        # by the length of any sequence 
    print("The sequence identity is", shared / len(s1))
    break
finish = input("Would you like to enter another sequence? Enter any key to continue or 'e' to quit. ")
print("Program terminated.")





