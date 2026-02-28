from matplotlib import pyplot as plt
import random
import matplotlib
#font ={'family':"Microsoft YaHei",'weight':'normal','size':14}
#matplotlib.rc("font", **font)
#matplotlib.rc("font",family='MicroSoft YaHei',weight="bold",size=14)
from matplotlib import font_manager

my_font=font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")#这里有问题,弄了好久,QUIT
x=range(0,120)
y=[random.randint(20,35) for i in range(120)]
plt.figure(figsize=(20,8), dpi=80)
plt.plot(x,y)
_xtick_labels =["10点{}分".format(i) for i in range(60)]
_xtick_labels+=["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45,fontproperties=my_font)
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位(℃)",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化",fontproperties=my_font)
plt.show()
#事实证明啊,有多种方法可以让pycharm 编译器中的中文显示出来,从windows里面去找是一种非常蠢的方法.
#一,找到默认字体具体位置代码.二,From matplotlib import font_manager......and import my_font
#三,13-15行每一行最后都要加上fontproperties=my_font
