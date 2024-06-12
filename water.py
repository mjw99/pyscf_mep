from pyscf import __config__
# Default of 3.0 is too small for 6-31G*
# Note, this *must* be run before importing cubge
setattr(__config__, 'cubegen_box_margin', 4.0)

from pyscf import dft
from pyscf.geomopt import berny_solver
from pyscf.tools import cubegen

from utils import *

mol = SMILES_to_Mole("O")

# https://pyscf.org/user/gto.html
mol.basis="6-31G*"
mol.verbose = 5 
mol.build()

# https://pyscf.org/user/dft.html
method = dft.RKS(mol)
method.xc = 'b3lypg'
method.scf()

# https://pyscf.org/user/geomopt.html
opt_mol = berny_solver.optimize(method)

_ = cubegen.density(opt_mol, 'water_den.cube', method.make_rdm1(), resolution=(1/6))
_ = cubegen.mep(opt_mol, 'water_pot.cube', method.make_rdm1(), resolution=(1/6))

