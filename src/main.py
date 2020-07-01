"""
Route Planner
Project 4 from Udacity's Data Structure & Algorithms Nanodegree Program
"""
import sys, os
from helpers import Map, load_map, show_map
from student_code import shortest_path

this_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(this_path, "objects"))
map_path = os.path.join(this_path, "../data/map-40.pickle")
map_40 = load_map(map_path)
#show_map(map_40)
start_node = 8
goal_node = 24
path = shortest_path(map_40, start_node, goal_node)
print(path)

#(8, 24, [8, 14, 16, 37, 12, 17, 10, 24])