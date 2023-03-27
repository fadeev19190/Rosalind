with open("rosalind_subs.txt", "r") as file:
    DNA_string_s = file.readline()
    DNA_string_t = 'CCGTTCTCC'

print(DNA_string_s)


def finding_motif(seq):
    position = 0
    for i in range(0, len(DNA_string_s)):
        motif = DNA_string_s[i:i+len(DNA_string_t)]
        position += 1
        if motif == DNA_string_t:
            print(position)
            

finding_motif(DNA_string_s)