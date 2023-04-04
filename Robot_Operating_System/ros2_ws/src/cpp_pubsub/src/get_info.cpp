#include <stdio.h>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include "cpp_pubsub/get_info.h"

std::string PicturesPath = "/debug/test";
std::string PicturesNumbersPath = "/scripts/pic/lib/numbers.csv";

void gettime()
{
	time_t rawtime;
	struct tm *ptminfo;
	time(&rawtime);
	ptminfo = localtime(&rawtime);
	printf("current: %02d-%02d-%02d %02d:%02d:%02d\n",                 //utc
	ptminfo->tm_year + 1900, ptminfo->tm_mon + 1, ptminfo->tm_mday,
	ptminfo->tm_hour, ptminfo->tm_min, ptminfo->tm_sec);
}

Ouint8 *TypeConversion(std::string str)
{
	return (unsigned char *)str.c_str();
}

path_select return_path()
{
	std::ifstream inFile(PicturesNumbersPath, std::ios::in);
	std::stringstream stream;
	std::string num;
	path_select pl;
    while (getline(inFile, num)){
		stream << num;
		stream >> pl.numbers;            // 文件读取
		pl.path = PicturesPath + std::to_string(pl.numbers) + ".png";
		return pl;
	}
	return pl;
}

void turn_picture_display(int mode){
	
	//config
	Ouint8* pIP = (Ouint8*)"192.168.112.11";
	Ouint8* pIP_back = (Ouint8*)"192.168.112.12";
	Ouint32 nPort = 5005;

	Ouint8* picPath = (Ouint8*)("/scripts/pic/52.png");
	Ouint8* picPath_back = (Ouint8*)("/scripts/pic/53.png");
	E_ScreenColor_G56 color = eSCREEN_COLOR_DOUBLE;
	int uAreaId = 0;
	int uAreaX = 16;//32
	int uAreaY = 0;
	int uWidth = 64;
	int uHeight = 32;

	//EQpageHeader_G6
	EQpageHeader_G6 pheader1;
	pheader1.PageStyle = 0x00;
	pheader1.DisplayMode = 0x07;    
	//0x00 –随机显示 0x01 –静止显示 0x02 –快速打出 0x03 –向左移动 0x04 –向左连移 0x05 –向上移动 0x06 –向上连移 0x07 –闪烁
	pheader1.ClearMode = 0x01;
	pheader1.Speed = 80;
	pheader1.StayTime = 10;
	pheader1.RepeatTime = 1;
	pheader1.ValidLen = 128;
	pheader1.CartoonFrameRate = 0x00;
	pheader1.BackNotValidFlag = 0x00;
	pheader1.arrMode = eMULTILINE;//eSINGLELINE
	pheader1.fontSize = 12;
	pheader1.color =E_Color_G56::eRED;
	pheader1.fontBold = false;
	pheader1.fontItalic = false;
	pheader1.tdirection = pNORMAL;
	pheader1.txtSpace = 0;
	pheader1.Valign = 0;
	pheader1.Halign = 0;

	if (mode == 1){
        bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, 32, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath);
        std::cout << "\033[31mfront ==> "<< picPath <<"\033[0m\n";
	    bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, 32, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath_back);
        std::cout << "\033[31mrear ==> "<< picPath_back <<"\033[0m\n";
	}
    else if (mode == 2 )
    {
	    bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, 32, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath_back);
	    std::cout << "\033[31mrear ==> "<< picPath_back <<"\033[0m\n";
	    bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, 32, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath);
	    std::cout << "\033[31mfront ==> "<< picPath <<"\033[0m\n";
	}
}

