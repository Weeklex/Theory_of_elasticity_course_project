import managers.managers as man


x_corner = -1
y_corner = 1
h_s = 1
time = 1
h = 0.01
square = man.create_material_body(x_corner, y_corner, h_s)
tr = man.move_material_body(time, h, square)

man.plot_trajectory(square, tr)


vf = man.move_through_space(1, 0.1)
man.plot_velocity_fields(vf)
