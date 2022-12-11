#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

#include "bx_dual_sdk.h"
#include "bx_sdk_dual.h"


using namespace std;

void gettime();
void turn_picture_display(int);

int main(int argc, char** argv)
{
	ifstream inFile("numbers.csv", ios::in);
    Ouint8* picPath;
    Ouint8* picPath_back;
	stringstream stream;
	string num;
	int n ;
    while (getline(inFile, num))
	{
	stream << num;
	stream >> n;
	switch (n){
		case 1 :
			picPath = (Ouint8*)("/scripts/pic/1.png");
			break;
		case 2 :
			picPath = (Ouint8*)("/scripts/pic/2.png");
			break;
		case 3 :
		    picPath = (Ouint8*)("/scripts/pic/3.png");
		    break;
        case 4 :
            picPath = (Ouint8*)("/scripts/pic/4.png");
            break;
        case 5 :
            picPath = (Ouint8*)("/scripts/pic/5.png");
            break;
        case 6 :
                        picPath = (Ouint8*)("/scripts/pic/6.png");
                        break;
                case 7 :
                        picPath = (Ouint8*)("/scripts/pic/7.png");
                        break;
                case 8 :
                        picPath = (Ouint8*)("/scripts/pic/8.png");
                        break;
                case 9 :
                        picPath = (Ouint8*)("/scripts/pic/9.png");
                        break;
                case 10 :
                        picPath = (Ouint8*)("/scripts/pic/10.png");
                        break;
                case 11 :
                        picPath = (Ouint8*)("/scripts/pic/11.png");
                        break;
                case 12 :
                        picPath = (Ouint8*)("/scripts/pic/12.png");
                        break;
                case 13 :
                        picPath = (Ouint8*)("/scripts/pic/13.png");
                        break;
                case 14 :
                        picPath = (Ouint8*)("/scripts/pic/14.png");
                        break;
                case 15 :
                        picPath = (Ouint8*)("/scripts/pic/15.png");
                        break;
                case 16 :
                        picPath = (Ouint8*)("/scripts/pic/16.png");
                        break;
                case 17 :
                        picPath = (Ouint8*)("/scripts/pic/17.png");
                        break;
                case 18 :
                        picPath = (Ouint8*)("/scripts/pic/18.png");
                        break;
                case 19 :
                        picPath = (Ouint8*)("/scripts/pic/19.png");
                        break;
                case 20 :
                        picPath = (Ouint8*)("/scripts/pic/20.png");
                        break;
                case 21 :
                        picPath = (Ouint8*)("/scripts/pic/21.png");
                        break;
                case 22 :
                        picPath = (Ouint8*)("/scripts/pic/22.png");
                        break;
                case 23 :
                        picPath = (Ouint8*)("/scripts/pic/23.png");
                        break;
                case 24 :
                        picPath = (Ouint8*)("/scripts/pic/24.png");
                        break;
                case 25 :
                        picPath = (Ouint8*)("/scripts/pic/25.png");
                        break;
                case 26 :
                        picPath = (Ouint8*)("/scripts/pic/26.png");
                        break;
                case 27 :
                        picPath = (Ouint8*)("/scripts/pic/27.png");
                        break;
                case 28 :
                        picPath = (Ouint8*)("/scripts/pic/28.png");
                        break;
                case 29 :
                        picPath = (Ouint8*)("/scripts/pic/29.png");
                        break;
                case 30 :
                        picPath = (Ouint8*)("/scripts/pic/30.png");
                        break;
                case 31 :
                        picPath = (Ouint8*)("/scripts/pic/31.png");
                        break;
                case 32 :
                        picPath = (Ouint8*)("/scripts/pic/32.png");
                        break;
                case 33 :
                        picPath = (Ouint8*)("/scripts/pic/33.png");
                        break;
                case 34 :
                        picPath = (Ouint8*)("/scripts/pic/34.png");
                        break;
                case 35 :
                        picPath = (Ouint8*)("/scripts/pic/35.png");
                        break;
                case 36 :
                        picPath = (Ouint8*)("/scripts/pic/36.png");
                        break;
                case 37 :
                        picPath = (Ouint8*)("/scripts/pic/37.png");
                        break;
                case 38 :
                        picPath = (Ouint8*)("/scripts/pic/38.png");
                        break;
                case 39 :
                        picPath = (Ouint8*)("/scripts/pic/39.png");
                        break;
		        case 40 :
                        picPath = (Ouint8*)("/scripts/pic/40.png");
                        break;
                case 41 :
                        picPath = (Ouint8*)("/scripts/pic/41.png");
                        break;
                case 42 :
                        picPath = (Ouint8*)("/scripts/pic/42.png");
                        break;
                case 43 :
                        picPath = (Ouint8*)("/scripts/pic/43.png");
                        break;
                case 44 :
                        picPath = (Ouint8*)("/scripts/pic/44.png");
                        break;
                case 45 :
                        picPath = (Ouint8*)("/scripts/pic/45.png");
                        break;
                case 46 :
                        picPath = (Ouint8*)("/scripts/pic/46.png");
                        break;
                case 47 :
                        picPath = (Ouint8*)("/scripts/pic/47.png");
                        break;
                case 48 :
                        picPath = (Ouint8*)("/scripts/pic/48.png");
                        break;
                case 49 :
                        picPath = (Ouint8*)("/scripts/pic/49.png");
                        break;
                case 50 :
                        picPath = (Ouint8*)("/scripts/pic/50.png");
                        break;
                case 51 :
                        picPath = (Ouint8*)("/scripts/pic/51.png");
                        break;
                case 54 :
                        picPath = (Ouint8*)("/scripts/pic/54.png");
                        break;
                case 55 :
                        picPath = (Ouint8*)("/scripts/pic/55.png");
                        break;
                case 56 :
                        picPath = (Ouint8*)("/scripts/pic/56.png");
                        break;
                case 57 :
                        picPath = (Ouint8*)("/scripts/pic/57.png");
                        break;
                case 58 :
                        picPath = (Ouint8*)("/scripts/pic/58.png");
                        break;
                case 59 :
                        picPath = (Ouint8*)("/scripts/pic/59.png");
                        break;
                case 60 :
                        picPath = (Ouint8*)("/scripts/pic/60.png");
                        break;
                case 61 :
                        picPath = (Ouint8*)("/scripts/pic/61.png");
                        break;
                case 62 :
                        picPath = (Ouint8*)("/scripts/pic/62.png");
                        break;
                case 63 :
                        picPath = (Ouint8*)("/scripts/pic/63.png");
                        break;
                case 64 :
                        picPath = (Ouint8*)("/scripts/pic/64.png");
                        break;
                case 65 :
                        picPath = (Ouint8*)("/scripts/pic/65.png");
                        break;
                case 66 :
                        picPath = (Ouint8*)("/scripts/pic/66.png");
                        break;
                case 67 :
                        picPath = (Ouint8*)("/scripts/pic/67.png");
                        break;
                case 68 :
                        picPath = (Ouint8*)("/scripts/pic/68.png");
                        break;	
	}

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
	    cout << picPath << endl;
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

        gettime();
        if (n == 52){
                turn_picture_display(1);
        }
        else if (n == 53){
                turn_picture_display(2);
        }
//api
        else {
   	        bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath);
	        cout << "\033[31mfront ==> "<< picPath <<"\033[0m\n" ;
	        bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath);
	        cout << "\033[31mrear ==> "<< picPath <<"\033[0m\n";
    	}
}
	return 0;
}

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

void turn_picture_display(int mode){
        //config
	Ouint8* picPath;
    Ouint8* picPath_back;
	Ouint8* pIP = (Ouint8*)"192.168.112.11";
    Ouint8* pIP_back = (Ouint8*)"192.168.112.12";
	Ouint32 nPort = 5005;
	picPath = (Ouint8*)("/scripts/pic/52.png");
	picPath_back = (Ouint8*)("/scripts/pic/53.png");
	E_ScreenColor_G56 color = eSCREEN_COLOR_DOUBLE;
    int uAreaId = 0;
    int uAreaX = 16;//32
    int uAreaY = 0;
    int uWidth = 64;
    int uHeight = 32;

//EQpageHeader_G6
    EQpageHeader_G6 pheader1;
    pheader1.PageStyle = 0x00;
   	pheader1.DisplayMode = 0x07;    //0x00 –随机显示 0x01 –静止显示 0x02 –快速打出 0x03 –向左移动 0x04 –向左连移 0x05 –向上移动 0x06 –向上连移 0x07 –闪烁
    pheader1.ClearMode = 0x01;
    pheader1.Speed = 40;
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
	// del pic
//	bxDual_dynamicArea_DelArea_6G(pIP, nPort, 0xff);

	if (mode == 1){
        bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, 32, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath);
        cout << "\033[31mfront ==> "<< picPath <<"\033[0m\n";
	    bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, 32, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath_back);
        cout << "\033[31mrear ==> "<< picPath_back <<"\033[0m\n";
	}else if (mode == 2 ){
	    bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, 32, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath);
	    cout << "\033[31mrear ==> "<< picPath_back <<"\033[0m\n";
	    bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, 32, uAreaY, uWidth, uHeight, &pheader1, (Ouint8*)picPath_back);
	    cout << "\033[31mfront ==> "<< picPath <<"\033[0m\n";
	}   
}

