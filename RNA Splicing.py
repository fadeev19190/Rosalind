from Bio import SeqIO
from bio_structs import *

# Specify the path to your FASTA file
fasta_file = "rosalind_splc-2.txt"

# Open the file and read the sequences
sequences = SeqIO.parse(fasta_file, "fasta")

sequences_list = []
# Iterate over each sequence in the file
for seq_record in sequences:
    # Access sequence information
    sequence = seq_record.seq
    sequences_list.append(sequence)

string = sequences_list[0]
exon = string
introns = []

for i in range(1, len(sequences_list)):
    introns.append(sequences_list[i])

for i in introns:
    exon = exon.replace(i, '')

print('Length of intron: ', len(string))
print('Exon:', exon)
print('Length of exon: ', len(exon))

peptide = ''
for i in range(0, len(exon), 3):
    codon = exon[i:i+3]
    if len(codon) == 3:
        aa = DNA_Codons[codon]
        peptide += aa

print('Protein string: ', peptide)