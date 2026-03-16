from opencosmorspy.cosmors import COSMORS

# cosmo 文件路径
cosmo_file = r"E:\Gaussian\CH3CH2OH\EtOH.cosmo"

# 创建 COSMO-RS 对象
crs = COSMORS()

# 读取 cosmo 文件
mol = crs.read_cosmo_file(cosmo_file)

# 计算 COSMO-RS 描述符
desc = crs.calculate_descriptors(mol)

# 输出结果
print("Hildebrand 溶解度参数 δ =", desc["delta"])