from argparse import Namespace
from pathlib import Path
from multiprocessing import Pool

import numpy as np
import torch
from torch_geometric.data import Data


def make_protein_pyg(d, save_dir=Path('data_preparation/04c-precomputation_pyg')):
    data = dict()
    for f in [
        'p1_list_indices.npy',
        'p1_rho_wrt_center.npy',
        'p1_theta_wrt_center.npy',
        'p1_mask.npy',
        # 'p1_iface_labels.npy',
        'p1_input_feat.npy',
        'p1_X.npy',
        'p1_Y.npy',
        'p1_Z.npy',
        'p1_normals.npy',
    ]:
        arr = np.load(d / f, allow_pickle=True)
        if arr.dtype == np.float64:
            arr = arr.astype(np.float32)
        data[f[3:-4]] = arr
    data = Namespace(**data)

    pos = np.stack([data.X, data.Y, data.Z], axis=1)
    normal = data.normals

    x = data.input_feat[:, 0, [0, 2, 3, 4]]

    edge_index = np.array([[i, j] for i, l_ in enumerate(data.list_indices) for j in l_[1:]]).T
    
    mask = data.mask.astype(bool)
    mask[:, 0] = False  # discard self loops

    ddc = data.input_feat[:, :, 1]  # the ddc is actually an edge feature
    ddc_tgt = ddc[mask]
    ddc_src = ddc[:, 0][edge_index[0]]
    rho = data.rho_wrt_center[mask]
    theta = data.theta_wrt_center[mask]
    edge_attr = np.stack([rho, theta, ddc_src, ddc_tgt], axis=1)

    tdata = Data(x=torch.FloatTensor(x), edge_index=torch.LongTensor(edge_index), edge_attr = torch.FloatTensor(edge_attr), normal=torch.FloatTensor(normal), pos=torch.FloatTensor(pos), id=d.name)
    torch.save(tdata, save_dir / f'{d.name}.pt')


if __name__ == '__main__':
    root = Path('data_preparation/04a-precomputation_12A/precomputation/')
    dirs = list(root.iterdir())
    with Pool(4) as p:
        p.map(make_protein_pyg, dirs)