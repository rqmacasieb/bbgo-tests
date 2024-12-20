import os
import pandas as pd
import numpy as np
import benchmark_functions as bf

def michalewicz(x):
    func = bf.Michalewicz(n_dimensions=10)
    sim = func(x)
    return sim

def helper(pvals=None):
    if pvals is None:
        pvals = pd.read_csv("dv.dat").values.reshape(-1).tolist()
    sim = michalewicz(pvals)
    with open('output.dat','w') as f:
        f.write('obsnme,obsval\n')
        f.write('func,'+str(sim)+'\n')
        f.write('func_sd,0\n')
        f.write('EI,0\n')
    return sim

def ppw_worker(pst_name,host,port):
    import pyemu
    ppw = pyemu.os_utils.PyPestWorker(pst_name,host,port,verbose=False)
    pvals = ppw.get_parameters()
    if pvals is None:
        return
    pvals.sort_index(inplace=True)

    while True:

        sim = helper(pvals=pvals.values)
        ppw.send_observations(np.array([sim]))
        pvals = ppw.get_parameters()
        if pvals is None:
            break
        pvals.sort_index(inplace=True)


if __name__ == "__main__":
    helper()
