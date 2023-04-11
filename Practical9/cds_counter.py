import re

##seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
seq = 'ATGTAATGATAA'


##start codon: ATG
##stop codons: TAA TAG TGA

##print(seq.find('ATG'))

startposition = seq.find('ATG')

##print(re.findall(r'ATG.*TAA',seq))
##print(re.findall(r'ATG.*TAG',seq))
##print(re.findall(r'ATG.*TGA',seq))

##I think the above solution is not correct. Here is hack data:
##seq = 'ATGTAATGATAA'
##it cannot correctly calculate the situations where the same stop codon occurs more than once
##the standard answer is 3, but the above solution would give 2.

##print(re.findall(r'TAA',seq[startposition:]))
##print(re.findall(r'TAG',seq[startposition:]))
##print(re.findall(r'TGA',seq[startposition:]))

##solution: I seperate the question into three subquestions to respectively calculate the three kinds of mRNA sequences.

countTAA = len(re.findall(r'TAA',seq[startposition:]))
countTAG = len(re.findall(r'TAG',seq[startposition:]))
countTGA = len(re.findall(r'TGA',seq[startposition:]))

print(countTAA+countTAG+countTGA)