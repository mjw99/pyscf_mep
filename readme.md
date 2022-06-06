Introduction
============
An example of how to calculate a MEP using PySCF, using Ubuntu and Conda.

QuickStart
==========
1) Clone the repo. Do this outside of conda since it interferes with git.

```
git clone https://github.com/mjw99/pyscf_mep.git
cd pyscf_mep
```	

2) Create a conda environment and install needed packages (you only need to do this once)
```

# Create and activate environment
conda create -y --name pyscf_mep python=3.8
source activate pyscf_mep

# PySCF: QM package
conda install -y -c conda-forge pyscf==2.0.1

# Optimiser
pip install pyberny==0.6.3

# Visualization
conda install -y -c conda-forge nglview

# SMILES to 3D
conda install -y -c openbabel
	
# jupyter-notebook related
conda install -y -c conda-forge jupyter
conda install -y -c conda-forge ipykernel
	
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
