#include <iostream>
#include <fstream>
#include <string>
#include <typeinfo>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;


double getcsvdata();
double remote_to_local_pose(double);
double utm_to_local_pose(double);

const double remote_delta_x{565123.0};
const double remote_delta_y{4317123.0};
const double local_delta_x(4078390.0167294773 + 314.61);
const double local_delta_y{-1527665.1822423297 + 4.0};
const double local_rotation{1.3428834074238685};
const double theta{0.0};

const double local_tran_matrix[3][3]{
    {cos(local_rotation), -sin(local_rotation), local_delta_x},
    {sin(local_rotation), cos(local_rotation), local_delta_y},
    {0, 0, 1}
};


int main(int argc, char** argv)
{

    getcsvdata();
    cout << local_tran_matrix[0][1] << endl;  // real
    return 0;
}

double getcsvdata(){
    ifstream inFile("test.csv", ios::in);
	string lineStr;
	vector<vector<string>> strArray;
    getline(inFile, lineStr);
	while (getline(inFile, lineStr))
	{
		stringstream ss(lineStr);
		string str;
		// 按照逗号分隔
        for (int s = 0 ; s < 3; s++){
		    getline(ss, str, ',');
            double x{0}, y{0}, z{0};
            if (s == 0){
                x = stod(str);
                cout << "x = " << x << endl; 
            }else if(s == 1 ){
                y = stod(str);
                cout << "y = " <<  y << endl;
            }else if (s == 2){
                z = stod(str);
                cout << "z = " << z << endl;
            }else{
                cout << "not" << endl;
            }
            // return x, y, z;
	    } 
    } 
}

/* double utm_to_local_pose(double utm_pose_matrix){
    double local_pose_matrix{local_tran_matrix[3][3], utm_pose_matrix}

}

double remote_to_local_pose(double x, double y, double z){
    double utm_pose_matrix[3][3]{
        {cos(z), -sin(z), x + remote_delta_x},
        {sin(z), cos(z), y + remote_delta_y},
        {0, 0, 1}
    };
    double local_pose_matrix[3][3]{utm_to_local_pose(utm_pose_matrix[3][3])};
    double local_pose_x{local_pose_matrix[0][2]};
    double local_pose_y{local_pose_matrix[1][2]};
    double local_pose_theta{atan2(local_pose_matrix[1][0], local_pose_matrix[0][0])};
    return utm_pose_matrix;
} */