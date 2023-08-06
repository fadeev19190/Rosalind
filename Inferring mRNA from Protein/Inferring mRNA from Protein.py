# I added a bio_struct file in Rosalind repository
from bio_structs import amino_acid_codons

# Protein sequence given by Rosalind
protein = 'MA'
# The variable count is initialized to 1. This variable will keep track of the number of possible RNA sequences.
count = 1
# The code loops through each amino acid in the protein sequence. It retrieves the corresponding list of codons
for aa in protein:
    count *= len(amino_acid_codons.get(aa))
# The variable count is multiplied by 3, since there are three possible stop codons
count *= 3

# The variable reminder is assigned the value of count modulo 1,000,000, which corresponds to the number of possible RNA sequences that can encode the protein sequence
reminder = count % 1000000

print(reminder)
