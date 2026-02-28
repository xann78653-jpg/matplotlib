from matplotlib import pyplot as plt
plt.figure(figsize=(20,8),dpi=80)
x=range(2,26,2)
y=[15,13,14.5,17,20,25,26,26,27,22,18,15]
plt.plot(x,y)
#plt.xticks(x)#强制显示出来所有的刻度
_xtick_labels=[i/2 for i in range(4,49)]
plt.xticks(_xtick_labels)#横轴显示以上面命名的变量为准,此时坐标与标签一一对应
plt.yticks(range(min(y),max(y)+1))
plt.savefig("./sig_size.png")
plt.show()