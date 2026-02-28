import matplotlib
from matplotlib import pyplot as plt
import numpy as np
matplotlib.rc("font", family="MicroSoft YaHei", size="20", weight="normal")
plt.figure(figsize=(20,10),dpi=80)
x_1=range(1,29)
x_2=range(51,78)
y_1= [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,19,21,22,22]
y_2 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,22,20,22,15,11,5,13,17,19,13,12]
y_3= [13,15,12,21,13,21,22,16,13,17,5,6,22,15,24,13,18,21,13,14,10,13,5,13,12,11,21,12]
y_4=[11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,19,21,22]
_x=list(x_1)+list(x_2)
_xtick_labels=["3月{}日".format(i) for i in x_1 ]
_xtick_labels+=["10月{}日".format(i-50) for i in x_2 ]
plt.xticks(_x[::3],_xtick_labels[::3],rotation=45)
plt.plot(x_1,y_1,label="3月气温")
plt.plot(x_2,y_2,label="10月气温")
plt.scatter(x_1,y_3,color="red",label="3月销量")
plt.scatter(x_2,y_4,color="blue",label="10月销量")
plt.xlabel("日期")
plt.ylabel("气温℃/销量",rotation=90)
plt.legend(loc="upper right")
plt.grid(alpha=0.4)
plt.savefig("./sig_size.png")
plt.show()