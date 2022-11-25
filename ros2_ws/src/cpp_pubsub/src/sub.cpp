#include <memory>
#include <iostream>
#include <string>

#include "bx_dual_sdk.h"
#include "bx_sdk_dual.h"
#include "get_info.h"
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using std::placeholders::_1;

void gettime();

class MinimalSubscriber : public rclcpp::Node
{
  public:
    MinimalSubscriber()
    : Node("minimal_subscriber")
    {
      subscription_ = this->create_subscription<std_msgs::msg::String>(
      "display", 10, std::bind(&MinimalSubscriber::topic_callback, this, _1));
    }

  private:
    void topic_callback(const std_msgs::msg::String::SharedPtr msg) const
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

      // turn func
      if ((int)data.c_str() == 51)
      {
      	turn_picture_display((int)data.c_str());
      }
      else if ((int)data.c_str() == 52)
      {
      	turn+picture_display((int)data.c_str());
      }
      else
      {
	//other func 
   	bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, return_path((int)data.c_str()));
	cout << "\033[31mfront ==> "<< *return_path() <<"\033[0m\n" ;
	bxDual_dynamicArea_AddAreaPic_6G(pIP_back, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, &pheader1, return_path((int)data.c_str()));
	cout << "\033[31mrear ==> "<< *return_path() <<"\033[0m\n";
      }  
     rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<MinimalSubscriber>());
  rclcpp::shutdown();
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
