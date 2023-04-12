#include <memory>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <unistd.h>
#include "rclcpp/rclcpp.hpp"

// #include "interfaces/msg/num.hpp" // CHANGE

#include "std_msgs/msg/u_int8.hpp"

#include "cpp_pubsub/get_info.h"

std::string GetEnv()
{
	char *Robot;
	if (Robot = getenv("QOMOLO_ROBOT_ID"))
	{
		std::string ROBOT_ID = Robot;
		return ROBOT_ID;
	}
	else
	{
		std::cout << "robot_id is empty" << std::endl;
	}
}

using std::placeholders::_1;
class MinimalSubscriber : public rclcpp::Node
{
public:
	MinimalSubscriber() : Node("led_server_sub_node")
	{
		subscription_ = this->create_subscription<std_msgs::msg::UInt8>(
			"/" + GetEnv() + "/agent/led_display", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
	}
	static int led_server(Ouint8 *pic_path, const std_msgs::msg::UInt8::SharedPtr msg);

private:
	void topic_callback(const std_msgs::msg::UInt8::SharedPtr msg) const
	{
		gettime();
		path_select pl;
		pl.path = "/opt/qomolo/utils/led_server/pic/" + std::to_string(msg->data) + ".png";
		Ouint8 *pic_path = (unsigned char *)pl.path.c_str();
		this->led_server(pic_path, msg);
	}
	rclcpp::Subscription<std_msgs::msg::UInt8>::SharedPtr subscription_;
};

int main(int argc, char *argv[])
{
	rclcpp::init(argc, argv);
	rclcpp::spin(std::make_shared<MinimalSubscriber>());
	rclcpp::shutdown();
	return 0;
}

int MinimalSubscriber::led_server(Ouint8 *pic_path, const std_msgs::msg::UInt8::SharedPtr msg)
{
	int left = 52;
	int right = 53;
	Ouint8 *pIP = (Ouint8 *)"192.168.112.11";
	Ouint8 *pIP_back = (Ouint8 *)"192.168.112.12";
	Ouint32 nPort = 5005;

	// config
	E_ScreenColor_G56 color = eSCREEN_COLOR_DOUBLE;
	int uAreaId = 0;
	int uAreaX = 32;
	int uAreaY = 0;
	int uWidth = 64;
	int uHeight = 32;

	// EQpageHeader_G6
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
	pheader1.arrMode = eMULTILINE; // eSINGLELINE
	pheader1.fontSize = 12;
	pheader1.color = E_Color_G56::eRED;
	pheader1.fontBold = false;
	pheader1.fontItalic = false;
	pheader1.tdirection = pNORMAL;
	pheader1.txtSpace = 0;
	pheader1.Valign = 0;
	pheader1.Halign = 0;
	if (msg->data == left)
	{
		turn_picture_display(msg->data);
	}
	else if (msg->data == right)
	{
		turn_picture_display(msg->data);
	}
	else
	{
		bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, pic_path);
		std::cout << "\033[31mfront ==> " << pic_path << "\033[0m\n";
		bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, pic_path);
		std::cout << "\033[31mrear ==> " << pic_path << "\033[0m\n";
	}
	return 0;
}

