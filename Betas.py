# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 22:32:11 2025

@author: isabe
"""


import matplotlib.pyplot as plt
import pandas as pd


file_pmma = "Beta PMMA.xlsx"
file_pmma2 = "Delta PMMA.xlsx"
file_cera = "Delta cera.xlsx"
file_nylon = "Delta nylon.xlsx"

df_pmma = pd.read_excel(file_pmma, sheet_name="Hoja1")
df_pmma2 = pd.read_excel(file_pmma2, sheet_name="Delta PMMA")
df_cera = pd.read_excel(file_cera, sheet_name="Delta cera")
df_nylon = pd.read_excel(file_nylon, sheet_name="Delta nylon")

energia_pmma = df_pmma["E(keV)"]
delta_pmma = df_pmma["Beta"]

energia_pmma2 = df_pmma2["E(keV)"]
delta_pmma2 = df_pmma2["Delta"]

energia_cera = df_cera["E(keV)"]
delta_cera = df_cera["Delta"]

energia_nylon = df_nylon["E(keV)"]
delta_nylon = df_nylon["Delta"]



#plt.figure(figsize=(8, 6))
#plt.plot(energia_pmma, delta_pmma, marker='o', linestyle='-', color='orange', label="δ vs Energía (PMMA)")
#plt.plot(energia_cera, delta_cera, marker='s', linestyle='-', color='blue', label="δ vs Energía (Cera)")
#plt.xlabel("Energía (keV)")
#plt.ylabel("δ (Índice de refracción)")
#plt.title("Comparación de δ en Nylon y Cera")
#plt.legend()
#plt.grid(True)
#plt.show()


#Log Cera y nylon

plt.figure(figsize=(8, 6))
plt.semilogy(energia_nylon, delta_nylon, marker='o', linestyle='-', color='green', label="β vs Energía (Nylon)")
plt.semilogy(energia_cera, delta_cera, marker='s', linestyle='-', color='blue', label="β vs Energía (Cera)")
plt.xlabel("Energía (keV)")
plt.ylabel("β (Coeficiente de atenuación)")
plt.title("Comparison of δ and β of PMMA")
plt.legend()
plt.grid(True, which="both")
plt.show()


#Log Nylon y PMMA
plt.figure(figsize=(8, 6))
plt.semilogy(energia_nylon, delta_pmma, marker='o', linestyle='-', color='green', label=" β (PMMA)")
plt.semilogy(energia_pmma, delta_pmma2, marker='s', linestyle='-', color='red', label="δ (PMMA)")
plt.xlabel("Energy(keV)")
plt.ylabel(" δ and β values")
plt.title("Comparison of δ and β of PMMA")
plt.legend()
plt.grid(True, which="both")
plt.show()

#Log Cera y PMMA
plt.figure(figsize=(8, 6))
plt.semilogy(energia_cera, delta_cera, marker='o', linestyle='-', color='blue', label="β vs Energía (Cera)")
plt.semilogy(energia_pmma, delta_pmma, marker='s', linestyle='-', color='red', label="β vs Energía (PMMA)")
plt.xlabel("Energía (keV)")
plt.ylabel("β (Coeficiente de atenuación)")
plt.title("Comparación Logarítmica de β en Cera y PMMA")
plt.legend()
plt.grid(True, which="both")
plt.show()


# Cociente
delta_ratio = delta_cera / delta_pmma2
delta_ratio1 = delta_cera / delta_nylon
delta_ratio2 = delta_nylon / delta_pmma2

plt.figure(figsize=(8, 6))
plt.plot(energia_pmma, delta_ratio, marker='d', linestyle='-', color='red', label="Cociente PMMA/Cera")
plt.xlabel("Energía (keV)")
plt.ylabel("Cociente β (PMMA/Cera)")
plt.title("Ratio between β de PMMA y Cera")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
plt.plot(energia_pmma, delta_ratio1, marker='d', linestyle='-', color='green')
plt.xlabel("Energy (keV)")
plt.ylabel("δ (Nylon/Wax)")
plt.title("Ratio between δ of Nylon and Wax")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(energia_pmma, delta_ratio2, marker='d', linestyle='-', color='blue')
plt.xlabel("Energy (keV)")
plt.ylabel("δ (PMMA/Nylon)")
plt.title("Ratio between δ of Nylon and PMMA")
plt.legend()
plt.grid(True)
plt.show()