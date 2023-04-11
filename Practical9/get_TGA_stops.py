import re

xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
fout = open('TGA_genes.fa', 'w')

##length = 0
##for i in xfile:
##    length = length + 1

##print(length)

##print(type(xfile))

list = []

for line in xfile:
    if line.startswith('>'):
        if len(list)>0 and re.search('TGA\n$',list[-1]):
            fout.write(genename.group()+'\n')
            for i in list:
                fout.write(i[:-1])
            fout.write('\n')
        genename = re.match(r'>\S+', line)
        list.clear()
    if re.search('[AGCT]$',line):
        list.append(line)

## do not forget to deal with the last gene sequence

if len(list)>0 and re.search('TGA\n$',list[-1]):
    fout.write(genename.group()+'\n')
    for i in list:
        fout.write(i[:-1])
    fout.write('\n')

fout.close()