# -*- coding: utf-8 -*-

import os
from PIL import Image
from django import template
import random

register = template.Library()


def thumbnail(my_file, size='150x150'):
    # defining the size
    x, y = [int(x) for x in size.split('x')]
    # defining the filename and the miniature filename
    filehead, filetail = os.path.split(my_file.path)
    basename, my_format = os.path.splitext(filetail)
    miniature = basename + '_' + size + my_format
    filename = my_file.path
    miniature_filename = os.path.join(filehead, miniature)
    filehead, filetail = os.path.split(my_file.url)
    miniature_url = filehead + '/' + miniature
    if os.path.exists(miniature_filename) and os.path.getmtime(filename) > os.path.getmtime(miniature_filename):
        os.unlink(miniature_filename)
    # if the image wasn't already resized, resize it
    if not os.path.exists(miniature_filename):
        image = Image.open(filename)
        image.thumbnail([x, y], Image.ANTIALIAS)
        try:
            image.save(miniature_filename, image.format, quality=90, optimize=1)
        except:
            image.save(miniature_filename, image.format, quality=90)

    return miniature_url


class RandomMusicSignNode(template.Node):
    """ Prints a random music symbol """

    def __init__(self):
        self.music_html_signs = ["&#9833;", "&#9834;", "&#9835;", "&#9836;", "&#9837;", "&#9838;", "&#9839;"]

    def render(self, context):
        return random.choice(self.music_html_signs)


def do_random_music_sign(parser, token):
    return RandomMusicSignNode()


def add_attributes(field, css):
    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            t, v = d.split(':')
            attrs[t] = v

    return field.as_widget(attrs=attrs)

register.filter(add_attributes)
register.filter(thumbnail)
register.tag('random_music_sign', do_random_music_sign)