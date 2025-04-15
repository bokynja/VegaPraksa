import pandas as pd
import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\bojana.boskovic\Downloads\Internship-20240613T152423Z-001\Internship\Python deo\orders.csv') 

df['Sales_log'] = np.log1p(df['Sales']) 

sns.displot(df, x='Sales_log', hue='Region', kind='kde')
plt.title('Distributon by Region (log-transf)')
plt.show()

# ANOVA test -da proveri da li postoji bilo kakva razlika
groups = [group['Sales_log'] for name, group in df.groupby('Region')]
anova_stat, anova_p = f_oneway(*groups)
print(f"\nANOVA p-vrednost: {anova_p:.4f}")

if anova_p < 0.05:
    print("Postoji statistički značajna razlika između barem dva regiona.")

    # Tukey HSD post hoc test
    tukey = pairwise_tukeyhsd(endog=df['Sales_log'],
                              groups=df['Region'],
                              alpha=0.05)
    print("\nRezultati Tukey HSD testa:\n")
    print(tukey)

    tukey.plot_simultaneous()
    plt.title('Tukey HSD - razlike između regiona')
    plt.show()
else:
    print("Nema statistički značajne razlike između regiona.")
