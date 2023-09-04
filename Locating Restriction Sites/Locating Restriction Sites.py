def reverse_complement(seq):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(seq))


def find_restriction_sites(dna_seq):
    restriction_sites = []
    seq_length = len(dna_seq)

    for i in range(seq_length):
        for j in range(i + 4, min(i + 13, seq_length + 1)):
            fragment = dna_seq[i:j]
            rev_complement = reverse_complement(fragment)
            if fragment == rev_complement:
                restriction_sites.append((i + 1, len(fragment)))

    return restriction_sites


dna_sequence = ''
with open('Locating Restriction Sites/rosalind_revp.txt', "r") as file:
    dna_sequence_list = file.readlines()[1:]
    for line in dna_sequence_list:
        dna_sequence += line.rstrip()

print(dna_sequence)

sites = find_restriction_sites(dna_sequence)
for site in sites:
    print(f"{site[0]} {site[1]}")
