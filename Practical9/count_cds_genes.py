import re

xfile =  open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')

codon = input('enter one of the three stop codons: ')
fname = codon + '_stop_genes.fa'

##print(type(fname))
##print(type(codon))

fout = open(fname, 'w')

list = []

for line in xfile:
    if line.startswith('>'): ##when meeting a '>', it means maybe a DNA ends, and exactly a DNA begins.
        if len(list)>0:
            seq = ''
            for i in list:
                seq += i[:-1] ## seq saves the gene sequence
            if re.search(codon+'$', seq):
                startposition = seq.find('ATG')
                count = len(re.findall(codon, seq[startposition:])) ##find the specific stop codon after the start codon
                fout.write(genename.group()+' '+str(count)+'\n') ##check if the DNA ends with the specific stop codon
                fout.write(seq+'\n')
        genename = re.match(r'>\S+', line)
        list.clear()
    if re.search('[AGCT]$',line): ##check if we are at a gene sequence line
        list.append(line)

if len(list)>0:
    seq = ''
    for i in list:
        seq += i[:-1]
    if re.search(codon+'$', seq):
        startposition = seq.find('ATG')
        count = len(re.findall(codon, seq[startposition:])) ##find the specific stop codon after the start codon
        fout.write(genename.group()+' '+str(count)+'\n') ##check if the DNA ends with the specific stop codon
        fout.write(seq+'\n')

if xfile:
    xfile.close()

fout.close()