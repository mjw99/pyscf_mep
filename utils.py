from openbabel import pybel
from openbabel import openbabel as ob

from pyscf import gto

def SMILES_to_Mole(SMILES):
    mol = pybel.readstring('smi', SMILES)
    mol.addh()
    ob.OBBuilder().Build(mol.OBMol)

    steps = 250
    ff = ob.OBForceField.FindForceField("mmff94")
    ff.Setup(mol.OBMol)

    ff.SetVDWCutOff(10.0)
    ff.EnableCutOff(True)
    ff.SetElectrostaticCutOff(20.0)
    ff.SetUpdateFrequency(10)

    ff.ConjugateGradients(steps, 1.0e-4)
    ff.FastRotorSearch(False)
    ff.ConjugateGradients(steps, 1.0e-6)

    ff.GetCoordinates(mol.OBMol)

    # Extract out just atom coordinates to pass over to PySCF
    finalAtoms = []

    for atom in mol.atoms:
        finalAtoms.append("{0} {1} {2} {3}".format(ob.GetSymbol(
            atom.atomicnum), atom.vector.GetX(), atom.vector.GetY(), atom.vector.GetZ()))

    qmMol = gto.Mole(atom=finalAtoms, units="Angstrom")

    return qmMol
