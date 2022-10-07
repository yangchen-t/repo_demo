#include<iostream>
#include<vector>
using namespace std;

//vector的遍历

int main()
{
	vector<int> list_numbrs(3,1);
	vector<int> vec1(list_numbrs);
	vector<float> vec2(3);
	vector<char> vec3(3,'a');
	vector<char> vec4(vec3);
	cout << "vec1:" << endl;
	for (int i = 0; i < vec1.size(); i++ )
	{
		cout << vec1[i] << "";
	}
	cout << endl << "vec2:" << endl;
       for ( int i = 0; i < vec2.size(); i++ )
       {
	       cout << vec2[i] << "";
       }
 	cout <<endl << "vec3:" << endl;
 	for ( int i = 0; i < vec3.size(); i++)
	{
		vec4.pop_back();
		cout << vec3[i] << "";
		vec4.push_back('s');
		break;
	}
	cout << endl << "vec4:" << endl;
	for (int i = 0; i < vec4.size() ; i++ )
	{
		cout << vec4[i] << "";
	}
	cout << endl;
	return 0 ;
}


