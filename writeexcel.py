import pandas as pd
list=['三打白骨精','刘姥姥逛大观园','面见如来','初见林黛玉']
p=pd.DataFrame(list,index=['第一集','第二集','第三集','第四集'],
      columns=['西游记和红楼梦'])
p.to_excel('.\excel\西游记和红楼梦.xlsx')
print(p)