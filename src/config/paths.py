import os
from .assets import *

base_route = os.path.expandvars(r'%LOCALAPPDATA%\Programs\CoviStats')
font_route = os.path.join(base_route, r"assets\font.ttf")
icon_route = os.path.join(base_route, r"assets\icon.ico")
titlebar_icon_route = os.path.join(base_route, r"assets\titlebar_icon.png")
global_heading_image_route = os.path.join(base_route, r"assets\global_heading_image.png")
searchbar_icon_route = os.path.join(base_route, r"assets\searchbar_icon.png")
ascending_cases_icon_route = os.path.join(base_route, r"assets\ascending_cases_filter_icon.png")
descending_cases_icon_route = os.path.join(base_route, r"assets\descending_cases_filter_icon.png")
a_to_z_alphabetical_icon_route = os.path.join(base_route, r"assets\a_to_z_alphabetical_filter_icon.png")
z_to_a_alphabetical_icon_route = os.path.join(base_route, r"assets\z_to_a_alphabetical_filter_icon.png")
x_icon_route = os.path.join(base_route, r"assets\x_icon.png")

#paths array
paths = [
	".",
	"assets"
]

#assets array
assets = [
	(icon_route, icon_ico),
	(titlebar_icon_route, titlebar_icon_png),
	(global_heading_image_route, global_heading_png),
	(searchbar_icon_route, searchbar_icon_png),
	(ascending_cases_icon_route, ascending_cases_icon_png),
	(descending_cases_icon_route, descending_cases_icon_png),
	(a_to_z_alphabetical_icon_route, a_to_z_alphabetical_icon_png),
	(z_to_a_alphabetical_icon_route, z_to_a_alphabetical_icon_png),
	(x_icon_route, x_icon_png)
]