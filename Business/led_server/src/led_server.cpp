#include <memory>
#include <iostream>
#include <string>
#include <stdio.h>
#include <time.h>
#include <fstream>
#include <sstream>
#include <unistd.h>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/u_int8.hpp"

#include "led_server/Obasic_types.h"
#include "led_server/bx_dual_sdk.h"
#include "led_server/bx_sdk_dual.h"

using std::placeholders::_1;

#define LEFT 52
#define RIGHT 53

class ControlParam
{
public:
	Ouint8 *f_ip;
	Ouint8 *r_ip;
	Ouint32 port;
	E_ScreenColor_G56 color;
	int uAreaId;
	int uAreaX;
	int uAreaY;
	int uWidth;
	int uHeight;
	EQpageHeader_G6 pheader1;
	Ouint8 *f_PicPath;
	Ouint8 *r_PicPath;
};

const std::string PICTURES = "/opt/qomolo/utils/led_server/pic/";

std::string GetQomoloRobotID()
{
    return std::string(getenv("QOMOLO_ROBOT_ID"));
}

// Get current date/time, format is YYYY-MM-DD.HH:mm:ss
const std::string currentDateTime()
{
    time_t     now = time(0);
    struct tm  tstruct;
    char       buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%Y-%m-%d.%X", &tstruct);
    return buf;
}

class LedServer : public rclcpp::Node
{
public:
	LedServer() : Node("led_server_sub_node")
	{
		subscription_ = this->create_subscription<std_msgs::msg::UInt8>(
			"/" + GetQomoloRobotID() + "/agent/led_display", 10, std::bind(&LedServer::topic_callback, this, _1));
	}
	static void led_server(Ouint8 *pic_path, const std_msgs::msg::UInt8::SharedPtr msg);

private:
	void topic_callback(const std_msgs::msg::UInt8::SharedPtr msg) const
	{
		std::string path = PICTURES + std::to_string(msg->data) + ".png";
		Ouint8 *pic_path = (unsigned char *)path.c_str();
		this->led_server(pic_path, msg);
	}
	rclcpp::Subscription<std_msgs::msg::UInt8>::SharedPtr subscription_;
};

void LedServer::led_server(Ouint8 *pic_path, const std_msgs::msg::UInt8::SharedPtr msg)
{
    std::cout << currentDateTime() << ":recv -> " << (int)msg->data << std::endl;
	ControlParam config;
    config.f_ip = (Ouint8 *)"192.168.112.11";
	config.r_ip = (Ouint8 *)"192.168.112.12";
	config.port = 5005;
	config.color = eSCREEN_COLOR_DOUBLE;
	config.uAreaId = 0;
	config.uAreaX = 32;
	config.uAreaY = 0;
	config.uWidth = 64;
	config.uHeight = 32;
	config.pheader1.PageStyle = 0x00;
	config.pheader1.DisplayMode = 0x02;
	config.pheader1.ClearMode = 0x01;
	config.pheader1.Speed = 20;
	config.pheader1.StayTime = 10;
	config.pheader1.RepeatTime = 3;
	config.pheader1.ValidLen = 128;
	config.pheader1.CartoonFrameRate = 0x00;
	config.pheader1.BackNotValidFlag = 0x00;
	config.pheader1.arrMode = eMULTILINE; // eSINGLELINE
	config.pheader1.fontSize = 12;
	config.pheader1.color = E_Color_G56::eRED;
	config.pheader1.fontBold = false;
	config.pheader1.fontItalic = false;
	config.pheader1.tdirection = pNORMAL;
	config.pheader1.txtSpace = 0;
	config.pheader1.Valign = 0;
	config.pheader1.Halign = 0;
    switch ((int)msg->data)
    {
    case LEFT:
    	config.f_PicPath = (unsigned char *)(PICTURES + "52.png").c_str();
		config.r_PicPath = (unsigned char *)(PICTURES + "53.png").c_str();
        break;
    case RIGHT:
    	config.f_PicPath = (unsigned char *)(PICTURES + "53.png").c_str();
		config.r_PicPath = (unsigned char *)(PICTURES + "52.png").c_str();
        break;
    default:
	    config.f_PicPath = pic_path;
	    config.r_PicPath = pic_path;
        break;
    }

    std::cout << currentDateTime() << ":front -> " << bxDual_dynamicArea_AddAreaPic_6G(
        config.f_ip, config.port, config.color,
        config.uAreaId, config.uAreaX, config.uAreaY, 
        config.uWidth, config.uHeight, &config.pheader1, 
        config.f_PicPath
    ) << std::endl;
    std::cout << currentDateTime() << ":rear -> " << bxDual_dynamicArea_AddAreaPic_6G(
        config.r_ip, config.port, config.color,
        config.uAreaId, config.uAreaX, config.uAreaY, 
        config.uWidth, config.uHeight, &config.pheader1, 
        config.r_PicPath
    ) << std::endl;
}

int main(int argc, char *argv[])
{
	rclcpp::init(argc, argv);
	rclcpp::spin(std::make_shared<LedServer>());
	rclcpp::shutdown();
	return 0;
}
