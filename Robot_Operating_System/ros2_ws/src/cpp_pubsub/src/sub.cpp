#include <memory>
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <unistd.h>
#include "rclcpp/rclcpp.hpp"

#include "interfaces/msg/num.hpp" // CHANGE
// #include "std_msgs/msg/string"

#include "cpp_pubsub/get_info.h"


using std::placeholders::_1;
class MinimalSubscriber : public rclcpp::Node
{
public:
    MinimalSubscriber(): Node("test_led_sub_node")
    {
        subscription_ = this->create_subscription<interfaces::msg::Num>( 
            "led_topic", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
    }
    static int led_server(Ouint8 *pic_path, const interfaces::msg::Num::SharedPtr msg);


private:
    void topic_callback(const interfaces::msg::Num::SharedPtr msg) const
    {
        gettime();
        path_select pl;
        pl.path = "/debug/test" + std::to_string(msg->num) + ".png";
        Ouint8 * realPath = (unsigned char *)pl.path.c_str();
        std::cout << realPath << std::endl;
        this->led_server(this->realpath, this->msg);
    }
    rclcpp::Subscription<interfaces::msg::Num>::SharedPtr subscription_;  
};



int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MinimalSubscriber>());
    rclcpp::shutdown();
    return 0;
}


int MinimalSubscriber::led_server(Ouint8 *pic_path, const interfaces::msg::Num::SharedPtr msg)
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
    if (msg->num == 52)
    {
        turn_picture_display(msg->num);
    }
    else if (msg->num == 53)
    {
        turn_picture_display(msg->num);
    }else {
        Ouint8 * pic_path = TypeConversion(p.path);
        bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, pic_path);
        std::cout << "\033[31mfront ==> "<< p.path <<"\033[0m\n" ;
        bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, pic_path);
        std::cout << "\033[31mrear ==> "<< p.path <<"\033[0m\n";
    }
    return 0;
}
	

