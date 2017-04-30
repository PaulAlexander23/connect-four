#include<iostream>
#include<array>

using namespace std;

void display(array<int, 42> board)
{
	for (int i = 0; i < 6; i++)
	{
		for (int j = 0; j < 7; j++)
		{


			if (board.at(j + 7*i)== 1)
				cout << " x ";
			else if (board.at(j + 7 * i) == 2)
				cout << " o ";
			else
				cout << "   ";
			
			if (j != 6)
			{
				cout << "|";
			}
		}
		cout << "\n";
	}

}


int main()
{
	cout << "Connect 4 with Ai" << endl;

	array<int, 42> board;
	board.fill(0);

	display(board);
	/*for (const auto& s : board)
		cout << s << "\n";*/

	bool end = false;
	int pmove = 0;
	
	/*while (!end)
	{
		cout << "Enter your move: ";
		cin >> pmove;
		//Check ok.
		display(board)

	}*/
	

	return 0;
}