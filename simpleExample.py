"""
Simple example script demonstrating how to use the pepdesMD library.

The script generates a peptide consisting of six arginines in alpha-helix
conformation, and it stores the peptide under the name "example.pdb".
"""

from pepdesMD import Geometry
import pepdesMD

# create a peptide consisting of 6 glycines
geo = Geometry.geometry("G")
geo.phi = -60
geo.psi_im1 = -40
structure = pepdesMD.initialize_res(geo)
for i in range(5):
    pepdesMD.add_residue(structure, geo)
# add terminal oxygen (OXT) to the final glycine
pepdesMD.add_terminal_OXT(structure)

import Bio.PDB

out = Bio.PDB.PDBIO()
out.set_structure(structure)
out.save("example.pdb")
