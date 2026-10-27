# constante de gravitação universal (6.67 x 10^-11)
G = 6.67e-11

# entrada de dados do usuário
m1 = float(input("Digite a massa do primeiro corpo (em kg): "))
m2 = float(input("Digite a massa do segundo corpo (em kg): "))
d = float(input("Digite a distância entre os corpos (em metros): "))

# cálculo da força gravitacional (F = G * (m1 * m2) / d^2)
F = G * (m1 * m2) / (d ** 2)

# exibição do resultado em notação científica ou padrão
print("A força gravitacional entre os corpos é:", F, "N")
print("Formatado em notação científica:", round(F, 2), "N")
