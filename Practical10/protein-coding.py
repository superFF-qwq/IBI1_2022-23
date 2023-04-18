## for task3: protein-coding capability	calculator

def checkcoding(seq):
    seq = seq.upper()
    ##print(seq)
    ## change lower case to upper case
    ATG = seq.find('ATG')
    TGA = seq.find('TGA')
    distance = TGA - ATG - 3
    ## distance does NOT contain the codons themselves
    percentage = 1.0 * distance / len(seq)
    ## calculate proportion
    if distance > len(seq)*0.5:
        label = 'protein-coding'
    elif distance < len(seq)*0.1:
        label = 'non-coding'
    else:
        label = 'unclear'
    ## check the label
    return percentage, label

##seq = 'ATGGTAAGAAGCTGA'
##seq = 'acatggtagtgata'
seq = 'aCaTgGtAgTgAtA'
percentage, label = checkcoding(seq)
print(percentage, label)