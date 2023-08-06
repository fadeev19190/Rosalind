"""
Solution of  problem calls 'Calculating Expected Offspring'
https://rosalind.info/problems/iev/

Probability of get offspring with dominant fenotype:
1. AA-AA - 1
2. AA-Aa - 1
3. AA-aa - 1
4. Aa-Aa - 3/4
5. Aa-aa - 1/2
6. aa-aa - 0

My dataset:
19864 18671 16338 17525 19840 17878
"""
# sum quantity of the first three genotypes because they give us the same probability
sum_first_three = 19864 + 18671 + 16338
population = {
    1: sum_first_three,
    3 / 4: 17525,
    1 / 2: 19840,
    0: 17878
}


def cal_exp_offspring(population):
    sum_off = 0
    for item in population:
        temp = population.get(item) * item * 2
        sum_off += temp
    return sum_off


print(cal_exp_offspring(population))
