with open("rosalind_hamm.txt", "r") as file:
    content_string1 = file.readline()
    content_string2 = file.readline()


def hamming_distance_count(str1, str2):
    hamming_distance = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            hamming_distance += 1
    return hamming_distance


count = hamming_distance_count(content_string1, content_string2)
print(count)


