####################################################################################### 
#
# Select only the longest "genes" from all the transcripts assembled through the Trinity 
# de novo assembly and save them in a new fasta file excluding the different isoforms of 
# the same gene
#
# Usage: find_Trinity_genes.py -i <transcripts.fasta> -o <outprefix> 
#
# Where:
# transcripts.fasta = resulting fasta file from Trinity de novo assembly containing all 
#                     the "genes" and its isoforms
# outprefix = Trinity "genes" only fasta file output
#
#######################################################################################

#!/usr/bin/python

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

import re, sys, getopt

genes_size = dict()
genes_seq = dict()
fasta = ""
outputfile = ""


try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["input=","outprefix="])
except getopt.GetoptError:
    print 'find_Trinity_genes.py -i <transcripts.fasta> -o <outprefix>'
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print 'find_Trinity_genes.py -i <transcripts.fasta> -o <outprefix>'
        sys.exit()
    elif opt in ("-i", "--input"):
        fasta = open(arg)
    elif opt in ("-o", "--outprefix"):
        outname = arg + ".fasta"
        outputfile = open(outname,"w")


# Look for the gene ID in the input fasta and count the sequence length

for seq_record in SeqIO.parse(fasta, "fasta"):
    full_seq = seq_record.id
    part = full_seq.split('_i')
    gene_id = part[0]
    seq_length = (len(seq_record))
    bases = (seq_record.seq)
      
 # Keep only the longest gene for each gene name
    if gene_id not in genes_size or seq_length > genes_size[gene_id]:
        genes_size[gene_id]= seq_length
        genes_seq[gene_id]= bases
             
# Recover the nucleotide sequence of the longest genes and save it in the output fasta file
for k,v in genes_seq.items():
    fasta_format_string = SeqRecord(v, id=k)
    outputfile.write(fasta_format_string.format("fasta"))
       
        
outputfile.close()
