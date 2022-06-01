lst = ['text2.txt', 'text3.txt', 'text4.txt']
dictionary = {}
for element in lst:
    with open(element, 'r', encoding='utf-8') as infile:
        length = len(infile.readlines())
        dictionary[element] = length
sorted_keys = sorted(dictionary, key=dictionary.get)
with open('result.txt', 'w', encoding='utf-8') as outfile:
    for element in sorted_keys:
        with open(element, 'r', encoding='utf-8') as infile:
            file = infile.read()
            outfile.write(element + '\n')
            outfile.write(str(dictionary[element])+ '\n')
            outfile.write(file + '\n')




