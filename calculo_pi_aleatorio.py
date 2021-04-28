from random import uniform
# from bokeh.plotting import figure, show

def is_inside_circle(root=(0, 0), coordinate = (1, 1), circle_radio=1.0):
    x, y = coordinate
    root_x, root_y = root
    coordinate_distance_from_root = ((root_x-x)**2 + (root_y-y)**2)**.5
    if coordinate_distance_from_root < circle_radio: return True
    return False

def put_coordinate_in_field(coordinate, rectangle_field, circle_field, circle_radio):
    if is_inside_circle(coordinate=coordinate, circle_radio=circle_radio):
        circle_field.append(coordinate)
    else:
        rectangle_field.append(coordinate)

def throw_needle(x_range=(0.0, 1.0), y_range=(0.0, 1.0)):
    x = uniform(x_range[0], x_range[1])
    y = uniform(y_range[0], y_range[1])
    return (x, y)

# def graph_field(field, color="red", p=None):
#     xs = [i[0] for i in field]
#     ys = [i[1] for i in field]

#     if p == None:
#         p = figure(plot_width=500, plot_height=500)
#     p.circle(xs, ys, size=10, color=color, alpha=0.5)
#     return p

def estimate_pi(circle_field, total_neddles):
    neddles_in_circle = len(circle_field)
    pi = 4*neddles_in_circle / total_neddles
    return pi

def main(needles, circle_radio):
    circle_field = []
    rectangle_field = []
    for _ in range(needles):
        coordinate = throw_needle(
            x_range=(-circle_radio, circle_radio),
            y_range=(-circle_radio, circle_radio)
        )
        put_coordinate_in_field(
            coordinate,
            rectangle_field, 
            circle_field,
            circle_radio
        )
    
    pi = estimate_pi(circle_field, needles)
    print(f"Estimated value for pi with {needles} neddles is {pi}")

    # p = graph_field(rectangle_field, color="red")
    # p = graph_field(circle_field, color="blue", p = p)
    # show(p)

if __name__ == '__main__':
    number_of_needles = int(input("number of needles: "))
    circle_radio = float(input("radio of the circle: "))
    main(number_of_needles, circle_radio)