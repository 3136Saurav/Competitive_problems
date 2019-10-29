/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
*/

#include<bits/stdc++.h>
#include<iostream>
using namespace std;

bool ifExists(int arr[], int n, int t)
{
  for(int i=0; i<n; i++)
  {
    if(arr[i]==t)
    {
      return true;
    }
  }
  return false;
}

bool sumUp(int arr[], int n, int k)
{
  int temp = 0;
  bool check = false;
  for(int i=0; i<n; i++)
  {
    temp = k - arr[i];
    if(ifExists(arr, n, temp))
    {
      return true;
    }
  }
  return false;
}


int main()
{
  int arr[] = {10, 15, 3, 7};
  int n = sizeof(arr)/sizeof(arr[0]);
  int k = 17;
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
