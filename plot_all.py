import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import pearsonr

def create_graph(x_input,y_input,graph_name,xlabel,ylabel):
    plt.close()
    figi, ax1 =plt.subplots(figsize=(6,6))
    scatter = ax1.scatter(x_input,y_input,marker = 'o')
    sns.set(style='darkgrid')
    ax1.grid(True)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_xlim(-5,105)
    ax1.set_ylim(-5,105)
    correlation_coefficient, _ = pearsonr(x_input, y_input)
    ax1.text(0.5, 0.9, f'R²= {correlation_coefficient:.4f}', transform=ax1.transAxes, ha='center', va='center')
    fit_params = np.polyfit(x_input, y_input, 1)
    fit_equation = f'f(x) = {fit_params[0]:.4f} * x + {fit_params[1]:.4f}'
    ax1.plot(x_input, np.polyval(fit_params, x_input), color='gray', label=fit_equation)
    ax1.legend()
    figi.savefig(graph_name+'.png')
    print(graph_name+'.png.complete')

print(111)


# x1 = [0, 0.045714285714285714, 0.2804232804232804, 0.2962962962962963, 0.4619289340101523, 0.8303571428571429]
# y1 = [0, 0.232142857, 0.432098765, 0.631868132, 1, 1]
# create_graph(x1,y1,'pro','formation rate(-)' ,'dead cell rate(-)')

