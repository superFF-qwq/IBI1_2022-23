'''
The alignment score and the percentage of identical amino acids are printed in "Results.txt".

I have chosen the optional task to print non-gapped alignment.
The non-gapped alignment is printed in "alignment.txt".
'''

import blosum as bl

blosum = bl.BLOSUM(62)

catfile = open("ACE2_cat.fa","r")
mousefile = open("ACE2_mouse.fa","r")
humanfile = open("ACE2_human.fa","r")

def getgene(file):
    gene = ''
    for line in file:
        if not line.startswith('>'):
            gene = line
            break
    return gene

catgene = getgene(catfile)
mousegene = getgene(mousefile)
humangene = getgene(humanfile)

xout = open("Results.txt","w")

def score(gene1, gene2, output):
    ans = 0
    cnt = 0
##    print(len(gene1), len(gene2))
    l = min(len(gene1), len(gene2)) - 1
    for i in range(0, l):
        ans += blosum[gene1[i]][gene2[i]]
        cnt += gene1[i] == gene2[i]
##    return ans, cnt
    if output:
        cnt /= l
        xout.write("alignment score: ")
        xout.write(str(int(ans)))
        xout.write('\n')
        xout.write("percentage of identical amino acids: ")
        xout.write(str('{:.6f}'.format(cnt*100))+'%')
        xout.write('\n\n')
    return ans

xout.write("ACE2_human ACE2_mouse\n")
score(humangene, mousegene, True)
xout.write("ACE2_human ACE2_cat\n")
score(humangene, catgene, True)
xout.write("ACE2_mouse ACE2_cat\n")
score(mousegene, catgene, True)
xout.close()

def non_gapped_alignment(gene1, gene2):
    l = len(gene1) - 1
    ans = ''
    for i in range(0, l):
        if gene1[i] == gene2[i]:
            ans+=gene1[i]
        elif score(gene1[i+1:], gene2[i:], False)>score(gene1[i:], gene2[i:] ,False):
            ans+='*'
        else:
            ans+=' '
    return ans

fout = open("alignment.txt","w")
fout.write("ACE2_human ACE2_mouse\n")
fout.write(humangene)
fout.write(non_gapped_alignment(humangene, mousegene))
fout.write(mousegene)

fout.write("ACE2_human ACE2_cat\n")
fout.write(humangene)
fout.write(non_gapped_alignment(humangene, catgene))
fout.write(catgene)

fout.write("ACE2_mouse ACE2_cat\n")
fout.write(mousegene)
fout.write(non_gapped_alignment(mousegene, catgene))
fout.write(catgene)

fout.close()
