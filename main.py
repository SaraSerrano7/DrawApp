import gettext
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Set the local directory
localedir = './locales'
translate = gettext.translation('en', localedir, languages=['en'])
translate.install()
_ = translate.gettext

SHAPES = [_('line'), _('circle'), _('square')]
COLORS = [_('red'), _('green'), _('blue')]
SIZES = [_('little'), _('medium'), _('big')]


def main():
    shape_wanted = get_shape()
    color_wanted = get_color(shape_wanted)
    size_wanted = get_size(shape_wanted, color_wanted)
    draw_canvas(shape_wanted, color_wanted, size_wanted)


def draw_shape(shape_wanted):
    if shape_wanted == _('line'):
        figure = plt.Line2D((0, 1), (0, 1), lw=1)
    elif shape_wanted == _('circle'):
        figure = plt.Circle((5, 5), 1)
    else:
        figure = plt.Rectangle((1, 1), 0, 0, fc='black', ec='black')

    return figure


def color_shape(figure_drawn, color_wanted):
    print(color_wanted)
    if color_wanted == _('red'):
        figure_drawn.set_color('red')
    elif color_wanted == _('green'):
        figure_drawn.set_color('green')
    else:
        figure_drawn.set_color('blue')

    return figure_drawn


def set_height_width(figure_colored, shape_wanted, size):
    if shape_wanted == _('line'):
        figure_colored.set_data([0, size], [0, size])
    else:
        figure_colored.set_height(size)
        figure_colored.set_width(size)
    return figure_colored


def resize_shape(figure_colored, size_wanted, shape_wanted):
    if size_wanted == _('little'):
        figure_resized = set_height_width(figure_colored, shape_wanted, 1)
    elif size_wanted == _('medium'):
        figure_resized = set_height_width(figure_colored, shape_wanted, 5)
    else:
        figure_resized = set_height_width(figure_colored, shape_wanted, 10)

    return figure_resized


def draw_canvas(shape_wanted, color_wanted, size_wanted):
    figure_drawn = draw_shape(shape_wanted)
    figure_colored = color_shape(figure_drawn, color_wanted)
    figure_resized = resize_shape(figure_colored, size_wanted, shape_wanted)

    if shape_wanted == _('line'):
        plt.gca().add_line(figure_resized)
    else:
        plt.gca().add_patch(figure_resized)

    plt.axis('scaled')
    plt.title(_('Your figure'))
    plt.xlim([0, 15])
    plt.ylim([0, 15])
    plt.show()


def get_shape():
    print(_("Select which shape you want to draw: line, circle or square."))
    shape_wanted = input().lower()
    while shape_wanted not in SHAPES:
        print(shape_wanted)
        print(SHAPES)
        print(_('You misspelled the shape. Please, write it again.'))
        print(_('What do you want to draw? Line, circle or square?'))
        shape_wanted = input().lower()
    return shape_wanted


def get_color(shape_wanted):
    print(_('You selected to draw a') + ' ' + _(shape_wanted) + ' ' + _(', now select color: red, green or blue.'))
    color_wanted = input().lower()
    while color_wanted not in COLORS:
        print(_('You misspelled the color. Please, write it again.'))
        print(_('What color do you want for your shape? Red, green or blue?'))
        color_wanted = input().lower()
    return color_wanted


def get_size(shape_wanted, color_wanted):
    print(_('You selected a') + ' ' + _(color_wanted) + ' ' + _(shape_wanted) +
          _(', now select size: little, medium or big.'))
    size_wanted = input().lower()
    while size_wanted not in SIZES:
        print(_('You misspelled the size. Please, write it again.'))
        print(_('What size do you want for your shape? Little, medium or big?'))
        size_wanted = input().lower()
    return size_wanted


if __name__ == '__main__':
    main()
