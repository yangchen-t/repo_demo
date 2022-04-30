#!/bin/bash 



sed -i s/tj032/$1/g /lidar_calib_pakgs/start_result_rviz2.rviz 

rviz2 -d /lidar_calib_pkgs/start_result_rviz2.rviz

sed -i s/$1/tj032/g /lidar_calib_pakgs/start_result_rviz2.rviz
