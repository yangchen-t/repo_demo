#include <iostream>
#include <cstring>

using namespace std;
void printBook(struct Books &b);

struct Books
{
   char  title[50];
   char  author[50];
   char  subject[100];
   int   book_id;
};

int main( )
{
   struct Books Book1;        
   struct Books Book2;      

   strcpy( Book1.title, "Learn C++ Programming");
   strcpy( Book1.author, "Chand Miyan");
   strcpy( Book1.subject, "C++ Programming");
   Book1.book_id = 6495407;

   strcpy( Book2.title, "Telecom Billing");
   strcpy( Book2.author, "Yakit Singha");
   strcpy( Book2.subject, "Telecom");
   Book2.book_id = 6495700;

   // 通过传 Book1 的地址来输出 Book1 信息
   printBook(Book1);
   printBook(Book2);

   return 0;
}

// 该函数以结构指针作为参数
void printBook(struct Books &b )
{
   cout << "Book title : " << b.title <<endl;
   cout << "Book author : " << b.author <<endl;
   cout << "Book subject : " << b.subject <<endl;
   cout << "Book id : " << b.book_id <<endl;
}
