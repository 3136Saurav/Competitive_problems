#include <iostream>
using namespace std;

void sub_sum(int arr[], int n, int key);

void sub_sum(int arr[], int n, int key)
{
    bool found = false;
    for(int s=0; s<n; s++)
    {
        int sum = 0;
        found = false;
        for(int e=s; e<n; e++)
        {
            sum += arr[e];
            if(sum==key)
            {
                found = true;
                cout<<s+1<<" "<<e+1<<endl;

            }
            if (found == true)
            {
                return;
            }
        }
    }
    if (found == false)
    {
        cout<<"-1"<<endl;
        return;
    }

}

int main()
{
    int t, n, s;

    cin>>t;
    for(int i=0; i<t; i++)
        {
            cin>>n>>s;
            int arr[n];

            for(int j=0; j<n; j++)
            {
                cin>>arr[j];
            }

            sub_sum(arr, n, s);
        }

    return 0;
}
