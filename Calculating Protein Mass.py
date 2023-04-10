from bio_structs import amino_acid_mass

with open('rosalind_prtm.txt') as file:
    peptide = file.read()

total_mass = 0

for aa in peptide:
    mass = amino_acid_mass.get(aa)
    if mass is not None:
        total_mass += mass

print(total_mass)