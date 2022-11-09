// #include<iostream>
// using namespace std;
// int factorial (int n) {
//     if (n>1) {
//         return n*factorial(n-1);
//     }
//     else 
//         return 1;
// }
// int main () {
//     int n=6;
//     cout<<factorial(n);
// }
//----------------prime number------------------
// #include<iostream>
// using namespace std;
// int main () {
//     int n,i,count=0;
//     cout<<"Enter n: ";
//     cin>>n;
//     for(i=1;i<=n;i++) {
//         if(n%i==0) {
//             count++;
//         }
//         i++;
//     }
//     if(count=2) {
//         cout<<n<<" is prime number";
//     }
//     else {
//         cout<<n<<" is composite number";
//     }

//     return 0;
// }
// #include<iostream>
// using namespace std;
// int main () {
//     int n,sum=0;
//     cout<<"Enter n: ";
//     cin>>n;
//     for(int i=1;i<=n;i++) {
//         sum=sum+i;
//         cout<<i<<", ";
//     }
//     cout<<endl;
//     cout<<sum;
//     return 0;

// }

// #include<iostream>
// using namespace std;
// int main () {
//     int n,i;
//     for (i=0;i<=n;i++) {
//         for (int j=0;j<=i;j++){
//         cout<<"*";
//         }
//         cout<<endl;
//     }
//     return 0;
// }