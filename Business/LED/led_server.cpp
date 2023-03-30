#include <stdio.h>
#include <string>
#include <fstream>
#include <sstream>
#include <unistd.h>

#include "get_info.h"




int main(int argc, char** argv)
{
	Ouint8* pIP = (Ouint8*)"192.168.112.11";
    Ouint8* pIP_back = (Ouint8*)"192.168.112.12";
	Ouint32 nPort = 5005;

	//config
	E_ScreenColor_G56 color = eSCREEN_COLOR_DOUBLE;
	int uAreaId = 0;
	int uAreaX = 32;
	int uAreaY = 0;
	int uWidth = 64;
	int uHeight = 32;

	//EQpageHeader_G6
	EQpageHeader_G6 pheader1;
	pheader1.PageStyle = 0x00;
   	pheader1.DisplayMode = 0x02;
	pheader1.ClearMode = 0x01;
	pheader1.Speed = 20;
	pheader1.StayTime = 10;
	pheader1.RepeatTime = 3;
	pheader1.ValidLen = 128;
	pheader1.CartoonFrameRate = 0x00;
	pheader1.BackNotValidFlag = 0x00;
	pheader1.arrMode = eMULTILINE; //eSINGLELINE
	pheader1.fontSize = 12;
	pheader1.color =E_Color_G56::eRED;
	pheader1.fontBold = false;
	pheader1.fontItalic = false;
	pheader1.tdirection = pNORMAL;
	pheader1.txtSpace = 0;
	pheader1.Valign = 0;
	pheader1.Halign = 0;

	path_select  p;
	while (true)
	{
		p = return_path();
		gettime();
		if (p.numbers == 52){
			turn_picture_display(1);
		}
		else if (p.numbers == 53){
			turn_picture_display(2);
		}else {
			Ouint8 * pic_path = TypeConversion(p.path);
			bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, pic_path);
			std::cout << "\033[31mfront ==> "<< p.path <<"\033[0m\n" ;
			bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, pic_path);
			std::cout << "\033[31mrear ==> "<< p.path <<"\033[0m\n";
		}
		return 0;
		sleep(1);
	}
}
	


