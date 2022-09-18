"""What are the non-obvious county abbreviations, for the Texas QSO
Party?"""

with open('TX_county_abbrevs.txt') as fh:
    for line in fh:
        try:
            abbr, full = line.split()
            # print(abbr, ',', full)
        except ValueError:
            # print(line, end='')
            pass
        first4 = line[0:4]
        last4 = line[-5:-1]
        if first4.lower() != last4.lower():
            print(line, end='')
        
