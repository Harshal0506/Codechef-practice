#include <iostream>
using namespace std;

int main() {
    int n;
    cin>>n;
    while(n--)
    {
        int temp=0,temp1=0;
       string str;
       cin>>str;
       for(int i=0;i<str.length();i++)
       {
           if('a'==str[i])
                temp++;
            else if('b'==str[i])
                temp1++;
       }
       if(temp==temp1)
            cout<<temp1<<endl;
            
       
            
        else if(temp>temp1) 
            cout<<temp1<<endl;
        else
            cout<<temp<<endl;
    }
	return 0;
}
