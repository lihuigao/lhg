import numbers
from pyecharts import options as opts
from pyecharts.charts import Map

#这个区域输入你的城市和对应城市的数据
number = [
['梧州市', 153],
['桂林市', 153],
['百色市', 104],
['柳州市', 68],
['南宁市',45],
['玉林市', 90],
['河池市',48],
['贺州市',42],
['贵港市',42],
['钦州市',28],
['来宾市',28],
['崇左市',24],
['防城港市',11],
['北海市',5]

]

city="广西" 

(Map()
.add(
    series_name="这个是图例",
    data_pair=number,
    maptype=city,
    is_map_symbol_show=True,
    label_opts= opts.LabelOpts(number),
    )

# 全局配置
.set_global_opts(
    toolbox_opts=opts.ToolboxOpts(),
    title_opts=opts.TitleOpts(title=city+"地图"), # 图表标题
    visualmap_opts=opts.VisualMapOpts(is_piecewise=True,max_=200,range_color=['#FFECEC','#EA0000']),
    # 这里的max和min需要根据数据来设置，range_color如果不设置的话也能出图，按默认值上色；需要自定义的我提供好几个颜色查询网站
    )
        
# 系列配置
.set_series_opts(
    label_opts=opts.LabelOpts(is_show=True, color="black", font_size = 10, rotate = 0)
    # 标签名称显示，默认为True，其它控制字体颜色，大小，方向
    ) 

.render(r"C:\Users\Lenovo\Desktop\寒假\地图绘制\统计分析与数据服务.html")# 生成本地html文件
)