Introduction
============
An example of how to calculate a MEP using [PySCF](https://arxiv.org/abs/2002.12531), using Ubuntu and [Mamba](https://mamba.readthedocs.io/en/latest/installation.html).

QuickStart
==========
1) Clone the repo. Do this outside of mamba since it interferes with git.

```
git clone https://github.com/mjw99/pyscf_mep.git
cd pyscf_mep
```	

2) Create a mamba environment and install needed packages (you only need to do this once)
```

# Create and activate environment
mamba create -y --name pyscf_mep python=3.8
mamba activate pyscf_mep

# PySCF: QM package
mamba install -y -c conda-forge pyscf==2.0.1

# Optimiser
pip install pyberny==0.6.3

# Visualization
mamba install -y -c conda-forge nglview

# SMILES to 3D
mamba install -y -c conda-forge openbabel
	
# jupyter-notebook related
mamba install -y -c conda-forge jupyter
mamba install -y -c conda-forge ipykernel

# https://github.com/nglviewer/nglview/issues/1032#issue-1343627010
mamba install "ipywidgets=7" -c conda-forge
	
# Create notebook which will use the deps in the conda environment
python -m ipykernel install --user --name pyscf_mep --display-name "Python (pyscf_mep)"
```
3) Start and execute the notebook
```
jupyter-notebook water_MEP.ipynb
```


Extra
==========

4) View with VMD
```
vmd -e water.vmd
```

5) View with JMOL
```
jmol water_den.cube
<from internal console>
isosurface "water_den.cube" map "water_pot.cube"
```
