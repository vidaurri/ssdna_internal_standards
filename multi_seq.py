import math
# OVERVIEW: I need to create a script that can take a multi fasta file,
# containing multiple sequences, and individually reverse and fragment
# the sequences, maintaining fasta format
#
# KEY FEATURES: Example of content of multifasta file below:
#   1.  Header line: contains header info, denoted by ">"
#   2.  Sequence: the dna sequence, immediately after the header line.
#           - Lines should be a maximum of 80 characters
#
#   e.g.
#           >Sequence 1
#           ABCDEKAJDJSKAHSFJS
#           AJSDOOJASDJSJDLJSD
#           ASKDJ
#
#           >Sequence 2
#           AKSJDKSJLAAJSDKKSL
#           ASKDJSALDKLKSDJLSL
#           ASLKDLSJFHSLMNVMLS
#           LKMFKLSDKLKKSL
#
#   NOTE:   Not 100% certain if there should be a new line inbetween sequences
#           as above.
#
# PROCESS:
#   1. Read in each line from the file
#   2. If first char in the line is a >, store as header info
#   3. Else if it is a character, add it to the string
#.  4. Else (it is an empty line), reverse, segment, and output the data

# These are the containers needed to store the read in information
sequences = []
headers = []

# Reverse helper function
# REQUIRES: string as input (aka entire sequence
# EFFECTS: reverses the string (sequence)
def reverse(string):
    string = string[::-1]
    return string


# This function reads in the data from the file, storing them in the
# 2d list sequences. This also reverses the individual sequences
def read_in(filename):

    # Create input file stream
    infile = open(filename, "r", 1)

    # chars string will hold individual sequences
    chars = ""

    # Loop to read in every line
    for line in infile:

        # If line starts with >, its a header
        if line[0] == ">":
            headers.append(line)

        # If line starts with \n, it is the end of a sequence
        # Therefore, add the reversed string to the sequences list!
        elif line[0] == "\n":
            chars = reverse(chars)
            sequences.append(chars)
            chars = ""

        # If it isn't a header or the end of a sequence, it is the data
        # Concatenate the data into a string
        else:
            for c in line:
                if c != "\n":
                    chars += c

    #print(headers)
    #print(sequences)
    

# This function does the bulk of the processing. It redirects input
# to an output file, splitting sequences into segments of desired size
# while maintaining readability, clarity, and fasta format
def multi_algo(filename, segment_size):

    # Reads in the data
    read_in(filename)

    # print(headers) <- DEBUG CODE

    # Creates the filename for the output.
    # Configured to [infile]_processed.fasta
    output_filename = ""
    for c in filename:
        if  c == ".":
            output_filename += "_processed"
        output_filename += c

    # Creates the output file stream
    output = open(output_filename, "w", 1)

    # Counter helps for keeping track of which sequence you are on
    header_counter = 0;

    # Nested for loop
    # Outer loop iterates through the individual sequences in the list
    for string in sequences:

        # More counters to help keep track of indices
        # char -> index of char to note when to segment
        # col -> index of column for output file (keeps readability)
        # seg -> keeps track of the segments of each sequence
        char_counter = 0
        col_counter = 0
        seg_counter = 1

        # Inner loop iterates through all BP in the sequence
        for char in string:

            # Checks to see if you should move to next segment
            if char_counter % segment_size == 0:

                # Takes care of newline output consistency
                if char_counter != 0:
                    output.write("\n\n")

                # Series of strings to show which segment you are on
                unchecked = headers[header_counter]
                checked = unchecked[:len(unchecked)-1]

                # UPDATE 3/10: Changed from this -
                # updated = checked + " (Seg " + str(seg_counter) + ")\n"
                # To this (for blast output header issues)
                updated = checked + "_S" + str(seg_counter) + "\n"

                # Sends header with segment number to output
                output.write(updated)

                # Resets/updates counters
                # col needed to ensure output is consistent
                col_counter = 0
                seg_counter += 1
                
            # Ensures lines are no longer than 80 chars/col long
            elif col_counter % 80 == 0 and char_counter != 0:
                output.write("\n")

            # Writes the current BP to output
            output.write(char)

            # Updates counters
            char_counter += 1
            col_counter += 1
            
        # for
        # Signifies a new sequence
        output.write("\n\n")
        header_counter += 1
            
     
# ---------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------


string1 = input("File: ")
segsize = int(input("Segment size: "))
print("Processing data...")
multi_algo(string1, segsize)
print("Done!")

