#******************************************************************************
# relatives.py
#******************************************************************************
# Name: Abrar Alsayedi 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#https://chatgpt.com/share/6a6e567a-78f4-83ea-9361-cdea5dc9fa44
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
# 
# 

def dis(string1, string2):
    count = 0

    for c in range(100):
        if string1[c] != string2[c]:
            count += 1

    return count


f = open('dna.txt', 'r')
dna = f.readlines()


lis = []
rows = []

for i in range(200):
    for r in range(i + 1, 200):
        d = dis(dna[i], dna[r])
        lis.append(d)
        rows.append([i, r])


ind = lis.index(min(lis))
m = min(lis)

r1 = rows[ind][0]
r2 = rows[ind][1]

dnar1 = dna[r1]
dnar2 = dna[r2]

f.close()

print(f'The relatives are found in row {r1 + 1} and row {r2 + 1} with a dissimilarity of {m}.')
print(dnar1.strip())
print(dnar2.strip())