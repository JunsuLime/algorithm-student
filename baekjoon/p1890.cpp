#include <iostream>
#include <vector>

#define MAX_ROW 100

using namespace std;

int board[MAX_ROW][MAX_ROW] = {0};
long long cached[MAX_ROW][MAX_ROW] = {0};
int n;

long long searchPath(int x, int y) {
    if (cached[x][y] != 0)
        return cached[x][y];
    if (x == n-1 && y == n-1)
        return 1;
    if (board[x][y] == 0)
        return 0;

    int nx, ny;
    long long path = 0;
    nx = x + board[x][y];
    ny = y;
    if (nx < n)
        path += searchPath(nx, ny);
    nx = x;
    ny = y + board[x][y];
    if (ny < n)
        path += searchPath(nx, ny);

    cached[x][y] = path;
    return path;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin >> n;

    int tmp = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }
    
    cout << searchPath(0, 0) << endl;

    return 0;
}
