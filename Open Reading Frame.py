# Importing required libraries
from bio_structs import *
from Bio import SeqIO

# Set input file name
input_file = 'rosalind_orf.txt'

# Read sequences from fasta file
with open(input_file) as f:
    fasta_sequences = list(SeqIO.parse(f, 'fasta'))

DNA_string_list = []

# Extract DNA sequences from fasta records and append them to a list
for fasta in fasta_sequences:
    DNA_string_list.append(str(fasta.seq))

# Concatenate DNA sequences from the list into a single string
DNA_string = ''
for nuc in DNA_string_list:
    DNA_string += nuc


# Check the sequence to make sure it is a DNA String:
def validate_seq(dna_seq):
    tmp_seq = dna_seq.upper()
    for nuc in tmp_seq:
        if nuc not in NUCLEOTIDE_BASE.get('DNA'):
            return False
    return tmp_seq


# Validate DNA string and assign it to a new variable:
DNA_string_verified = validate_seq(DNA_string)


def reverse_complement(seq):
    return ''.join([DNA_reverse_complement[nuc] for nuc in seq])[::-1]
# Swapping adenine with thymine and guanine with cytosine. Reversing newly generated string


# Generate the reverse complement of the validated DNA string
DNA_string_verified_second_strand = reverse_complement(DNA_string_verified)
possible_seq_of_proteins = []


# Class to handle DNA sequences and find open reading frames
class DNASequence:
    def __init__(self, seq):
        self.seq = seq

    def find_open_reading_frames(self):
        starts = []  # list to hold start codon positions
        for k in range(0, 3):
            line = []  # list to hold start codon positions in one frame
            for i in range(k, len(self.seq)+1, 3):
                codon = self.seq[i:i+3]
                if codon == 'ATG':
                    line.append(i)
            starts.append(line)
        strands = []  # list to hold protein strings generated from each start codon
        for j in starts:
            for n in j:
                strand = ''
                count = 0 # counter to track stop codons
                for f in range(n, len(self.seq)+1, 3):
                    codon = self.seq[f:f+3]
                    if count == 1:
                        continue
                    if codon in ['TGA', 'TAA', 'TAG']:
                        count += 1
                    if codon not in ['TGA', 'TAA', 'TAG']:
                        strand += codon
                if count < 1:
                    strand = "Stop"
                strands.append(strand)
        proteins = []  # list to hold protein sequences generated from each start codon
        for str in strands:
            seq_aa = [] # list to hold amino acids translated from each codon
            for l in range(0, len(str) + 1, 3):
                codon = str[l:l + 3]
                aa = DNA_Codons.get(codon)
                if aa not in [None, "_"]:
                    seq_aa.append(aa)
            tmp_seq = ''
            for ch in seq_aa:
                tmp_seq += ch
            proteins.append(tmp_seq)
        proteins_without_duplicates = list(set(proteins))  # remove duplicate protein sequences
        for protein in proteins_without_duplicates:
            possible_seq_of_proteins.append(protein)


# create DNASequence objects for both the forward and reverse complement strand:
print('Distinct candidate protein string that can be translated from ORFs:')
first_strand = DNASequence(DNA_string_verified)
first_strand.find_open_reading_frames()
second_strand = DNASequence(DNA_string_verified_second_strand)
second_strand.find_open_reading_frames()
possible_seq_of_proteins_without_duplicate = list(set(possible_seq_of_proteins))

# print all possible sequences without duplicates: 
for seq in possible_seq_of_proteins_without_duplicate:
    print(seq)
