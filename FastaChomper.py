####################################################################################### 
#
# Sub set only certain transcripts from a fasta file.
#
# Usage: FastaChomper.py <options> -f <fasta> -l <idlist> -o <output>
#
# Where:
# fasta = the fasta file containing all the sequences
# idlist = List of sequences IDs to keep or exclude from the fasta file. One per line.
# output = Name of the output file
#
# Options:
# -i = Keep only the sequences of the Ids included in the list
# -e = Exclude the sequence of the Ids in the list
# 
#######################################################################################

#!/usr/bin/python

import sys, getopt
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

genes_seq = dict()

Ids = list()

fasta = ""
input1 = ""
keep = 0
exclude = 0
outputfile = ""

# Check for the arguments and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hief:l:o:",["fasta=","idlist=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage: FastaChomper.py <options> -f <fasta> -l <idlist> -o <output>'
    print 'For help use ClustersSeq_Corset.py -h'
    sys.exit(99)

for opt, arg in opts:
    if opt == '-h':
        print '\n', 'Sub set only certain transcripts from a fasta file.', '\n'
        print 'Usage: FastaChomper.py <options> -f <fasta> -l <idlist> -o <output>', '\n'
        print 'Where: fasta = the fasta file containing all the sequences'
        print 'idlist = List of sequences IDs to keep or exclude from the fasta file. One per line.'
        print 'output = Name of the output file' , '\n'
        print 'Options:'
        print '-i = Keep only the sequences of the Ids included in the list'
        print '-e = Exclude the sequence of the Ids in the list'
        sys.exit()
    elif opt == "-i":
        keep = 1
    elif opt == "-e":
        exclude = 1
    elif opt in ("-f", "--fasta"):
        fasta = open(arg)
    elif opt in ("-l", "--idlist"):
        input1 = open(arg)
    elif opt in ("-o", "--output"):
        outname = arg + ".fasta"
        outputfile = open(outname,"w")
    else:
        assert False, "unhandled option"


## Make a list of the transcript IDs to search
for line in input1:
    list = line.split()
    id = list[0]
    Ids.append(id)


## Open the fasta file and save the information the user wants
for seq_record in SeqIO.parse(fasta, "fasta"):
    gene_id = seq_record.id
    bases = (seq_record.seq)
    genes_seq[gene_id]= bases
    
## Open the fasta file and save the information the user wants
for seq_record in SeqIO.parse(fasta, "fasta"):
    gene_id = str(seq_record.id)
    bases = (seq_record.seq)
    genes_seq[gene_id]= bases
    if exclude == 1 and gene_id not in Ids:
            fasta_format_string = SeqRecord(bases, id=gene_id)
            outputfile.write(fasta_format_string.format("fasta"))

if keep == 1 :
    for id in Ids:
        fasta_format_string = SeqRecord(genes_seq[id], id=id)
        outputfile.write(fasta_format_string.format("fasta"))
    
        
outputfile.close()
