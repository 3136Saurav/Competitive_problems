/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
*/

#include<bits/stdc++.h>
#include<iostream>
using namespace std;

bool sumUp(int arr[], int n, int k)
{
  int sum = 0;
  int temp = 0;
  for(int i=0; i<n; i++)
  {
    sum = 0;
    temp = arr[i];
    for(int j=0; j<n; j++)
    {
      sum = temp + arr[j];
      if(sum == k)
      {
        return true;
      }
      sum = 0;
    }
  }
  return false;
}


int main()
{
  int arr[] = {10, 15, 3, 7};
  int n = sizeof(arr)/sizeof(arr[0]);
  int k = 2;
  if(sumUp(arr, n, k))
  {
    cout << "YES" << '\n';
  }
  else
  {
    cout<<"NO"<<'\n';
  }

  return 0;
}
