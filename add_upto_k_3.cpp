/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
*/

#include<bits/stdc++.h>
#include<iostream>
using namespace std;

bool sumUp(int arr[], int n, int k)
{
  map<int, bool> comp;
  int temp;
  for(int i=0; i<n; i++)
  {
    if(comp[arr[i]])
    {
      return true;
    }
    else{
      temp = k - arr[i];
      comp[temp] = true;
    }
  }
  return false;
}

int main()
{
  int arr[] = {10, 15, 3, 7, 1};
  int n = sizeof(arr)/sizeof(arr[0]);
  int k = 4;
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
