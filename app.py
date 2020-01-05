from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Map, Line, Timeline, Bar
from pyecharts.globals import ChartType,SymbolType

df = pd.read_csv("GDP.csv", encoding='gbk')
df1 = pd.read_csv("arrivals.csv",encoding = 'gbk')
df2 = pd.read_csv("departure.csv",encoding = 'gbk')
df3 = pd.read_csv("highincome_a.csv",encoding = 'gbk')
df4 = pd.read_csv("lowincome_d.csv",encoding = 'gbk')
df5 = pd.read_csv("arrivals_departure2.csv",encoding = 'gbk')
app = Flask(__name__)

# 准备工作

regions_available = list(df.CountryName.dropna().unique())
@app.route('/', methods=['GET'])
def hu_run_2019():
    data_str = df.to_html()
    return render_template('results2.html',
                           the_title='世界出入境人数与就业人口人均GDP之间的关系',
                           the_res=data_str,
                           the_select_region=regions_available)


@app.route('/hurun', methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region)  # 检查用户输入
    the_region = request.form["the_region_selected"]
    print(the_region)
    dfs = df.query("CountryName=='{}'".format(the_region))


    fig = dfs.iplot(kind="bar", x="CountryName", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
    data_str = dfs.to_html()

    return render_template('results2.html',
                           the_title='世界出入境人数与就业人口人均GDP之间的关系',
                           the_plot_all=plot_all,
                           # the_plot_all = [],
                           the_res=data_str,
                           the_select_region=regions_available,
                           )


@app.route('/arrivals',methods=['GET'])
def arrivals():
    fig = df1.iplot(kind="bar", x="Country Name", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
        data_str = df1.to_html()
        return render_template('results2.html',
                               the_plot_all=plot_all
                               )


@app.route('/departure', methods=['GET'])
def departure():
    fig = df2.iplot(kind="bar", x="Country Name", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
        data_str = df2.to_html()
    return render_template('results2.html',
                           the_plot_all=plot_all,
                           )
@app.route('/high', methods=['GET'])
def high():
    fig = df3.iplot(kind="bar", x="Country Name", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
        data_str = df3.to_html()

    return render_template('results2.html',
                           the_plot_all=plot_all)

@app.route('/low', methods=['GET'])
def low():
    fig = df4.iplot(kind="line", x="Country Name", asFigure=True)
    py.offline.plot(fig, filename="example1.html", auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())
        data_str = df4.to_html()

    return render_template('results2.html',
                           the_res=data_str,
                           the_plot_all=plot_all)



@app.route('/all', methods=['GET'])
def all():
    res = {
        "name": "中国"}
    return render_template("index.html", **res)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
