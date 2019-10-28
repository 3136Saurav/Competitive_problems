#include<bits/stdc++.h>
#include<iostream>

using namespace std;

int equilibrium_index(int arr[], int n)
{
  int i, j;
  for(int i=0; i<n; i++)
  {
    int left_sum=0;
    for(int j=0; j<i; j++)
    {
      left_sum = left_sum + arr[j];
    }
    int right_sum=0;
    for(int j=i+1; j<n; j++)
    {
      right_sum = right_sum + arr[j];
    }

    if(left_sum == right_sum)
    {
      return i;
    }
  }
  return -1;
}

int main() {

  int arr[] = {0, 1, 6 ,2, -1};
  int n = sizeof(arr)/sizeof(arr[0]);
  cout<<equilibrium_index(arr, n);
  return 0;

}
