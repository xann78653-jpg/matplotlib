from matplotlib import pyplot as plt
import matplotlib
plt.figure(figsize=(20,8),dpi=80)
matplotlib.rc("font",family="MicroSoft YaHei",size=10,weight="normal")
interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]
bar_width=[w/10 for w in width]
_x=list(range(len(interval)))
plt.bar(_x,quantity,width=bar_width)
plt.show()