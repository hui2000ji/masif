masif_root=$(git rev-parse --show-toplevel)
masif_source=$masif_root/source/
masif_matlab=$masif_root/source/matlab_libs/
export PYTHONPATH=$PYTHONPATH:$masif_source
export masif_matlab
PDB_ID=$(echo $1| cut -d"_" -f1)
CHAIN1=$(echo $1| cut -d"_" -f2)
CHAIN2=$(echo $1| cut -d"_" -f3)
python $masif_source/data_preparation/01-pdb_extract_and_triangulate.py $PDB_ID\_$CHAIN1
python $masif_source/data_preparation/01-pdb_extract_and_triangulate.py $PDB_ID\_$CHAIN2
python $masif_source/data_preparation/02-compute_matlab_matrix.py $1
python $masif_source/data_preparation/03-compute_coords.py $1
python $masif_source/data_preparation/03b-convert_mat2npy.py $1
python $masif_source/data_preparation/04-masif_precompute.py masif_ppi_search $1
