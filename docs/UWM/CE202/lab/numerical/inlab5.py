import numpy as np

a_d = 8
v_c = -4
timestamp = np.arange(0,2,0.01)

v_d    = lambda time  : a_d*time
del_sd = lambda time  : a_d/2 * pow(time,2)
del_sa = lambda del_sd: del_sd/-2

v_a = lambda time : a_d/-2*time
# v_b = lambda time : v_c/2
v_arb = lambda v_a,v_b : v_a - v_b

# theta = 150
# v_radian     = r_d(theta_d,theta)
# v_theta = r(theta) *  theta_d
# print (v_radian)
# print (v_theta)


vd_stamp = [ v_d(t) for t in timestamp]
del_sd   = [ del_sd(t) for  t in timestamp ]
del_sa   = [ del_sa(sd) for sd in del_sd ]

v_a   = [ v_a(t) for t in timestamp]
# v_b   = [ v_b(t) for t in timestamp]
v_b = v_c/2
v_arb = [ v_arb(a,v_b) for a in v_a]

from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line

position = (
    Line()
    .add_xaxis(xaxis_data=timestamp)
    .add_yaxis(
        series_name="displacement_D",
        y_axis=del_sd,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="displacement_A",
        y_axis=del_sa,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
        # International System of Units (SI) mm
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Pulley System", subtitle="accerlation d = %s m/s2 " %(a_d) ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=True),
    )
   
)

spped = (
    Line()
    .add_xaxis(xaxis_data=timestamp)
    .add_yaxis(
        series_name="velocity_A",
        y_axis=v_a,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),)

    .add_yaxis(
        series_name="velocity_A/B",
        y_axis=v_arb,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False))

    .set_global_opts(
        title_opts=opts.TitleOpts(title="Relative speed", subtitle="v_c = %s m/s "%(v_c),
        pos_bottom="48%"),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        legend_opts=opts.LegendOpts(pos_bottom="48%"),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,
        # min_=0,
        # max_=200,
        # # interval=1,
        # axislabel_opts=opts.LabelOpts(formatter="{value} s"),
        # axistick_opts=opts.AxisTickOpts(is_show=True),
        # splitline_opts=opts.SplitLineOpts(is_show=True),
        ),


    )
)




grid = (
    Grid()
    .add(position, grid_opts=opts.GridOpts(pos_bottom="60%"))
    .add(spped, grid_opts=opts.GridOpts(pos_top="60%"))
     .render("pulley_ad%s_vc%s.html" %(a_d,v_c) ) 
)