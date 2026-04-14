import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/andru/Documents/2026-I (S10)/Mineria de Datos/Trabajo Primer Corte/Cancer_Data.csv')
df.columns = df.columns.str.strip().str.replace('"', '')

df['diagnosis'] = df['diagnosis'].str.strip().str.replace('"', '')

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(data=df, x='area_mean', hue='diagnosis', kde=True, ax=axes[0], palette={'B':'blue', 'M':'red'}, bins=30)
axes[0].set_title('Histograma de area_mean')
sns.histplot(data=df, x='concavity_mean', hue='diagnosis', kde=True, ax=axes[1], palette={'B':'blue', 'M':'red'}, bins=30)
axes[1].set_title('Histograma de concavity_mean')
plt.tight_layout()
plt.savefig('C:/Users/andru/Documents/2026-I (S10)/Mineria de Datos/Trabajo Primer Corte/documento/hist_area_concavity.png')
plt.close()

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(data=df, x='smoothness_mean', hue='diagnosis', kde=True, ax=axes[0], palette={'B':'blue', 'M':'red'}, bins=30)
axes[0].set_title('Histograma de smoothness_mean')
sns.histplot(data=df, x='symmetry_mean', hue='diagnosis', kde=True, ax=axes[1], palette={'B':'blue', 'M':'red'}, bins=30)
axes[1].set_title('Histograma de symmetry_mean')
plt.tight_layout()
plt.savefig('C:/Users/andru/Documents/2026-I (S10)/Mineria de Datos/Trabajo Primer Corte/documento/hist_smooth_sym.png')
plt.close()
