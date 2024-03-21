import numpy as np

t_point    = 150   
theta_d    =  6
theta_dd   = 0

if t_point < 0 :
    thetastamp = np.arange(0, t_point-0.1, -1)
else :
    thetastamp = np.arange(0, t_point+0.1, 1)


r    = lambda theta : 200*(2-np.cos(theta/180*np.pi))
r_d  = lambda theta_d,theta : 200*(np.sin(theta/180*np.pi) * theta_d) 
r_dd = lambda theta_dd,theta_d,theta : 200 * (np.cos(theta/180*np.pi)*pow(theta_d,2) + np.sin(theta/180*np.pi) * theta_dd )

# theta = 150
# v_radian     = r_d(theta_d,theta)
# v_theta = r(theta) *  theta_d
# print (v_radian)
# print (v_theta)


r_stamp = [r(x) for x in thetastamp]

print (thetastamp)

vr_stamp = [r_d(theta_d,theta) for theta in thetastamp]
vt_stamp = [r(theta) *  theta_d  for theta in thetastamp ]

ar_stamp = [r_dd(theta_dd,theta_d,theta) -r(theta)*pow(theta_d,2) for theta in thetastamp ]
at_stamp = [r(theta)*theta_dd + 2*r_d(theta,theta_d)*theta_d      for theta in thetastamp ]


from pyecharts.charts import Line
import pyecharts.options as opts
(
    Line()
    .add_xaxis(xaxis_data=thetastamp)
    .add_yaxis(
        series_name="velocity_radian",
        y_axis=vr_stamp,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="velocity_theta",
        y_axis=vt_stamp,
        areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
    )

    # .add_yaxis(
    #     series_name="acceleration_radian",
    #     y_axis=ar_stamp,
    #     areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    #     label_opts=opts.LabelOpts(is_show=False),
    # )

    # .add_yaxis(
    #     series_name="acceleration_theta",
    #     y_axis=at_stamp,
    #     areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
    #     label_opts=opts.LabelOpts(is_show=False),
    # )
    # International System of Units (SI) mm
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Polar System", subtitle="agular speed = %s mm/s; angle = %s" %(theta_d,t_point) ),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False),
    )
    .render("polar_vt_%s_theta%s.html" %(theta_d,t_point) ) 
)