k = []

with open("test_text_file.txt") as f:
    for line in f:
        print(line)
        print(type(line))