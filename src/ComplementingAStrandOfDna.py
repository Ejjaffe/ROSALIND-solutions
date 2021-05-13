"""
Complementing a Strand of DNA
http://rosalind.info/problems/revc/
"""

BP_COMPLIMENTS = {
	'A':'T',
	'T':'A',
	'C':'G',
	'G':'C',
}

def reverse_compliment(dna):
	"""
	The reverse complement of a DNA string s is the string s^c formed by reversing the symbols of s, 
	then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").
	
	In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
	
	Params:
	-------
		dna: (str)
			string, hopefully containing characters from the alphabet "ATCG"
	
	Returns:
	--------
		str, reverse compliment of dna
	"""
	compliments = [BP_COMPLIMENTS[c] for c in dna if c in BP_COMPLIMENTS.keys()]
	reverse_compliments = compliments[::-1]
	return "".join(reverse_compliments)


if __name__ == '__main__':
	with open(r"C:\path\to\rosalind_revc.txt") as file:
		line = file.read()
		print(reverse_compliment(line))
	
