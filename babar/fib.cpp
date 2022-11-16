// #include<iostream>
// using namespace std;

// int fib(int n) {
//     int a= 0;
//     int b=1;
//     // int nextNumber;
//     cout<<a<<" "<<b<<" ";
//     for (int i =1;i<=(n-2);i++){
//         int nextNumber = a + b;
//         cout<<nextNumber<<" ";
//         a = b;
//         b = nextNumber;
//     }
// }

// int main () {
//     int n;
//     cout<<"ENter the length : "<<endl;
//     cin>>n;
//     fib(n);
// }


#include<iostream>
using namespace std;
int fib(int n){
    int a=0;
    int b=1;
    cout<<a<<" "<<b<<" ";
    for(int i=1;i<=(n-2);i++){
        int nextnumber = a+b;
        cout<<nextnumber<<" ";
        a = b;
        b = nextnumber;
    }
}
int main () {
    int n;
    cout<<"Enter the length: ";
    cin>>n;
    fib(n);
}