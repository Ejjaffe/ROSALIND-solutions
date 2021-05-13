"""
Transcribing DNA into RNA
http://rosalind.info/problems/rna/
"""

def dna_2_rna(dna_str):
	"""
	Transcribes DNA into RNA
	
	RNA differs from DNA in that it contains a base called uracil in place of thymine.
	An RNA string is formed by replacing all occurrences of 'T' in the DNA string with 'U'.
	
	Params:
	-------
		dna_str: (str)
			DNA string. For example: "GATGGAACTTGACTACGTAAATT"
	Returns:
	--------
		rna_str: (str)
			RNA string. Example from above returns "GAUGGAACUUGACUACGUAAAUU"
	"""
	return dna_str.replace('T','U')


if __name__ == '__main__':
	with open(r"C:\path\to\rosalind_rna.txt") as file:
		line = file.read()
		print(dna_2_rna(line))
