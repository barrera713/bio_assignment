# For this problem you will write a very simple sequence 
# identity calculator. The user will input 2 DNA/RNA sequences 
# which must be of the same length. Once both sequences have been 
# input then the program will compute the fraction of nucleotides in 
# both sequences that are shared.

# Test 1
# GCGTTAGCTAAAGCC
# CCGTAAGCTATACCG        

# Test 2
# AGCCGCGCTA
# UGcCTCGCug

# Test 3
# TATAT
# UAUAT


# Validate the length of sequences
# A G C T U
# --------- validate the sequence  --------- 
# @param {String}
# @return {Boolean}
def validateSeq(s):
    for i in range(len(s)):
        if(s[i] != 'A' and s[i] != 'G' and s[i] != 'C' and s[i] != 'T' and s[i] != 'U'):
            return False 
    return True # Returning True will indicate that there were no validation errors


# ---------- Main Program ------------
finish = 's'
while(finish != 'e'):
    # strip() to remove spaces
    s1 = str.upper(input("Input the nucleotide sequence 1. ").strip())
    s2 = str.upper(input("Input the nucleotide sequence 2. ").strip())


    # Validate the lengths of both sequences
    if(len(s1) != len(s2)): 
        print("ERROR: Sequence lengths do not match.")
        break

    # We call our validation function on both sequences
    # We break and print error message if there are invalid nucleotides in a sequence
    elif(validateSeq(s1) != True or validateSeq(s2) != True):
        print("ERROR: Sequence contains invalid nucleotides.")
        break
    else:
        # If there our zero errors we continue and calculate the identity
        shared = 0
        for i in range(len(s1)): 
            # If nucleotides match in the same position of their sequence
            # Increment shared 
            if(s1[i] == s2[i]):
                shared += 1

            # In addition, we also want to increment if U and T
            # share their position in their sequence
            elif (s1[i] == "T" and s2[i] == "U" or s1[i] == "U" and s2[i] == "T"):
                shared += 1

        # We divide the total amount of shared nucleotides
        # by the length of any sequence 
    print("The sequence identity is", shared / len(s1))
    break
finish = input("Would you like to enter another sequence? Enter any key to continue or 'e' to quit. ")
print("Program terminated.")





