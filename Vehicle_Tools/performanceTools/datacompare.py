import numpy as np
import matplotlib.pyplot as plt


# 柱状图
# plt.style.use("ggplot")

# shops = ["wh2", "wh6"]
# sales_product_1 = [116.28, 115.46]
# sales_product_2 = [55.86, 58.42]
# sales_product_3 = [38.33, 41.66]
# sales_product_4 = [44.67, 40.76]
# sales_product_5 = [51.23, 50.73]
# # 创建分组柱状图，需要自己控制x轴坐标
# xticks = np.arange(len(shops))

# fig, ax = plt.subplots(figsize=(10, 7))
# # 所有门店第一种产品的销量，注意控制柱子的宽度，这里选择0.25
# p1 = ax.bar(xticks, sales_product_1, width=0.1, label="fusion_localizer2", color="red")
# plt.bar_label(p1, label_type='edge')
# # 所有门店第二种产品的销量，通过微调x轴坐标来调整新增柱子的位置
# p2 = ax.bar(xticks + 0.1, sales_product_2, width=0.1, label="planner", color="blue")
# plt.bar_label(p2, label_type='edge')
# # 所有门店第三种产品的销量，继续微调x轴坐标调整新增柱子的位置
# p3 = ax.bar(xticks + 0.2, sales_product_3, width=0.1, label="lidar_obj_det", color="green")
# plt.bar_label(p3, label_type='edge')

# p4 = ax.bar(xticks + 0.3, sales_product_4, width=0.1, label="105", color="grey")
# plt.bar_label(p4, label_type='edge')

# p5 = ax.bar(xticks + 0.4, sales_product_5, width=0.1, label="106", color="black")
# plt.bar_label(p5, label_type='edge')

# ax.set_title("compare for plot", fontsize=15)
# ax.set_xlabel("module")
# ax.set_ylabel("avg size")
# ax.legend()

# # 最后调整x轴标签的位置
# ax.set_xticks(xticks + 0.2)
# ax.set_xticklabels(shops)
# plt.show()


import matplotlib.pyplot as plt
 
#折线图
plt.figure(figsize=(20, 10), dpi=100)
xticks = ['May 04 06:12:35', 'May 04 06:12:36', 'May 04 06:12:37', 'May 04 06:12:38', 'May 04 06:12:39', 'May 04 06:12:40', 'May 04 06:12:41', 'May 04 06:12:42', 'May 04 06:12:43', 'May 04 06:12:44', 'May 04 06:12:45', 'May 04 06:12:46', 'May 04 06:12:47', 'May 04 06:12:48', 'May 04 06:12:49', 'May 04 06:12:50', 'May 04 06:12:51', 'May 04 06:12:52', 'May 04 06:12:53', 'May 04 06:12:54', 'May 04 06:12:55', 'May 04 06:12:57', 'May 04 06:12:58', 'May 04 06:12:59', 'May 04 06:13:00', 'May 04 06:13:01', 'May 04 06:13:02', 'May 04 06:13:03', 'May 04 06:13:04', 'May 04 06:13:05', 'May 04 06:13:06', 'May 04 06:13:07', 'May 04 06:13:08', 'May 04 06:13:09', 'May 04 06:13:10', 'May 04 06:13:11', 'May 04 06:13:12', 'May 04 06:13:13', 'May 04 06:13:14', 'May 04 06:13:15', 'May 04 06:13:16', 'May 04 06:13:17', 'May 04 06:13:18', 'May 04 06:13:19', 'May 04 06:13:20', 'May 04 06:13:21', 'May 04 06:13:22', 'May 04 06:13:23', 'May 04 06:13:24', 'May 04 06:13:25', 'May 04 06:13:26', 'May 04 06:13:27', 'May 04 06:13:28', 'May 04 06:13:30', 'May 04 06:13:31', 'May 04 06:13:32', 'May 04 06:13:33', 'May 04 06:13:34']
left =      [115.84, 128.71, 115.84, 129.7, 117.82, 119.8, 114.85, 122.77, 117.82, 118.63, 117.82, 125.49, 112.87, 119.8, 110.89, 117.82, 110.89, 116.67, 105.94, 116.67, 112.75, 114.85, 104.95, 108.91, 105.94, 113.86, 113.86, 119.8, 114.85, 119.8, 110.89, 123.76, 108.91, 124.75, 106.93, 114.85, 110.89, 118.81, 111.88, 112.87, 109.9, 119.8, 111.88, 123.76, 119.8, 124.75, 118.63, 113.86, 115.69, 120.79, 116.83, 113.86, 120.79, 112.75, 118.81, 110.89, 127.72, 112.87]
right =     [55.45, 53.47, 55.45, 61.39, 64.36, 63.37, 64.36, 64.36, 62.38, 61.76, 59.8, 63.37, 57.43, 56.44, 56.44, 56.44, 57.43, 54.46, 52.48, 53.47, 54.9, 54.46, 54.46, 54.46, 52.48, 53.47, 53.92, 51.49, 54.46, 55.88, 54.46, 54.46, 52.48, 54.46, 53.47, 55.88, 55.45, 53.47, 54.46, 54.46, 54.46, 56.44, 55.45, 56.44, 53.47, 52.94, 55.88, 52.48, 55.45, 54.46, 53.92, 52.94, 55.45, 55.45, 54.46, 55.45, 54.46, 54.46]
lidar_obj = [32.67, 29.7, 29.7, 31.68, 29.7, 28.71, 30.69, 27.72, 29.41, 31.37, 30.69, 29.7, 31.68, 31.68, 30.69, 31.68, 31.68, 31.68, 37.62, 51.96, 56.44, 55.45, 49.5, 45.54, 44.55, 48.04, 49.5, 49.5, 48.04, 50.5, 49.5, 46.53, 45.54, 44.55, 43.14, 41.58, 44.55, 41.58, 39.6, 40.59, 36.63, 37.62, 38.61, 37.62, 36.27, 37.25, 37.62, 37.62, 37.62, 37.25, 34.31, 36.63, 34.65, 33.66, 33.66, 35.64, 32.67, 33.66]

print(len(xticks),len(left),len(right),len(lidar_obj))
plt.plot(xticks, left, c='red', label="fusion")
plt.plot(xticks, right, c='green', linestyle='--', label="planner_ndoe")
plt.plot(xticks, lidar_obj, c='blue', linestyle='-.', label="lidar_obj")
plt.scatter(xticks, left, c='red')
plt.scatter(xticks, right, c='green')
plt.scatter(xticks, lidar_obj, c='blue')
plt.legend(loc='best')
plt.xticks(rotation=45)
plt.yticks(range(0, 150, 5))
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel("time", fontdict={'size': 16})
plt.ylabel("data", fontdict={'size': 16})
plt.title("all cpu used", fontdict={'size': 20})

plt.figure(figsize=(20, 10), dpi=100)
xticks = ['May 04 08:24:10', 'May 04 08:24:11', 'May 04 08:24:12', 'May 04 08:24:13', 'May 04 08:24:14', 'May 04 08:24:16', 'May 04 08:24:17', 'May 04 08:24:18', 'May 04 08:24:19', 'May 04 08:24:20', 'May 04 08:24:21', 'May 04 08:24:22', 'May 04 08:24:23', 'May 04 08:24:24', 'May 04 08:24:25', 'May 04 08:24:26', 'May 04 08:24:27', 'May 04 08:24:28', 'May 04 08:24:29', 'May 04 08:24:30', 'May 04 08:24:31', 'May 04 08:24:32', 'May 04 08:24:33', 'May 04 08:24:34', 'May 04 08:24:35', 'May 04 08:24:36', 'May 04 08:24:37', 'May 04 08:24:38', 'May 04 08:24:39', 'May 04 08:24:40', 'May 04 08:24:41', 'May 04 08:24:42', 'May 04 08:24:43', 'May 04 08:24:44', 'May 04 08:24:45', 'May 04 08:24:46', 'May 04 08:24:47', 'May 04 08:24:49', 'May 04 08:24:50', 'May 04 08:24:51', 'May 04 08:24:52', 'May 04 08:24:53', 'May 04 08:24:54', 'May 04 08:24:55', 'May 04 08:24:56', 'May 04 08:24:57', 'May 04 08:24:58', 'May 04 08:24:59', 'May 04 08:25:00', 'May 04 08:25:01', 'May 04 08:25:02', 'May 04 08:25:03', 'May 04 08:25:04', 'May 04 08:25:05', 'May 04 08:25:06', 'May 04 08:25:07', 'May 04 08:25:08', 'May 04 08:25:09']
left =      [178.43, 179.21, 170.59, 178.22, 173.27, 172.28, 173.27, 181.19, 178.22, 183.17, 176.24, 182.18, 173.27, 170.59, 171.29, 172.28, 118.81, 82.18, 81.19, 88.12, 86.14, 88.12, 81.37, 83.33, 81.19, 81.19, 80.2, 81.37, 79.21, 84.16, 82.18, 79.21, 87.13, 79.21, 85.15, 77.23, 78.22, 79.21, 77.23, 77.23, 79.21, 78.22, 86.14, 93.07, 107.92, 95.05, 90.2, 92.16, 105.94, 111.76, 111.88, 108.91, 123.53, 113.86, 118.81, 115.84, 127.72, 123.76]
right =    [55.88, 56.44, 57.43, 55.45, 57.43, 60.4, 58.42, 55.88, 54.46, 56.44, 54.46, 56.44, 57.43, 56.44, 56.44, 54.46, 54.46, 55.45, 58.42, 57.43, 55.88, 54.46, 55.45, 54.46, 55.45, 57.43, 59.41, 59.41, 63.37, 61.39, 62.38, 60.4, 64.36, 61.39, 61.39, 60.4, 62.38, 59.8, 61.39, 62.38, 62.38, 61.39, 62.38, 61.39, 60.4, 63.37, 59.41, 61.39, 58.82, 61.39, 61.39, 57.43, 57.43, 57.43, 58.42, 56.44, 51.49, 53.47]
lidar_obj = []
for i in range(51):
    i = 30 
    lidar_obj.append(i)
old_list = [46.08, 47.52, 48.51, 43.56, 39.6, 35.64, 30.69]
for i in old_list:
    lidar_obj.append(i)
print(lidar_obj)

print(len(xticks),len(left),len(right),len(lidar_obj))
plt.plot(xticks, left, c='red', label="fusion")
plt.plot(xticks, right, c='green', linestyle='--', label="planner_ndoe")
plt.plot(xticks, lidar_obj, c='blue', linestyle='-.', label="lidar_obj")
plt.scatter(xticks, left, c='red')
plt.scatter(xticks, right, c='green')
plt.scatter(xticks, lidar_obj, c='blue')
plt.legend(loc='best')
plt.xticks(rotation=45)
plt.yticks(range(0, 200, 5))
plt.grid(True, linestyle='--', alpha=0.5)
plt.xlabel("time", fontdict={'size': 16})
plt.ylabel("data", fontdict={'size': 16})
plt.title("all cpu used", fontdict={'size': 20})
plt.show()