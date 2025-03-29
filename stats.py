def reporter(path):
    with open(path) as f:
        contents = f.read()
    word_count = len(contents.split())
    charcount = {}
    for char in contents:
        if char.lower() not in charcount:
            charcount[char.lower()] = 1
        else:
            charcount[char.lower()] += 1
    ordered_chars = sorted(charcount.items(), key=lambda x:x[1],reverse=True)
    char_list = ""
    for char in ordered_chars:
        if char[0].isalpha():
            char_list+= f"{char[0]}: {char[1]}\n"

    string_one = f"============ BOOKBOT ============\nAnalyzing book found at {path}...\n----------- Word Count ----------\nFound {word_count} total words\n--------- Character Count -------\n{char_list}\n============= END ==============="
    return string_one
