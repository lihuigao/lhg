import matplotlib
print(matplotlib.__version__) #查看Matplotlib版本
import pandas as pd
print(pd.__version__) #查看pandas版本
import numpy as np
print(np.__version__) #查看numpy版本
import matplotlib.pyplot as plt 
plt.rcParams['font.sans-serif'] = ['SimHei']  #设置中文

plt.figure(figsize=(8,9),dpi = 100)  
sizes = [150,250,300,60]
labels = ['A','B','C','D'] 
colors = ['#8A977B','#F4D000','#FF7F00','#FF4040']
patches,l_text,p_text = plt.pie(sizes,labels = labels,
                      colors=colors,
                      autopct = '%3.2f%%', 
                      startangle = 90,
                      pctdistance = 0.8       
                      ) 

centre_circle = plt.Circle((0,0),0.50,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.legend(patches, labels,
          loc="center left",
          bbox_to_anchor=(1, 0.2, 1, 1),
          fontsize=20)


for t in l_text:
    t.set_size(30)
for t in p_text:
    t.set_size(17)

plt.title("饼图（甜甜圈图）- 增加白色块",fontsize = 20) 
plt.axis('equal')

plt.show()