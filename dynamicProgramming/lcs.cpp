#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(int argc, char const *argv[])
{
    string A,B;
    cin >> A;
    cin >> B;
    vector<vector<int> > k;

    vector<int> firstRow(B.length()+1,0);
    vector<int> otherRow(B.length()+1,0);
    k.push_back( firstRow );

    for (int i = 0; i < A.length(); ++i)
    {
        k.push_back(otherRow);
    }

    for (int i = 1; i <= A.length(); ++i)
    {
        for (int j = 1; j <= B.length(); ++j)
        {
            if (A[i] == B[j])
            {
                k[i][j] = 1 + k[i-1][j-1];
            }
            else
            {
                k[i][j] = max(k[i-1][j],k[i][j-1]);
            }
        }
    }

    for (int i = 1; i <= A.length(); ++i)
    {
        for (int j = 1; j <= B.length(); ++j)
        {
            cout << k[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
