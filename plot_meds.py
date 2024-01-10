import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plot_all import create_graph 

meds_c = []
with open('sk25_etapro_FITC_c_1227_meds_means_vars.txt') as f:
    for i in f.readlines():
        meds_c.append(float(i.split(',')[0]))
meds_5 = []
with open('sk25_eta_FITC_5_meds_means_vars.txt') as f:
    for i in f.readlines():
        meds_5.append(float(i.split(',')[0]))
meds_6 = []
with open('sk25_eta_FITC_7_meds_means_vars.txt') as f:
    for i in f.readlines():
        meds_6.append(float(i.split(',')[0]))
meds_7 = []
with open('sk25_eta_FITC_8_meds_means_vars.txt') as f:
    for i in f.readlines():
        meds_7.append(float(i.split(',')[0]))
meds_8 = []
with open('sk25_eta_FITC_9_meds_means_vars.txt') as f:
    for i in f.readlines():
        meds_8.append(float(i.split(',')[0]))
meds_10 = []
with open('sk25_eta_FITC_10_meds_means_vars.txt') as f:
    for i in f.readlines():
        meds_10.append(float(i.split(',')[0]))

data1,data2,data3,data4,data5,data6= meds_c,meds_5,meds_6,meds_7,meds_8,meds_10
lower_percentile_95 = np.percentile(data1, 5)
prob_below_lower_percentile_95 = [np.mean(data < lower_percentile_95) for data in [data2, data3, data4, data5, data6]]
print(f"下限95パーセンタイルを下回るサンプルの発生確率: {prob_below_lower_percentile_95}")

def multiple_by_100(data):
    return[y * 100 for y in data]
x = [0, 5, 6, 7, 8, 10]
y = [5] + multiple_by_100(prob_below_lower_percentile_95)
fig, ax = plt.subplots()

ax.plot(x, y, marker = 'o', linestyle = '-')
ax.grid()
ax.set_xlabel('etanol conc.(%)')
ax.set_ylabel('formation rate(%)')
fig.savefig('fig_eta_95%.png')
plt.close(fig)
plt.clf()
plt.close()

x1 = [5] + multiple_by_100(prob_below_lower_percentile_95)
y1 = multiple_by_100([0, 0.232142857, 0.432098765, 0.631868132, 1, 1])
create_graph(x1,y1,'eta1','formation rate(-)' ,'dead cell rate(-)')
