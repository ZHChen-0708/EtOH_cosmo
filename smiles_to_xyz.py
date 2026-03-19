from rdkit import Chem
from rdkit.Chem import AllChem

def smiles_to_xyz(smiles, atom_name, xyz_filename):
    """
    由分子 SMILES 式生成 xyz 文件
    """
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        raise ValueError("Invalid SMILES string.")

    # 添加氢原子
    mol = Chem.AddHs(mol)

    # 生成 3D 坐标
    success = AllChem.EmbedMolecule(mol, randomSeed=42)
    if success != 0:
        raise ValueError("Could not generate 3D coordinates.")

    # UFF 优化
    AllChem.UFFOptimizeMolecule(mol)

    # 原子数
    num_atoms = mol.GetNumAtoms()

    # 写 xyz 文件
    with open(xyz_filename, 'w', encoding='utf-8') as xyz_file:
        xyz_file.write(f"{num_atoms}\n")
        xyz_file.write(f"{atom_name} {atom_name}.ff\n")

        conf = mol.GetConformer()
        for atom in mol.GetAtoms():
            idx = atom.GetIdx()
            pos = conf.GetAtomPosition(idx)
            xyz_file.write(
                f"{atom.GetSymbol():<2} {pos.x:>12.6f} {pos.y:>12.6f} {pos.z:>12.6f}\n"
            )

if __name__ == "__main__":
    print("=== SMILES 转 XYZ 程序 ===")

    smiles_expression = input("请输入分子的 SMILES 表达式：").strip()
    atom_name = input("请输入分子名称：").strip()
    xyz_filename = input("请输入输出 xyz 文件名（例如 water.xyz）：").strip()

    try:
        smiles_to_xyz(smiles_expression, atom_name, xyz_filename)
        print(f"生成成功，xyz 文件已保存为：{xyz_filename}")
    except Exception as e:
        print(f"生成失败：{e}")