'''
Takes in a text file, finds out how many lines there are and splits it into smaller files. 
'''

with open('filename.txt') as jk:
    text = jk.readlines()
    size = len(text)
    new_size = print(size/5)
    
lines_per_file = 804
smallfile = None
with open('filename.txt') as bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = '{}-filename.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()
