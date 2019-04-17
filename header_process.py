# Header fix
#
# OVERVIEW: The reversed fasta file needs the sequence header lines to be
# adjusted so that we can keep track of which segment is which in blast
# output. Currently, I had just added a "(Seg #)" at the end of the header
# line to differentiate between different segments of the same sequence
#
# Blast output, however, butchers the titles and that method of tracking
# which segment it came from becomes obsolete. Blast outputs an ID like so:
#
# example - NC_001422.1
#
# After speaking with Melissa, she suggested taking out everything from
# the segment 
# Need to adjust the titles accordingly:
#
# 1) Add segment number to ID above, for example, NC_001422.1.1 or
# NC_001422.seg1 or NC_001422.S1


# This function will pre-process sequences so that the header lines are fixed
def header_fixer(filename):

    # Create input file stream
    infile = open(filename, "r", 1)

    # Create filename for output
    output_filename = ""
    for c in filename:
        if c == ".":
            output_filename += "_headerfix"
        output_filename += c

    # Create output file stream
    output = open(output_filename, "w", 1)

    
    # Loop to read in every line
    for line in infile:

        # Check if header
        if line[0] == ">":
            header = ""
            for char in line:
                if char == " ":
                    break
                else:
                    header += char

            output.write(header)
            output.write("\n")
        # Check if line begins with \n char
        elif line[0] == "\n":
            output.write(line)
            
        # Check if line begins with valid BP
        elif line[0] == "A" or line[0] == "C" or line[0] == "T" or line[0] == "G":
            output.write(line)

    # for
# header_fixer

#MAIN

string = input("File: ")
print("Fixing headers...")
header_fixer(string)
print("Done!")
    
    
