# ==================================================================
# PLOTTWIST - DEV
# ==================================================================

import os
import sys
import maya.cmds as cmds

# Path where you Plot Twist development virtual environment package are located.
# For example: D:\dev\plottwist\plottwist\dev\win\plottwist_dev\Lib\site-packages'
dev_path = r'' 
paths_to_add = [dev_path]
for f in os.listdir(dev_path):
    if f.endswith('.egg-link'): 
        file_path = os.path.join(dev_path, f)
        with open(file_path) as f:
            new_path = f.readline().rstrip()
            if os.path.isdir(new_path):
                paths_to_add.append(new_path)

for p in paths_to_add:
    if os.path.isdir(p) and p not in sys.path:
        sys.path.append(p)
        
# =============================================================

import artellapipe
import plottwist.loader
plottwist.loader.init(True, dev=True)


# Example of how to launch a tool
# artellapipe.ToolsMgr().run_tool('artellapipe-tools-artellamanager', do_reload=True, debug=False)