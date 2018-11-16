#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
	int N,w,V1,W1;

	vector< vector<int> > k;
	vector<int> V, W;

	cin >> N >> w;
	V.push_back(-1);
	W.push_back(-1);

	for (int i = 0; i < N; ++i)
	{
		cin >> V1 >> W1;
		V.push_back(V1);
		W.push_back(W1);
	}

	vector<int> firstRow(w+1,0);
	vector<int> otherRow(w+1,0);
	k.push_back( firstRow );

	for (int i = 0; i < N; ++i)
	{
		k.push_back(otherRow);
	}

	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= w; ++j)
		{
			if ( W[i] <= j )
			{
				k[i][j] = max( k[i-1][j], k[i-1][j - W[i]] + V[i] );
			}
		}
	}

	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= w; ++j)
		{
			cout << k[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}
