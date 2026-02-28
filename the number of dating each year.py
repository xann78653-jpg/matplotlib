import matplotlib
from matplotlib import pyplot as plt
matplotlib.rc("font",family="MicroSoft YaHei",weight="normal",size=14)
x=range(11,31)
y_1=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2=[0,3,1,2,2,5,2,3,3,4,3,5,2,1,4,3,2,1,5,3]
plt.figure(figsize=(20,8),dpi=80)
plt.plot(x,y_1,label="自己",color="m",linestyle=":")
plt.plot(x,y_2,label="同桌",color="c",linestyle="--")
#r红色,g绿色,b蓝色,w白色,c青色,m洋红,k黑色
#-实线--虚线,破折线,-.点划线,:点虚线,虚线,''留空或空格,无线条
_xtick_labels=["{}岁".format (i) for i in x]
plt.xticks(x,_xtick_labels,rotation=45)
plt.yticks(range(min(y_1),max(y_1)+1))
plt.xlabel("岁数")
plt.ylabel("个数")
plt.grid(alpha=0.4)
plt.legend()
plt.savefig("./sig_size.png")
plt.show()