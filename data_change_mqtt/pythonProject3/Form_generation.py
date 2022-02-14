import xlwt

mission = [['MOVE', 'MANUALMOVE', 'QCTP', 'QCTP.Q303.108', 0, 0], ['MOVE', 'MANUALMOVE', 'QCTP', 'QCTP.Q303.108', 0, 0], ['MOVE', 'MANUALMOVE', 'PSTP', 'STATION-02-QPB1', 0, 0], ['MOVE', 'MANUALMOVE', 'QCTP', 'QCTP.Q303.108', 0, 0], ['MOVE', 'MANUALMOVE', 'PSTP', 'STATION-03', 0, 0], ['MOVE', 'MANUALMOVE', 'PSTP_HPB', 'STATION-03-HPB2', 0, 0], ['MOVE', 'MANUALMOVE', 'QCTP', 'QCTP.Q302.106', 0, 0], ['MOVE', 'MANUALMOVE', 'PSTP', 'STATION-03', 0, 0], ['MOVE', 'MANUALMOVE', 'PSTP', 'STATION-02', 0, 0], ['MOVE', 'MANUALMOVE', 'YCTP', 'YARD.2AA.30', 0, 0], ['RECEIVE', 'LOAD', 'YCTP', 'YARD.2AA.71', 20, 2], ['RECEIVE', 'LOAD', 'YCTP', 'YARD.2AA.71', 20, 2], ['DELIVER', 'LOAD', 'PSTP', 'STATION-03-QPB1', 20, 2], ['DELIVER', 'LOAD', 'PSTP', 'STATION-03-QPB1', 20, 2], ['RECEIVE', 'LOAD', 'YCTP', 'YARD.2AA.53', 20, 2]]
navi = [['A021', 'QCTP', '157805', True], ['A021', 'QCTP', '157719', True], ['A021', 'PSTP_QPB', '', False], ['A021', 'QCTP', '157719', True], ['A021', 'PSTP', '', True], ['A021', 'PSTP_HPB', '', False], ['A021', 'QCTP', '', True], ['A021', 'PSTP', '', True], ['A021', 'PSTP', '', True], ['A021', 'YCTP', '', True], ['A021', 'YCTP', '', True], ['A021', 'YCTP', '', True], ['A021', 'PSTP_QPB', '', False], ['A021', 'PSTP_QPB', '', False], ['A021', 'PSTP', '', True], ['A021', 'QCTP', '157743', True], ['A021', 'YCTP', '', True]]
alignment = [['20210822T084057Z', 'A021', 2, -3082], ['20210822T084102Z', 'A021', 2, 513], ['20210822T084123Z', 'A021', 2, 3281], ['20210822T084137Z', 'A021', 2, -515], ['20210822T084154Z', 'A021', 1, 0], ['20210822T084234Z', 'A021', 2, 6255], ['20210822T084308Z', 'A021', 2, -486], ['20210822T084332Z', 'A021', 2, -994000], ['20210822T084340Z', 'A021', 1, 0], ['20210822T084433Z', 'A021', 2, -255], ['20210822T092343Z', 'A021', 1, 0], ['20210822T092555Z', 'A021', 2, 460], ['20210822T092610Z', 'A021', 1, 0], ['20210822T092720Z', 'A021', 2, -3236], ['20210822T092741Z', 'A021', 2, 0], ['20210822T092742Z', 'A021', 1, 0], ['20210822T092908Z', 'A021', 2, 0], ['20210822T092912Z', 'A021', 2, 3180], ['20210822T092934Z', 'A021', 2, 0], ['20210822T092935Z', 'A021', 1, 0], ['20210822T093622Z', 'A021', 2, 254], ['20210822T093651Z', 'A021', 2, -83], ['20210822T093658Z', 'A021', 1, 0]]

# print(mission)

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.colour_index = 4
    font.height = height
    style.font = font
    return style


def write_excel(data):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('mission', cell_overwrite_ok=True)
    row0 = []
    col0 = []
    # sheet1.write(1,1,'20210817T152919Z')
    for i in range(0, len(data)):
        for j in range(0,len(data[i])):
            # print(data[i][j])
            sheet1.write(i+1, j+1, data[i][j], set_style('Times New Roman', 220, True))
    f.save('test.xls')


write_excel(mission)
# write_excel(navi)
# write_excel(alignment)
