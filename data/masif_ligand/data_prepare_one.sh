# source /work/upcorreia/bin/load_masif_environment.sh
masif_root=$(git rev-parse --show-toplevel)
masif_source=$masif_root/source/
masif_matlab=$masif_root/source/matlab_libs/
export PYTHONPATH=$PYTHONPATH:$masif_source
export masif_matlab
PDB_ID=$(echo $1| cut -d"_" -f1)
CHAIN1=$(echo $1| cut -d"_" -f2)
CHAIN2=$(echo $1| cut -d"_" -f3)

module load nixpkgs/16.09
module load reduce/20180820
# conda activate my-rdkit-env
# ~/anaconda3/envs/my-rdkit-env/bin/python  $masif_source/data_preparation/00-pdb_download.py $1
# conda activate py2
# ~/anaconda3/envs/py2/bin/python $masif_source/data_preparation/00b-generate_assembly.py $1
# ~/anaconda3/envs/py2/bin/python $masif_source/data_preparation/00c-save_ligand_coords.py $1
conda activate my-rdkit-env
~/anaconda3/envs/my-rdkit-env/bin/python $masif_source/data_preparation/01-pdb_extract_and_triangulate.py $1 masif_ligand
~/anaconda3/envs/my-rdkit-env/bin/python $masif_source/data_preparation/04-masif_precompute.py masif_ligand $1
~/anaconda3/envs/my-rdkit-env/bin/python $masif_source/data_preparation/04c-make_protein_pyg.py $1
