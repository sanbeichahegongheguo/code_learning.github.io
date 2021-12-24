import re


with open('./Go学习入门/src/SUMMARY.md', 'r', encoding='utf-8', errors='ignore') as f:
    c = 4
    pattern1 = re.compile(r'\((.*)\)')
    pattern2 = re.compile(r'\[([0-9]{1,2}\.[0-9]{1,2})\s(.*)\]')

    for line in f.readlines():
        name1 = pattern1.search(line)
        name2 = pattern2.search(line)
        if name1 is not None and name2 is not None:
            # print(name1.group(1))
            # print(name2.group(2))
            if c < 10:
                numb = "00" + str(c)
            elif c < 100:
                numb = "0" + str(c)
            else:
                numb = str(c)
            newname = name2.group(2)
            name3 = re.sub(r'(\s)', "_", newname)
            name4 = "./" + numb + "_" + name3 + ".md"
            # print(name4)
            newline = re.sub(name1.group(1), name4, line)

            print(newline)
            c += 1
