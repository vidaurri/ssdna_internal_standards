README Overview for all scripts I have created so far

This will be a quick guide for using my scripts and explaining their purpose.
GENERAL USAGE:
	1. Run fasta file through header_process.py
	2. Run file generated from header_process.py through multi_seq.py
	3. Use file generated from 2 to run with BLAST on flux
	4. Run extract_candidates.py to generate candidates

	** For more details on using each individual script, read below.


FILE SUMMARIES:
Here is a quick summary and usage guide for using these scripts. For a much more detailed look at how they work,
you'll find that the file is extensively commented and has also has usage instructions. The general order of usage is as follows

header_process.py:
	multi_seq originially just added "(Seg #)" to the header line for each fragmented sequence
	However, BLAST output butchers titles and renders this method for keeping track of what sequence is what obsolete.
	Blast outputs ID like so: NC_001422.1 ---> lose the fragment number
	So, this script will preprocess the fasta file and fix headers to an easy-to-track format along with handling incorrect header format and invalid sequence BP chars
	USAGE: Running script will prompt user for a fasta filename. Outputs a new fasta file [infile]_headerfix.fasta, fixed headers and characters for later use.
	***Should run a fasta file through this before using multi_seq***

seg_counter.py:
	Super basic script that will count the number of sequences in the fasta file, used as a helper function for multi_seq.py
	Works by just counting how many times ">" appears in the file (invariant: properly formatted fasta file)
	To use, just modify the first line to have the name of the fasta file to count segments, and run it
	Returns number of sequences, used as helper function in multi_seq

multi_seq.py:
	Script takes a fasta file with multiple sequences, and individually reverses and fragments each sequence while maintaining format.
	Program will ask user to input a fasta file and the segment/fragment size (in bps) when run
	Cleans up the format to ensure a max of 80 characters per line for the sequence
	Creates an output file [infile]_processed.fasta that is reversed/fragmented
	USAGE: Prompts user for filename and segment size. Outputs a new fasta file that is reversed/fragmented


After using this, the [filename]_headerfix_processed.fasta is ready to be run with blast.


extract_candidates.py:
	This file is more involved with the user and requires more input
	A few uses: 
	- calculates the gc content of a fasta file, creates output file with only the sequence header and its GC content (_gc appended)
	- asks for blast output, will select candidates based on user input of minimum e_val
	More in depth usage:
	1. Prompts user for a headerfix_processed fasta file to calculate the GC content of each sequenece in the file. Generates output file with the header followed by gc content on the next line
	2. Prompts user for blast output file to select candidates and the desired minimum e_val. Will then prompt the user for the gc file created above
	3. Script will create another output file, with the e_val appended to the file name, which contains candidates with the minimum e_val.
		- Format of the output is query_id or header, subject id, e_value, bit_score, and gc content on each line separated by tabs.

