#include<iostream>
using namespace std;
int main () {
    int n;
    cout<<"Enter number of elements: ";
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    cout<<"reverse of given array is: "<<endl;
    for(int i=n-1;i>=0;i--){
        cout<<arr[i]<<" ";
    }
} 