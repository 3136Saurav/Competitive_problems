#include<iostream>
using namespace std;

int gcd(int a, int b)
{
  if (b == 0)
  {
    return a;
  }
  return gcd(b, a%b);
}

void leftRotate(int arr[], int n, int k)
{
  //int j, temp, d;
  int sets = gcd(n, k);
  for(int i=0; i<sets; i++)
  {
    int j = i;
    int temp = arr[i];
    int d = -1;
    while(true)
    {
      d = (j + k)%n;
      if(d == i)
      {
        break;
      }
      arr[j] = arr[d];
      j = d;
    }
    arr[j] = temp;
  }
}

void rightRotateByOne(int arr[], int n)
{
  int temp = arr[n-1];
  int i;
  for (int i=n-1; i>0; i--)
  {
    arr[i] = arr[i-1];
  }
  arr[0] = temp;
}

void rightRotate(int arr[], int n, int k)
{
    int i;
    for(int i=1; i<=k; i++)
    {
      rightRotateByOne(arr, n);
    }
}

void printArray(int arr[], int n)
{
  for(int i=0; i<n; i++)
  {
    cout<<arr[i]<<" ";
  }
}

int main()
{
  int arr[] = {1,2,3,4,5,6};
  int n = sizeof(arr)/sizeof(arr[0]);
  printArray(arr, n);
  cout<<endl;
  leftRotate(arr, n, 2);
  rightRotate(arr, n, 2);
  cout<<"\n";
  printArray(arr, n);
}
