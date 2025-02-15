from pathlib import Path

from Bio.PDB.Polypeptide import PPBuilder
from Bio.PDB import PDBParser

import pepdesMD
from pepdesMD import Geometry


def compare_residues(r1, r2) -> bool:
    if not r1 == r2:
        return False
    if not len(list(r1.get_atoms())) == len(list(r2.get_atoms())):
        return False

    result = True
    for a1, a2 in zip(r1, r2):
        result = result and (abs(a1.coord - a2.coord) < 0.001).all()

    return result


def compare_to_reference(structure, ref_file) -> bool:
    parser = PDBParser()
    ref_structure = parser.get_structure("test", str(Path("tests", "pdbs", ref_file)))

    res = list(list(structure[0])[0])
    ref_res = list(list(ref_structure[0])[0])
    if not len(res) == len(ref_res):
        return False

    result = True
    for r1, r2 in zip(res, ref_res):
        result = result and compare_residues(r1, r2)

    return result


def test_add_residue():
    """
    Build a peptide containing all 20 amino acids
    """
    structure = pepdesMD.initialize_res("A")
    for aa in "CDEFGHIKLMNPQRSTVWY":
        pepdesMD.add_residue(structure, aa)

    # extract peptide from structure and compare to expected
    ppb = PPBuilder()
    pp = next(iter(ppb.build_peptides(structure)))
    assert pp.get_sequence() == "ACDEFGHIKLMNPQRSTVWY"

    assert compare_to_reference(structure, "extended.pdb")


def test_add_residue2():
    """
    Build a helix containing all 20 amino acids, with slowly varying backbone angles
    """
    phi = -60
    psi_im1 = -40
    geo = Geometry.geometry("A")
    geo.phi = phi
    geo.psi_im1 = psi_im1
    structure = pepdesMD.initialize_res(geo)

    for aa in "CDEFGHIKLMNPQRSTVWY":
        phi += 1
        psi_im1 -= 1
        geo = Geometry.geometry(aa)
        geo.phi = phi
        geo.psi_im1 = psi_im1
        pepdesMD.add_residue(structure, geo)

    assert compare_to_reference(structure, "helix.pdb")


def test_make_structure_from_geos():
    """Build a helix containing all 20 amino acids from list of geometries.
    The structure should be identical to `extended.pdb`
    """
    geos = [Geometry.geometry(aa) for aa in "ACDEFGHIKLMNPQRSTVWY"]
    structure = pepdesMD.make_structure_from_geos(geos)
    assert compare_to_reference(structure, "extended.pdb")


def test_make_extended_structure():
    """
    Build a peptide containing all 20 amino acids in extended conformation.
    The structure should be identical to `extended.pdb`
    """
    structure = pepdesMD.make_extended_structure("ACDEFGHIKLMNPQRSTVWY")
    assert compare_to_reference(structure, "extended.pdb")

    # test unit tests by comparing structures that don't match
    structure = pepdesMD.make_extended_structure("ACDEFGHIKLMNPQRSTVW")
    assert not compare_to_reference(structure, "extended.pdb")
    structure = pepdesMD.make_extended_structure("ACDEFGHIKLMNPQRSTVWW")
    assert not compare_to_reference(structure, "extended.pdb")


def test_make_structure_from_geos2():
    """
    Build a peptide containing all 20 amino acids from list of geometries.
    The structure should be identical to `extended.pdb`
    """
    geos = [Geometry.geometry(aa) for aa in "ACDEFGHIKLMNPQRSTVWY"]
    structure = pepdesMD.make_structure_from_geos(geos)
    assert compare_to_reference(structure, "extended.pdb")


def test_make_structure():
    """
    Build a helix containing all 20 amino acids, with slowly varying
    backbone angles, using make_structure().
    The resulting structure should be identical to `helix.pdb`
    """
    phi_list = []
    psi_im1_list = []

    for i in range(1, 20):
        phi_list.append(-60 + i)
        psi_im1_list.append(-40 - i)
    structure = pepdesMD.make_structure(
        "ACDEFGHIKLMNPQRSTVWY", phi_list, psi_im1_list
    )
    assert compare_to_reference(structure, "helix.pdb")


def test_make_structure2():
    """
    Build a helix containing all 20 amino acids, with slowly varying
    backbone angles, using make_structure(). Now we're changing omega also.
    The first half of the resulting structure should be identical to
    `helix.pdb`, while the second half should be slightly different.
    """
    phi_list = []
    psi_im1_list = []
    omega_list = []

    for i in range(1, 20):
        phi_list.append(-60 + i)
        psi_im1_list.append(-40 - i)
        omega_list.append(180)

    for i in range(9, 19):
        omega_list[i] = -178

    structure = pepdesMD.make_structure(
        "ACDEFGHIKLMNPQRSTVWY", phi_list, psi_im1_list, omega_list
    )
    assert compare_to_reference(structure, "helix2.pdb")


def test_add_terminal_OXT():
    """
    Build a peptide with terminal OXT
    """
    structure = pepdesMD.initialize_res("A")
    for aa in "CDEFGHIKLMNPQRSTVWY":
        pepdesMD.add_residue(structure, aa)
    pepdesMD.add_terminal_OXT(structure)
    assert compare_to_reference(structure, "extended_OXT.pdb")
    # check that presence of OXT is tested
    assert not compare_to_reference(structure, "extended.pdb")
