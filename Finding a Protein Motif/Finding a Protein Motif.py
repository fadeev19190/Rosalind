# Import the "requests" module to make HTTP requests to the UniProt API.
import requests

# define the UniProt API URL to query
url = "https://www.uniprot.org/uniprot/{peptide}.fasta"

# define a list of peptides to retrieve sequences for
with open('Finding a Protein Motif/rosalind_mprt-9.txt', 'r') as file:
    peptides = file.read().replace('\n', ' ')
    peptides_list = peptides.rsplit(' ')
    peptides_list.pop(-1)

# Remove any underscores in each peptide's name and store them in a new list called "peptides_list_end".
peptides_list_end = []
for prot in peptides_list:
    temp = ''
    for char in prot:
        if char != '_':
            temp += char
        else:
            break
    peptides_list_end.append(temp)

print(peptides_list_end)

# initialize a dictionary to store the sequences of the peptides
peptide_sequences = {}

# loop through each peptide and retrieve its sequence from UniProt
for peptide in peptides_list_end:
    # format the URL with the peptide name
    peptide_url = url.format(peptide=peptide)

    # send a GET request to the UniProt API to retrieve the peptide sequence
    response = requests.get(peptide_url)

    # parse the response content and retrieve the sequence
    sequence = ''.join(response.content.decode("utf-8").split("\n")[1:])

    # add the peptide name and sequence to the dictionary
    peptide_sequences[peptide] = sequence

# print the dictionary of peptide sequences
print(peptide_sequences)


def glycosylation_motif(seq, peptide_list):
    # Loop through each peptide in the "peptide_list" and print its name.
    for k in range(len(peptide_list)):
        print('\n', peptides_list[k])
        for prot in seq:
            # Loop through each protein in "seq" and check if its name matches the first 6 characters of the current peptide's name.
            if prot == peptide_list[k][0:6]:
                prot_seq = seq.get(prot)
                # If there is a match, loop through each amino acid in the protein's sequence and check if it matches the glycosylation motif (NxS/T, where x is any amino acid except proline).
                for i in range(len(prot_seq)):
                    if i + 3 <= len(prot_seq):
                        if prot_seq[i] == 'N':
                             if prot_seq[i + 1] != "P":
                                if prot_seq[i+2] in ["S", "T"]:
                                    if prot_seq[i + 3] != "P":
                                        # If a match is found, print the index of the amino acid in the protein's sequence.
                                        print(i+1, end=' ')


glycosylation_motif(peptide_sequences, peptides_list_end)
