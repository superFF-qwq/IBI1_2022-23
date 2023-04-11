##This code can deal with the situation where the gene sequence exists more than one 'ATG'

import re

#seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
##seq = 'ATGTAATGATAA'
##seq = 'AAA'


##start codon: ATG
##stop codons: TAA TAG TGA

##print(seq.find('ATG'))
##print(re.match('ATG',seq).span()[0])

now = 0 ## the present dealing position
ans = 0

#print(type(seq[1:]))
#print(type(seq))

while True:
        result = re.match('ATG',seq[now:])
        if result == None:
            break
        startposition = result.span()[0] ##startposition marks the postion of the first ATG
        if startposition == -1:
            break
        countTAA = len(re.findall(r'TAA',seq[startposition:]))
        countTAG = len(re.findall(r'TAG',seq[startposition:]))
        countTGA = len(re.findall(r'TGA',seq[startposition:]))
        #seperate the question into subquestions to respectively calculate the three kinds of stop codons.
        ans += countTAA + countTAG + countTGA
        '''
        print('now = ')
        print(now)
        print('ans = ')
        print(ans)
        '''
        now = startposition + 1 ## jump behind the current ATG
        
print(ans)
        
'''
I think the above solution is not correct. Here is hack data:
seq = 'ATGTAATGAATGTAA'
it cannot correctly calculate the situations where the same stop codon occurs more than once
the standard answer is 3.
'''