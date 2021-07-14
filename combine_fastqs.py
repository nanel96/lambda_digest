from Bio import SeqIO
import glob
files = glob.glob('*.fastq')
with open('pass/combined_reads.fastq', 'w') as outfile:
    for file in files:
        for seq_record in SeqIO.parse(file, 'fastq'):
            outfile.write(seq_record.format('fastq'))
close(outfile)