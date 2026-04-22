#!/usr/bin/env python3

import csv

def read_fasta(fasta_file):
    # make a variable to store the genome sequence
    seq = ''
    with open(fasta_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                continue
            else:
                seq += line.rstrip()
    return seq

def read_gff(gff3_file, genome_sequence):
    with open(gff3_file, "r") as g:
        # create a csv reader object
        reader = csv.reader(g, delimiter='\t')

        # read the file line by line
        for line in reader:
            start = int(line[3]) - 1
            end = int(line[4]) # no need to change end values
            feature_seq = genome_sequence[start:end]
            #print(start, end, len(feature_seq),atts)
            atts = line[8]
            atts_list = atts.split(':')
            a = atts_list[0].split('=')
            gene_name = a[-1]
            #print(gene_name)

            write_output(gene_name, feature_seq)



def write_output(name, seq):
    print(f">{name}")
    print(seq)



# set the environment for this script
# is it main(), or is this a module being called by something else?
if __name__ == '__main__':
    main()