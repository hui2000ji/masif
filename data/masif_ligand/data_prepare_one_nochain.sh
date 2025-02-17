# source /work/upcorreia/bin/load_masif_environment.sh
masif_root=$(git rev-parse --show-toplevel)
masif_source=$masif_root/source/
masif_matlab=$masif_root/source/matlab_libs/
export PYTHONPATH=$PYTHONPATH:$masif_source
export masif_matlab

module load nixpkgs/16.09
module load reduce/20180820
~/anaconda3/envs/my-rdkit-env/bin/python  $masif_source/data_preparation/00-pdb_download_nochain.py $1
~/anaconda3/envs/py2/bin/python $masif_source/data_preparation/00b-generate_assembly_nochain.py $1

# export APBS_BIN=/home/hycai/scratch/202107Docking/APBS-1.5-linux64/bin/apbs
# export MULTIVALUE_BIN=/home/hycai/scratch/202107Docking/APBS-1.5-linux64/share/apbs/tools/bin/multivalue
# export PDB2PQR_BIN=/home/hycai/scratch/202107Docking/pdb2pqr-linux-bin64-2.1.1/pdb2pqr
# export MSMS_BIN=/home/hycai/anaconda3/envs/my-rdkit-env/bin/msms
# export PDB2XYZRN=/home/hycai/anaconda3/envs/my-rdkit-env/bin/pdb_to_xyzrn
# ~/anaconda3/envs/my-rdkit-env/bin/python $masif_source/data_preparation/01-pdb_extract_and_triangulate_nochain.py $1 masif_ligand

# ~/anaconda3/envs/my-rdkit-env/bin/python $masif_source/data_preparation/04-masif_precompute_nochain.py masif_ligand $1
