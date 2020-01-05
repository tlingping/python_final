# 18级《Python》与17级《交互式数据可视化》协作期末项目
## 项目名称：世界出入境人数与就业人口人均GDP之间的关系
### 项目展示
* [pythonanywhere 链接](http://lingpingtang0.pythonanywhere.com)

本网站一共有6个url
* [使用for循环下拉框遍历option且选中想要的值，点击"do it！"出现图表](http://lingpingtang0.pythonanywhere.com/hurun)
* [2010、2013、2017国际入境人数](http://lingpingtang0.pythonanywhere.com/arrivals)
* [2010、2013、2017国际离境人数](http://lingpingtang0.pythonanywhere.com/departure)
* [高收入水平国家的出入境人数](http://lingpingtang0.pythonanywhere.com/high)
* [低收入水平国家的出入境人数](http://lingpingtang0.pythonanywhere.com/low)
* [使用if/else语句写小结](http://lingpingtang0.pythonanywhere.com/all)


### html文档介绍
results2.html: 首页及返回页html
index.html：总结页html

### python代码
使用模块：flask、pandas、pyecharts、numpy、cufflinks、plotly
读取数据：使用pandas读取csv文件，并以提取country值
处理数据：共使用了6个csv表格
python 文档与html文档的数据交互：利用传值，结合html模板数据

### web app动作
* 链接到以下路径 实现图表交互
/arrivals
/departure
/high
/low
* 其中使用了for循环以及if/else语句
