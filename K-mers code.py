from Bio import SeqIO
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import re

def Kmers_funct(seq, size):
    return [seq[x:x+size] for x in range(len(seq) - size + 1)]

X = np.empty((0, 2097152), int)

with open('K-mer array.txt', 'w') as outfile:
    for sequence in SeqIO.parse('file name', "fasta"):
        sequence_id = sequence.id
        sequence_string = str(sequence.seq)

        encoded_sequence = Kmers_funct(sequence_string, size=7)

        cv = CountVectorizer(analyzer=lambda x: x)
        X_seq = cv.fit_transform(encoded_sequence).toarray()

        outfile.write(f'>{sequence_id}\n')
        outfile.write(f'{sequence_string}\n')
        outfile.write(f'K-mer counts:\n')
        outfile.write(f'{X_seq}\n\n')
    
      

