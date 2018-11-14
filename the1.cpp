#include <iostream>
#include <vector>

using namespace std;


int main(int argc, char const *argv[])
{
	int algoType, numOfBuildings,t1,t2,t3;
	cin >> algoType;
	cin >> numOfBuildings;
	vector<int> temp; 
	vector<int> heightMap(1000,0);
	vector< vector<int>  > buildings;

	for (int i = 0; i < numOfBuildings; ++i)
	{
		cin >> t1 >> t2 >> t3;
		temp.push_back( t1 );
		temp.push_back( t2 );
		temp.push_back( t3 );
		buildings.push_back(temp);
		temp.clear();
	}

	if (algoType == 0)
	{
		for (int i = 0; i < buildings.size(); ++i)
		{
			for (int j = buildings[i][0]; j<buildings[i][2]; ++j)
			{
				if (buildings[i][1] > heightMap[j])
				{
					heightMap[j] = buildings[i][1];
				}
			}
		}

		for (int i = 1; i < 1000; ++i)
		{
			if ( heightMap[i - 1] != heightMap[i] )
			{
				cout << i << " " << heightMap[i] << endl;
			}
		}
	}
	else
	{
		//TODO implement n*logn solution
	}

	return 0;
}