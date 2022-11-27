import gettext
import matplotlib.pyplot as plt
import warnings

# To clear a couple of deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Set the local directory and configure translations
localedir = './locales'
translate = gettext.translation('en', localedir, languages=['en'])
translate.install()
_ = translate.gettext

SHAPES = [_('line'), _('circle'), _('square')]
COLORS = [_('red'), _('green'), _('blue')]
SIZES = [_('little'), _('medium'), _('big')]


def main():
    """
    The program asks for shape, color and size for the figure and then it is drawn.
    :return: Nothing.
    """
    shape_wanted = get_shape()
    color_wanted = get_color(shape_wanted)
    size_wanted = get_size(shape_wanted, color_wanted)
    draw_canvas(shape_wanted, color_wanted, size_wanted)


def draw_shape(shape_wanted):
    """
    The figure is drawn in the final drawing.
    :param shape_wanted: String with the shape desired.
    :return: The figure drawn in the canvas with a 'default size and color.
    """
    if shape_wanted == _('line'):
        figure = plt.Line2D((0, 1), (0, 1), lw=1)
    elif shape_wanted == _('circle'):
        figure = plt.Circle((5, 5), 1)
    else:
        figure = plt.Rectangle((1, 1), 0, 0, fc='black', ec='black')

    return figure


def color_shape(figure_drawn, color_wanted):
    """
    The figure is filled and coloured with the user desired color.
    :param figure_drawn: default figure drawn in the canvas
    :param color_wanted: String with the user desired color.
    :return: The drawn and colored figure.
    """
    print(color_wanted)
    if color_wanted == _('red'):
        figure_drawn.set_color('red')
    elif color_wanted == _('green'):
        figure_drawn.set_color('green')
    else:
        figure_drawn.set_color('blue')

    return figure_drawn


def set_height_width(figure_colored, shape_wanted, size):
    """
    Change the figure to the user desired size depending on the figure's shape.
    :param figure_colored: Figure drawn and colored.
    :param shape_wanted: String with the wanted user shape.
    :param size: String with the size desired by user.
    :return: The drawn and colored figure resized.
    """
    if shape_wanted == _('line'):
        figure_colored.set_data([0, size], [0, size])
    else:
        figure_colored.set_height(size)
        figure_colored.set_width(size)
    return figure_colored


def resize_shape(figure_colored, size_wanted, shape_wanted):
    """
    The user's figure is resized to the desired size depending on the figure size.
    :param figure_colored: The figure drawn and colored.
    :param size_wanted: String with the user's desired size.
    :param shape_wanted: String with the user's desired shape.
    :return: The figure resized to the user's desired size.
    """
    if size_wanted == _('little'):
        figure_resized = set_height_width(figure_colored, shape_wanted, 1)
    elif size_wanted == _('medium'):
        figure_resized = set_height_width(figure_colored, shape_wanted, 5)
    else:
        figure_resized = set_height_width(figure_colored, shape_wanted, 10)

    return figure_resized


def draw_canvas(shape_wanted, color_wanted, size_wanted):
    """
    The drawing is done and shown to the user.
    :param shape_wanted: String with the shape desired by the user.
    :param color_wanted: String with the color desired by the user.
    :param size_wanted: String with the size desired by the user.
    :return: Nothing.
    """
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
    """
    The program asks the user which shape will the figure have.
    :return: String with the desired shape.
    """
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
    """
    The program asks the user which color will the figure have.
    :param shape_wanted: String with the desired shape.
    :return: String with the color desired.
    """
    print(_('You selected to draw a') + ' ' + _(shape_wanted) + ' ' + _(', now select color: red, green or blue.'))
    color_wanted = input().lower()
    while color_wanted not in COLORS:
        print(_('You misspelled the color. Please, write it again.'))
        print(_('What color do you want for your shape? Red, green or blue?'))
        color_wanted = input().lower()
    return color_wanted


def get_size(shape_wanted, color_wanted):
    """
    The program asks the user which size will the figure have.
    :param shape_wanted: String with the user desired shape.
    :param color_wanted: String with the user desired color.
    :return: String with the desired size.
    """
    print(_('You selected a') + ' ' + _(color_wanted) + ' ' + _(shape_wanted) +
          _(', now select size: little, medium or big.'))
    size_wanted = input().lower()
    while size_wanted not in SIZES:
        print(_('You misspelled the size. Please, write it again.'))
        print(_('What size do you want for your shape? Little, medium or big?'))
        size_wanted = input().lower()
    return size_wanted


if __name__ == '__main__':
    """
    Execution of the program.
    """
    main()
