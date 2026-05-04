with open('input.txt', 'r', encoding='utf-8') as infile, open('output.txt', 'w', encoding='utf-8') as outfile:
    for i, line in enumerate(infile, start=1):
        outfile.write(f'{i}: {line}')
