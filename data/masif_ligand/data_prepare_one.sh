# source /work/upcorreia/bin/load_masif_environment.sh
masif_root=$(git rev-parse --show-toplevel)
masif_source=$masif_root/source/
cd $masif_source
conda init
conda activate my-rdkit-env
conda deactivate
module load nixpkgs/16.09
module load reduce/20180820
# conda activate my-rdkit-env
# ~/anaconda3/envs/my-rdkit-env/bin/python  $masif_source/data_preparation/00-pdb_download.py $1
# conda activate py2
# ~/anaconda3/envs/py2/bin/python $masif_source/data_preparation/00b-generate_assembly.py $1
# ~/anaconda3/envs/py2/bin/python $masif_source/data_preparation/00c-save_ligand_coords.py $1
conda activate my-rdkit-env
~/anaconda3/envs/my-rdkit-env/bin/python -m data_preparation.01-pdb_extract_and_triangulate $1 masif_ligand
~/anaconda3/envs/my-rdkit-env/bin/python -m data_preparation.04c-make_protein_pyg $1
