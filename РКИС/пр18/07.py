with open('input.txt', 'r', encoding='utf-8') as InpFile, open('output.txt', 'w', encoding='utf-8') as OutFile:
    content = InpFile.read()
    OutFile.write(content)
