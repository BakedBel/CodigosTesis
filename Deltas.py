# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:48:16 2025

@author: isabe
"""

import matplotlib.pyplot as plt
import pandas as pd


file_pmma = "Delta PMMA.xlsx"
file_cera = "Delta cera.xlsx"
file_nylon = "Delta nylon.xlsx"

df_pmma = pd.read_excel(file_pmma, sheet_name="Delta PMMA")
df_cera = pd.read_excel(file_cera, sheet_name="Delta cera")
df_nylon = pd.read_excel(file_nylon, sheet_name="Delta nylon")

energia_pmma = df_pmma["E(keV)"]
delta_pmma = df_pmma["Delta"]

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
plt.semilogy(energia_nylon, delta_nylon, marker='o', linestyle='-', color='green', label="δ vs Energía (Nylon)")
plt.semilogy(energia_cera, delta_cera, marker='s', linestyle='-', color='blue', label="δ vs Energía (Cera)")
plt.xlabel("Energía (keV)")
plt.ylabel("δ (Índice de refracción)")
plt.title("Comparación Logarítmica de δ en Nylon y Cera")
plt.legend()
plt.grid(True, which="both")
plt.show()


#Log Nylon y PMMA
plt.figure(figsize=(8, 6))
plt.semilogy(energia_nylon, delta_nylon, marker='o', linestyle='-', color='green', label="δ vs Energía (Nylon)")
plt.semilogy(energia_pmma, delta_pmma, marker='s', linestyle='-', color='red', label="δ vs Energía (PMMA)")
plt.xlabel("Energía (keV)")
plt.ylabel("δ (Índice de refracción)")
plt.title("Comparación Logarítmica de δ en Nylon y PMMA")
plt.legend()
plt.grid(True, which="both")
plt.show()

#Log Cera y PMMA
plt.figure(figsize=(8, 6))
plt.semilogy(energia_cera, delta_cera, marker='o', linestyle='-', color='blue', label="δ vs Energía (Cera)")
plt.semilogy(energia_pmma, delta_pmma, marker='s', linestyle='-', color='red', label="δ vs Energía (PMMA)")
plt.xlabel("Energía (keV)")
plt.ylabel("δ (Índice de refracción)")
plt.title("Comparación Logarítmica de δ en Cera y PMMA")
plt.legend()
plt.grid(True, which="both")
plt.show()


# Cociente
delta_ratio = delta_pmma / delta_nylon
delta_ratio1 = delta_cera / delta_pmma
delta_ratio2 = delta_cera / delta_nylon

plt.figure(figsize=(8, 6))
plt.plot(energia_pmma, delta_ratio, marker='d', linestyle='-', color='red', label="Cociente PMMA/Cera")
plt.xlabel("Energía (keV)")
plt.ylabel("Cociente δ (PMMA/nylon)")
plt.title("Cociente entre δ de PMMA y nylon")
plt.legend()
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
plt.plot(energia_pmma, delta_ratio1, marker='d', linestyle='-', color='green', label="Cociente Cera/PMMA")
plt.xlabel("Energía (keV)")
plt.ylabel("Cociente δ ")
plt.title("Cociente entre δ de Cera y PMMA")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(energia_pmma, delta_ratio2, marker='d', linestyle='-', color='blue', label="Cociente Cera/Nylon")
plt.xlabel("Energía (keV)")
plt.ylabel("Cociente δ")
plt.title("Cociente entre δ de Cera y Nylon")
plt.legend()
plt.grid(True)
plt.show()