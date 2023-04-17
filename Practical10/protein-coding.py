## for task3: protein-coding capability	calculator

def checkcoding(seq):
    for i in range(0,len(seq)):
        if 'a'<=seq[i] and seq[i]<='z':
            seq[i]=seq[i]-'a'+'A'
    ATG = seq.find('ATG')
    TGA = seq.find('TGA')
    distance = TGA - ATG
    percentage = 1.0 * distance / len(seq)
    if distance > len(seq)*0.5:
        label = 'protein-coding'
    elif distance < len(seq)*0.1:
        label = 'non-coding'
    else:
        label = 'unclear'
    return percentage, label

seq = 'ATGGTAAGAAGCTGA'
percentage, label = checkcoding(seq)
print(percentage, label)