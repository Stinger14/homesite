import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}

def list_of_occurrences():
    """
    Build an index mapping word, handle missing ke
    """
    #
    with open(sys.argv[1], encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start() + 1
                location = (line_no, column_no)
                occurrences = index.get(word, [])
                occurrences.append(location)
                index[word] = occurrences

    for word in sorted(index, key=str.upper):
        print(word, index[word])

def list_of_occurrences2():
    """
    Handling Missing Keys with setdefault
    """
    with open(sys.argv[1], encoding='utf-8') as fp: 
        for line_no, line in enumerate(fp, 1):
            for match in WORD_RE.finditer(line):
                word = match.group()
                column_no = match.start()+1
                location = (line_no, column_no) 
                index.setdefault(word, []).append(location)

    for word in sorted(index, key=str.upper):
        print(word, index[word])

list_of_occurrences2()
