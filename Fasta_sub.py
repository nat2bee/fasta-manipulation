####################################################################################### 
#
# Sub set first X sequences from a fasta file.
#
# Usage: Fasta_sub.py -n <number_of_sequences> -f <fasta> -o <output>
#
# Where:
# number_of_sequences = how many sequences do you want to extract
# fasta = the fasta file containing all the sequences
# output = Name of the output file
#
# 
#######################################################################################

#!/usr/bin/python

import sys, getopt
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord


fasta = ""
input1 = ""
n_seqs = 0
n = 0
outputfile = ""

# Check for the arguments and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hn:f:o:")
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage: Fasta_sub.py -n <number_of_sequences> -f <fasta> -o <output>'
    print 'For help use Fasta_sub.py -h'
    sys.exit(99)

for opt, arg in opts:
    if opt == '-h':
        print '\n', 'Sub set first X sequences from a fasta file.', '\n'
        print 'Usage: Fasta_sub.py -n <number_of_sequences> -f <fasta> -o <output>', '\n'
        print 'Where: number_of_sequences = how many sequences do you want to extract'
        print 'fasta = the fasta file containing all the sequences'
        print 'output = Name of the output file' , '\n'
        sys.exit()
    elif opt == "-n":
        n_seqs = int(arg)
    elif opt in ("-f", "--fasta"):
        fasta = open(arg)
    elif opt in ("-o", "--output"):
        outname = arg + ".fasta"
        outputfile = open(outname,"w")
    else:
        assert False, "unhandled option"


## Open the fasta file and save the information the user wants

for seq_record in SeqIO.parse(fasta, "fasta"):
    if n < n_seqs:
        gene_id = str(seq_record.id)
        bases = (seq_record.seq)
        fasta_format_string = SeqRecord(bases, id=gene_id)
        outputfile.write(fasta_format_string.format("fasta"))
        n = n+1
    else:
     outputfile.close()
     sys.exit(0)
