import os
import pyemu
import sys

temp_dir = os.path.join(os.getcwd(),"template")
sys.path.insert(0,temp_dir)

port = 5544
num_workers=10
from forward_run import ppw_worker as ppw_function

# Test if ppw_function was imported successfully
# try:
#     print(f"ppw_function type: {type(ppw_function)}")
# except ImportError as e:
#     print(f"Import failed: {e}")

pyemu.os_utils.start_workers(temp_dir,"pestpp-mou","mic_bbgo.pst",
                             num_workers=num_workers,
                             worker_root=".",
                             master_dir="master",
                             port=port,
                             ppw_function=ppw_function)