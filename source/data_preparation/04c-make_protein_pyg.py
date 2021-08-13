from argparse import Namespace
from pathlib import Path
from multiprocessing import Pool
import sys
import numpy as np
import torch
from torch_geometric.data import Data
from default_config.masif_opts import masif_opts
from masif_modules.read_data_from_surface import read_data_from_surface


def make_protein_pyg(prot_id, save_dir=Path(masif_opts['ligand']['masif_pyg_dir']), exists_ok=True):
    if (save_dir / f'{prot_id}.pt').exists() and exists_ok:
        return
    # Read directly from the ply file.
    ply_file = masif_opts['ply_file_template'].format(prot_id)
        
    # Compute shape complementarity between the two proteins. 
    input_feat, rho, theta, mask, list_indices, _, pos, normal = read_data_from_surface(ply_file, masif_opts['ligand'])

    x = input_feat[:, 0, [0, 2, 3, 4]]

    edge_index = np.array([[i, j] for i, l_ in enumerate(list_indices) for j in l_[1:]]).T
    
    mask = mask.astype(bool)
    mask[:, 0] = False  # discard self loops

    ddc = input_feat[:, :, 1]  # the ddc is actually an edge feature
    ddc_tgt = ddc[mask]
    ddc_src = ddc[:, 0][edge_index[0]]
    rho = rho[mask]
    theta = theta[mask]
    edge_attr = np.stack([rho, theta, ddc_src, ddc_tgt], axis=1)

    tdata = Data(x=torch.FloatTensor(x), edge_index=torch.LongTensor(edge_index), edge_attr=torch.FloatTensor(edge_attr), normal=torch.FloatTensor(normal), pos=torch.FloatTensor(pos), id=prot_id)
    torch.save(tdata, save_dir / f'{prot_id}.pt')


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        root = Path(masif_opts['ligand']['ply_chain_dir'])
        files = root.glob('*.ply')
        stems = [f.stem for f in files]
        with Pool(4) as p:
            p.map(make_protein_pyg, stems)
    else:
        make_protein_pyg(sys.argv[1])
