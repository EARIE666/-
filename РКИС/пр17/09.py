# File: 09.py
def task9():
    filenames = ['file1.txt', 'file2.txt']
    with open('result.txt', 'w', encoding='utf-8') as outfile:
        for fname in filenames:
            with open(fname, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
                outfile.write('\n') # разделитель между файлами
