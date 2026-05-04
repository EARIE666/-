with open('input.txt', 'r', encoding='utf-8') as InpFile, open('output.txt', 'a', encoding='utf-8') as OutFile:
    for line in InpFile:
        if line.strip():  # фильтрует строки с пробелами/\n с обеих сторон
            OutFile.write(line)
