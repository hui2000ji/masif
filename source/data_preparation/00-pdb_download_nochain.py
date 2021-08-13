#!/usr/bin/python
import Bio
from Bio.PDB import * 
import sys
import importlib
import os

from default_config.masif_opts import masif_opts
# Local includes
from input_output.protonate import protonate

if not os.path.exists(masif_opts['raw_pdb_dir'][:-1]+"_protonized"):
    os.mkdir(masif_opts['raw_pdb_dir'][:-1]+"_protonized")

pdb_id = sys.argv[1]
pdb_filename = masif_opts['raw_pdb_dir']+"/"+pdb_id+".pdb"

##### Protonate with reduce, if hydrogens included.
# - Always protonate as this is useful for charges. If necessary ignore hydrogens later.
protonated_file = masif_opts['raw_pdb_dir'][:-1]+"_protonized"+"/"+pdb_id+".pdb"
protonate(pdb_filename, protonated_file)
pdb_filename = protonated_file

