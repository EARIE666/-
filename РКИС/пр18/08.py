with open('input.txt', 'r', encoding='utf-8') as InpFile:
    text = InpFile.read()
    if not text:
        print('Empty')
    else:
        print(text)
