# Change first arg to desired fasta file.
infile = open("test.fasta", "r", 1)

count = 0
for line in infile:
    
    if line[0] == ">":

        count += 1

print(count)
