from Bio import SeqIO
import math


def calculate_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)


def count_perfect_matchings(sequence):
    count_a = sequence.count('A')
    count_c = sequence.count('C')
    return calculate_factorial(count_a) * calculate_factorial(count_c)


if __name__ == "__main__":
    # Load data from the FASTA file
    with open("rosalind_pmch-4.txt", 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            sequence = str(record.seq)
            break

    # Calculate the number of perfect matchings
    perfect_matchings = count_perfect_matchings(sequence)
    print(perfect_matchings)