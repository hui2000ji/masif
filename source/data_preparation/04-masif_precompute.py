import sys
import time
import os
import numpy as np
from IPython.core.debugger import set_trace
import warnings 
with warnings.catch_warnings(): 
    warnings.filterwarnings("ignore",category=FutureWarning)

# Configuration imports. Config should be in run_args.py
from default_config.masif_opts import masif_opts

np.random.seed(0)

# Load training data (From many files)
from masif_modules.read_data_from_surface import read_data_from_surface, compute_shape_complementarity

print(sys.argv[2])

if len(sys.argv) <= 1:
    print("Usage: {config} "+sys.argv[0]+" {masif_ppi_search | masif_site} PDBID_A")
    print("A or AB are the chains to include in this surface.")
    sys.exit(1)

masif_app = sys.argv[1]

if masif_app == 'masif_ppi_search': 
    params = masif_opts['ppi_search']
elif masif_app == 'masif_site':
    params = masif_opts['site']
    params['ply_chain_dir'] = masif_opts['ply_chain_dir']
elif masif_app == 'masif_ligand':
    params = masif_opts['ligand']

ppi_pair_id = sys.argv[2]

total_shapes = 0
total_ppi_pairs = 0
np.random.seed(0)
print('Reading data from input ply surface files.')

all_list_desc = []
all_list_coords = []
all_list_shape_idx = []
all_list_names = []
idx_positives = []

my_precomp_dir = params['masif_precomputation_dir']+ppi_pair_id+'/'
if not os.path.exists(my_precomp_dir):
    os.makedirs(my_precomp_dir)



# Save data only if everything went well. 
np.save(my_precomp_dir+'rho_wrt_center', rho)
np.save(my_precomp_dir+'theta_wrt_center', theta)
np.save(my_precomp_dir+'input_feat', input_feat)
np.save(my_precomp_dir+'normals', normals)
np.save(my_precomp_dir+'mask', mask)
np.save(my_precomp_dir+'list_indices', neigh_indices)
np.save(my_precomp_dir+'iface_labels', iface_labels)
# Save x, y, z
np.save(my_precomp_dir+'X.npy', verts[:,0])
np.save(my_precomp_dir+'Y.npy', verts[:,1])
np.save(my_precomp_dir+'Z.npy', verts[:,2])

# global: id, x_names
# node: x, pos, normals
# edge: rho, theta, dx