import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc("font",family="MicroSoft YaHei",weight="normal",size=10)
plt.figure(figsize=(20,8),dpi=80)
a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,3124,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,382]
bar_width = 0.2
x_14=list(range(len(a)))
x_15=[i+bar_width for i in x_14]
x_16=[i+bar_width for i in x_15]
plt.bar (x_14,b_14,label="9.14",color="red",width=bar_width)
plt.bar (x_16,b_16,label="9.16",color="orange",width=bar_width)
plt.bar (x_15,b_15,label="9.15",color="blue",width=bar_width)
plt.xticks(x_15,a)
plt.legend(loc="upper right")
plt.show()
