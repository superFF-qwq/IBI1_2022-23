import re

xfile =  open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

codon = input('enter one of the three stop codons: ')
fname = codon + '_stop_genes.fa'

##print(type(fname))
##print(type(codon))

fout = open(fname, 'w')

list = []
ans = []

for line in xfile:
    if line.startswith('>'):
        if len(list)>0:
            seq = ''
            for i in list:
                seq += i[:-1]
            if re.search(codon+'$', seq):
                fout.write(genename.group()+'\n')
                fout.write(seq+'\n')
            startposition = seq.find('ATG')
            count = len(re.findall(codon, seq[startposition:]))
            ans.append(genename.group()+' '+str(count))
        genename = re.match(r'>\S+', line)
        list.clear()
    if re.search('[AGCT]$',line):
        list.append(line)

if len(list)>0:
    seq = ''
    for i in list:
        seq += i[:-1]
    if re.search(codon+'$', seq):
        fout.write(genename.group()+'\n')
        fout.write(seq+'\n')
    startposition = seq.find('ATG')
    count = len(re.findall(codon, seq[startposition:]))
    ans.append(genename.group()+' '+str(count))
    
for i in ans:
    fout.write(i[1:]+'\n')

fout.close()