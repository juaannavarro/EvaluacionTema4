from collections import defaultdict
import time
from huffman import HuffmanCoding

DEBUG = False
DIA_FILE = 'huffman.tree'
LOG_FILE = 'log.csv'
TEST = "this is an example for huffman encoding"



"""User input
"""
txtin = input("Write some symbols(blank for sample case):")
txtin = TEST if txtin=="" else txtin
txtout = txtin

"""Extract frecuency of each symbol of set
"""
symb2freq = defaultdict(float)
for ch in txtin:
    if ch == 'a':
        symb2freq[ch] = float(0.2)
    if ch == 'f':
        symb2freq[ch] = float(0.17)
    if ch == '1':
        symb2freq[ch] = float(0.13)
    if ch == '3':
        symb2freq[ch] = float(0.21)
    if ch == '0':
        symb2freq[ch] = float(0.05)
    if ch == 'm':
        symb2freq[ch] = float(0.09)
    if ch == 't':
        symb2freq[ch] = float(0.15)
    

"""Implementation of Huffman Algorithm
"""

print("VAR", symb2freq)
start = time.time()
huff = HuffmanCoding()
huff.encode(symb2freq)
end = time.time()
time_lapse = end - start

"""Conversion from Huffman Coding Tree to Coding table
"""
coding_table = huff.tree_to_table()

"""Outputs
"""
print ("Codes table")
print ("Symbol\tFrec\tCode")
for coding in coding_table:
    print ("\t".join(map(str,coding)))
    # Replace at the input text the symbol with the propper code
    txtout = txtout.replace(coding[0],coding[2])
print ("Time: ",time_lapse,"ms")

print ("\nText input:",txtin)
print ("Text output:",txtout)

