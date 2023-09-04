import math

with open('Introduction to Randon Strings/rosalind_prob.txt') as f:
    s = f.readline().replace('\n', '')
    a = f.readline().replace('\n', '').split(' ')

gc_content = []
for gc in a:
    gc_int = float(gc)
    gc_content.append(gc_int)

prob_list = []
for i in range(0, len(a)):
    prob = 1
    for nuc in s:
        if nuc in ['C', 'G']:
            b = gc_content[i] / 2
            prob *= b
        elif nuc in ['A', 'T']:
            d = (1 - gc_content[i]) / 2
            prob *= d
    log = math.log10(prob)
    prob_list.append(log)

for el in prob_list:
    print(round(el, 3))


