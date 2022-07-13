#!/usr/bin/env python
import pandas as pd
import sys
import numpy as np
from math import sin, cos, atan2, pi
from pyproj import Proj

from geometry_msgs.msg import Pose2D

# tianjin FMS delta x/y
remote_delta_x = 565123.0
remote_delta_y = 4317123.0

# remote_delta_x = 0.0
# remote_delta_y = 0.0

local_delta_x = 4078390.0167294773 + 314.61
local_delta_y = -1527665.1822423297 + 4.0
local_rotation = 1.3428834074238685

local_tran_matrix = np.array(
        [
            [cos(local_rotation), -sin(local_rotation), local_delta_x],
            [sin(local_rotation), cos(local_rotation), local_delta_y],
            [0, 0, 1]
        ]
    )

def utm_to_local_pose(utm_pose_matrix):
    local_pose_matrix = np.dot(local_tran_matrix, utm_pose_matrix)
    return local_pose_matrix

def local_to_utm_pose(local_pose_matrix):
    trans_reverse = np.linalg.inv(local_tran_matrix)
    utm_pose_matrix = np.dot(trans_reverse, local_pose_matrix)
    return utm_pose_matrix

def remote_to_local_pose(x, y, theta=0.0):
    utm_pose_matrix = np.array(
        [
            [cos(theta), -sin(theta), x + remote_delta_x],
            [sin(theta), cos(theta), y + remote_delta_y],
            [0, 0, 1]
        ]
    )
    local_pose_matrix = utm_to_local_pose(utm_pose_matrix)
    local_pose = Pose2D()
    local_pose.x = local_pose_matrix[0][2]
    local_pose.y = local_pose_matrix[1][2]
    local_pose.theta = atan2(local_pose_matrix[1][0], local_pose_matrix[0][0])
    return local_pose.x, local_pose.y

def local_to_remote_pose(x, y, theta=0.0):
    local_pose_matrix = np.array(
        [
            [cos(theta), -sin(theta), x],
            [sin(theta), cos(theta), y],
            [0, 0, 1]
        ]
    )
    utm_pose_matrix = local_to_utm_pose(local_pose_matrix)
    remote_pose = Pose2D()
    remote_pose.x = utm_pose_matrix[0][2] - remote_delta_x
    remote_pose.y = utm_pose_matrix[1][2] - remote_delta_y
    remote_pose.theta = pi / 2.0 - atan2(utm_pose_matrix[1][0], utm_pose_matrix[0][0])
    lon, lat = utmInverse(remote_pose.x, remote_pose.y) # to get utm for heatmap
    return remote_pose.x, remote_pose.y, remote_pose.theta # for tj fms
    # return lon, lat, 0

def utmInverse(x, y):
    utm = Proj(proj='utm', zone=50, ellps='WGS84')  # thailand 47 xingjiang45 tianjin 50 qingdao 51 Denmark 32
    lon, lat = utm(x, y, inverse=True)  # ouput  lon  and lan
    return lon, lat

def utm2(x, y, z):
    return pd.Series(local_to_remote_pose(x, y, z), index=['WGS84_x', 'WGS84_y', 'theta'])

def process_csv(csv_path):
    train_data = pd.read_csv(csv_path)
    train_data[['WGS84_x', 'WGS84_y', 'theta']] = train_data.apply(
        lambda x: utm2(x['x'], x['y'], x['z']), axis=1)
    print(train_data)
    train_data.to_csv('out_charge_tran.csv', index=False)

def main():
    if len(sys.argv) < 2:
        print("Please provide csv path.")
    else:
        process_csv(sys.argv[1])

if __name__ == '__main__':
    main()



