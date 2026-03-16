from opencosmorspy import CosmoRS  # 导入 openCOSMO-RS 库

# 设定.cosmo 文件路径
orcacosmo_file = "E:\\Gaussian\\CH3CH2OH\\EtOH.cosmo"

# 创建 CosmoRS 对象
crs = CosmoRS()

# 读取 .cosmo 文件
mol = crs.read_cosmo_file(orcacosmo_file)

# 计算 COSMO-RS 描述符
desc = crs.calculate_descriptors(mol)

# 输出计算结果
print("Hildebrand 溶解度参数 δ：", desc["delta"])
