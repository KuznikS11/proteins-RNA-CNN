from Bio.PDB.PDBParser import PDBParser
from Bio.PDB.PDBList import PDBList

pdbl = PDBList()

for vrstica in open('./structures lists/new structures.txt'):
    structure_id = vrstica.strip('\n')
    pdbl.retrieve_pdb_file(structure_id, file_format='pdb', pdir='pdb structures')
