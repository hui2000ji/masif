import os
import sys
from SBI.structure import PDB
from default_config.masif_opts import masif_opts

print(masif_opts["ligand"]["assembly_dir"])
if not os.path.exists(masif_opts["ligand"]["assembly_dir"]):
    os.mkdir(masif_opts["ligand"]["assembly_dir"])

def assemble(pdb_id):
    # Reads and builds the biological assembly of a structure
    print(os.path.join(masif_opts["raw_pdb_dir"][:-1]+"_protonized", "{}.pdb".format(pdb_id)))
    struct = PDB(
        os.path.join(masif_opts["raw_pdb_dir"][:-1]+"_protonized", "{}.pdb".format(pdb_id)), header=True
    )
    exit(0)
    try:
        struct_assembly = struct.apply_biomolecule_matrices()[0]
    except:
        return 0
    struct_assembly.write(
        os.path.join(masif_opts["ligand"]["assembly_dir"], "{}.pdb".format(pdb_id))
    )
    return 1

pdb_id = sys.argv[1]

res = assemble(pdb_id)
if res:
    print("Building assembly was successfull for {}".format(pdb_id))
else:
    print("Building assembly was not successfull for {}".format(pdb_id))
