writeList = []
with open('input.txt', 'r', encoding='utf-8') as InpFile, open('output.txt', 'w', encoding='utf-8') as OutFile:
    for line in InpFile:
        if len(line.rstrip()) > 5:
            writeList.append(line.rstrip()) 
    OutFile.write('\n'.join(writeList))
