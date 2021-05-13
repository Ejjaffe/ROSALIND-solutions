"""
Counting DNA Nucleotides
http://rosalind.info/problems/dna/
"""
from collections import Counter

def count_nucleotides(dna_str):
    """
    Count nucleotides A C G T and return them as integers separated by spaces.
	
	Turns "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
	into "20 12 17 21"
    
    Params:
    -------
        dna_str: (str)
            string containing nucleotides (ATCG))
    
    Returns:
	--------
        problem output: str with count of each nucleotide: 'A C G T'
		
	ATCG 
    """
    
    # Count the symbols (treats a string like an iterable)
    ctr = Counter(dna_str)
	
    # specify order ACGT and format between spaces
    order_cts = [ctr[symb] for symb in ['A','C','G','T']]
    return " ".join(str(ct) for ct in order_cts)
