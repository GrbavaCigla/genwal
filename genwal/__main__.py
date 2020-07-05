import argparse
import re
import requests
import os

BACKGROUND = '{BACKGROUND}'
FOREGROUND1 = '{FOREGROUND1}'
FOREGROUND2 = '{FOREGROUND2}'
FOREGROUND3 = '{FOREGROUND3}'

def color(color: str):
    if not re.match(r'#[0-9a-fA-F]{6}', color):
        raise argparse.ArgumentTypeError
    return color

parser = argparse.ArgumentParser(
    prog='genwal',
    description='Little python script to generate Gentoo wallpapers',
    add_help=True
)

parser.add_argument('--bg', '--background', default="#4D4D4D", type=color)
parser.add_argument('--fg1', '--foreground1', default="#0D4F73", type=color)
parser.add_argument('--fg2', '--foreground2', default="#FFFFFF", type=color)
parser.add_argument('--fg3', '--foreground3', default="#007CBF", type=color)

args = parser.parse_args()

with open("wallpaper.svg") as file:
    pass