#%%
'''
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.

'''
#%%
DNA= input( " Enter your DNA string: " )
DNA = list(DNA)[::-1]

for i in range(len(DNA)) :
    if DNA[i] == "A" :
        DNA[i] = "T" 
    elif DNA[i] == "T" :
        DNA[i] = "A" 
    elif DNA[i] == "C" :
        DNA[i] = "G"
    elif DNA[i] == "G" :
        DNA[i] = "C"

DNA_reversed_STR = ""
for i in DNA :
    DNA_reversed_STR += i   



        
    
        
        