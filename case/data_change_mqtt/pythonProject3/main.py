# -*- coding: utf-8 -*-
import time
import xlwt


def timestamp_to_time(timestamp):
    # timearray = time.strptime(timestamp, "%Y%m%dT%H%M%SZ")
    stamp = time.mktime(time.strptime(timestamp,'%Y%m%dT%H%M%SZ'))
    # print(stamp)
    delta = 8 * 3600.0
    new_stamp = stamp + delta
    local_time = time.localtime(new_stamp)

    otherstyletime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return otherstyletime


def container_Statistics(missionParas):
    container_type = missionParas["containerId1Size"]
    container_count = -1
    if missionParas["containerId1"] == "":
        container_count = 0
    elif container_type == 40:
        container_count = 1
    elif missionParas["containerId2"] == "":
        container_count = 1
    else:
        container_count = 2
    return container_count


def read_log(path):
    namespace = "A021"
    with open(path, 'r') as f:
        line = f.readlines()
        # print(line[27])
        navi = []
        alignment = []
        mission = []
    for i in range(len(line)):
        if line[i].find('topic:') != -1 and line[i].find('Message received') == -1:

            json_str = '{' + line[i].rstrip('\n').strip().split("]:")[1] + '}'
            json_str = json_str.replace('topic', '"topic"')
            json_str = json_str.replace('msg', '"msg"')
            json_str = json_str.replace(':', ':"', 1)
            json_str = json_str.replace(',', '",', 1)
            # print(json_str)
            json_dict = eval(json_str)
            topic = json_dict["topic"].strip()

            if topic == "to/v1/devicetask/mission/request/" + namespace:
                try:
                    timestamp = json_dict["msg"]['header']['time']
                except:
                    timestamp = ""
                time = timestamp_to_time(timestamp)
                deviceId = json_dict["msg"]['header']['deviceId']
                missiontype = json_dict["msg"]["body"]['missionType']
                operateType = json_dict["msg"]["body"]['operateType']
                locationType = json_dict["msg"]["body"]['destination']['locationType']
                locationId = json_dict["msg"]["body"]['destination']['locationId']

                if json_dict["msg"]["body"]["missionParas"]:
                    missionParas = json_dict["msg"]["body"]["missionParas"]
                    container_type = missionParas["containerId1Size"]
                    container_count = container_Statistics(missionParas)

                    mission.append(
                        ['mission',time, deviceId, missiontype, operateType, locationType, locationId, container_type,
                         container_count])
                    # mission.append([missiontype, operateType, locationType, locationId, container_type, container_count])

                else:
                    mission.append([timestamp, deviceId, missiontype, operateType])
                    # mission.append([deviceId, missiontype, operateType, locationType, locationId, ])

            if topic == "to/v1/devicenavi/navi/request/" + namespace:
                try:
                    timestamp = json_dict["msg"]['header']['timestamp']
                except:
                    timestamp = ""
                deviceId = json_dict["msg"]['header']['deviceId']
                locationType = json_dict["msg"]["body"]["destination"]["locationType"]
                description = json_dict["msg"]["body"]["destination"]["description"]
                isFinalNavi = json_dict["msg"]["body"]["isFinalNavi"]

                navi.append(['navi',timestamp, deviceId, locationType, description, isFinalNavi])
                # navi.append([deviceId, locationType, description, isFinalNavi])

            if topic == "to/v1/alignment/inposition/request/" + namespace:
                try:
                    timestamp = json_dict["msg"]['header']['timestamp']
                    time = timestamp_to_time(timestamp)
                except:
                    timestamp = ""
                    time = ""
                deviceId = json_dict["msg"]['header']['deviceId']
                inPosition = json_dict["msg"]["body"]["inPosition"]
                offset = json_dict["msg"]["body"]["offset"] * 0.001
                targetId = json_dict["msg"]["body"]['targetId']

                alignment.append(['alignment',time, deviceId, inPosition, offset, targetId])
                # alignment.append([deviceId, inPosition, offset])
    return mission, navi, alignment


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font
    return style


def write_excel(data1, sheet_name_1, data2, sheet_name_2):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(sheet_name_1, cell_overwrite_ok=True)
    row_1 = ['topic','时间(UTC+8)','车辆编号','作业任务类型','业务场景类型','位置类型','位置编号','箱尺寸','箱数']
    for i in range(len(row_1)):
        sheet1.write(0,i + 1,row_1[i],set_style('Times New Roman', 220, True))

    for i in range(0, len(data1)):
        sheet1.write(i + 1, 0 , i + 1,set_style('Times New Roman', 220, True))
        for j in range(0, len(data1[i])):
            # print(data[i][j])
            sheet1.write(i + 1, j + 1, data1[i][j], set_style('Times New Roman', 220, True))
    sheet2 = f.add_sheet(sheet_name_2, cell_overwrite_ok=True)
    row_2 = ['topic','时间(UTC+8)','车辆编号','inposition','偏移量/m','作业位置']
    for i in range(len(row_2)):
        sheet2.write(0,i + 1,row_2[i],set_style('Times New Roman', 220, True))

    for i in range(0, len(data2)):
        sheet2.write(i + 1, 0 , i + 1,set_style('Times New Roman', 220, True))
        for j in range(0, len(data2[i])):
            # print(data[i][j])
            sheet2.write(i + 1, j + 1, data2[i][j], set_style('Times New Roman', 220, True))
    local_time = time.localtime()
    time_result = time.strftime('%m-%d %H:%m',time.localtime(time.time()))
    f.save('result'+str(time_result)+'.xls')


if __name__ == '__main__':
    path = '/home/westwell/PycharmProjects/pythonProject3/mqtt_agent/mqtt_0825'
    mission, navi, alignment = read_log(path)
    # print(mission)
    print('write successed')
    write_excel(mission, 'mission', alignment, 'alignment')
