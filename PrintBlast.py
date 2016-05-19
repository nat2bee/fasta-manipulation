#!/usr/bin/python

####################################################################################### 
#
# Print useful information from blast alignments in a table format.
#
# Usage: PrintBlast.py -b <blastresult.xml> -o <output.txt>
#
# Where:
# blastresult.xml = blast result in xml format
# output.txt = the name of the file to save the output table
#
# Options: -h for usage help
#
# Outputs: A table named as your -o option containing essential information about your blast results
#
#######################################################################################

import re, sys, getopt

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIXML

blast = ""

n = 0
a = 100000



# Check for the arguments, open the inputs and print useful help messages

try:
    opts, args = getopt.getopt(sys.argv[1:],"hb:o:",["blast=","output="])
except getopt.GetoptError:
    print '\n', '####     Invalid use     ####', '\n'
    print 'Usage: PrintBlast.py -b <blastresult.xml> -o <output.txt>'
    print 'For help use PrintBlast.py -h'
    sys.exit(99)
    

for opt, arg in opts:
    if opt == '-h':
        print '\n', 'Print useful information from blast alignment in a table format.', '\n'
        print 'Usage: PrintBlast.py -b <blastresult.xml> -o <output.txt>', '\n'
        print 'Where: blastresult.xml = blast result in xml format'
        print 'output.txt = the name of the file to save the output table'
        sys.exit()
    elif len(arg) >= 2:
        if opt in ("-b"):
            blast = open(arg)
            blast_records = NCBIXML.parse(blast)
        if opt in ("-o"):
            output = open(arg,"w")
    elif len(arg) < 2:
        print '\n', '###    Arguments are missing   ###', '\n', '\n' 'Use -h option for help\n'
        sys.exit(1)
    else:
        assert False, "unhandled option"


# Creating the output header

output.write("Name\tQuery_ID\tQuery_length\tSubjct_ID\tSubjct_length\tAlignment_length\te-value\tgaps\tsimilarity\tPosition_Sbjct\n")
			   
# Parsing the information of interest and write it in the output

for rec in blast_records:
	for alignment in rec.alignments:
			for hsp in alignment.hsps:
			    query = rec.query
			    query = query.split(' ')
			    query_id = str(query[0])
			    hit = alignment.hit_def
			    hit = hit.split(' ')
			    hit_id = str(hit[0])
			    output.write(str(alignment.title) + "\t" + query_id + "\t" + str(rec.query_length) + "\t" + hit_id + "\t" +
			    str(rec.database_length) + "\t" + str(hsp.align_length) + '\t' + str(hsp.expect) + '\t' + 
			    str(hsp.gaps) + '\t' + str(float(hsp.identities)/int(hsp.align_length)) + "\t" + str(hsp.sbjct_start) + "-" + str(hsp.sbjct_end) + "\n")   
			    n = n + 1 
			    if n == a:
			        print n, "Hsp already checked. Please wait..."
			        a = a + 100000


output.close() 
sys.exit(0)
