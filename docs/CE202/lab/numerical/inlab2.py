import numpy as np

s_0 = 0
t_0 = 0
v_0 = 0.1
k   = 0.5

v_ft = lambda k,t,v_0 : pow(2*k*t + pow(v_0,-2),-1/2)
#v_ft(k,1,v_0)

a_fv = lambda k,v : -1*k*pow(v,3) 
#a_fv(k,v_0)

x_ft = lambda k,t,v_o : 1/k* (pow( 2*k*t + pow(v_0,-2) , 1/2) - pow(v_0,-1) )
#x_ft(k,1,v_0)

timestamp = np.arange(0, 10.1, 0.1)
velostamp = [v_ft(k,ts,v_0) for ts in timestamp] 
acc_stamp = [a_fv(k,vs) for vs in velostamp]
pos_stamp = [x_ft(k,ps,v_0) for ps in timestamp]


from pyecharts.charts import Line
import pyecharts.options as opts
(
    Line()
    .add_xaxis(xaxis_data=timestamp)
    .add_yaxis(
        series_name="velocity",
        y_axis=velostamp,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="acceleration",
        y_axis=acc_stamp,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="displacement",
        y_axis=pos_stamp,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="k = %s , initiial v = %s" %(k,v_0)),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("k%s_v%s.html" %(k,v_0)) 
)