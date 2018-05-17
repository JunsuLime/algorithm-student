#include <iostream>
#include <queue>

#define D_NUM 6

#define GOOD 1
#define NOT_YET 0
#define EMPTY -1

using namespace std;

int direction[D_NUM][3] = {
    {1, 0, 0}, {0, 0, 1}, {0, 1, 0}, {-1, 0, 0}, {0, -1, 0}, {0, 0, -1}
};

struct Location {
    int m, n, h;

    Location(int _h, int _n, int _m) {
        m = _m;
        n = _n;
        h = _h;
    }
};

int main() {
    ios_base::sync_with_stdio(false);

    int m, n, h;

    cin >> m >> n >> h;

    queue<Location> q;
    int tomato_box[h][n][m];
    int remained = 0;

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < m; k++) {
                int tomato;
                cin >> tomato;
                if (tomato == GOOD) {
                    q.push(Location(i, j, k));
                }
                else if (tomato == NOT_YET) {
                    remained++;
                }

                tomato_box[i][j][k] = tomato;
            }
        }
    }

    q.push(Location(-1, -1, -1));
    int depth = -1;
    while (1) {
        Location l = q.front();
        q.pop();

        if (l.m == -1) {
            depth++;
            if (q.empty()) {
                break;
            }
            q.push(Location(-1, -1, -1));
            l = q.front();
            q.pop();
        }
        
        for (int i = 0; i < D_NUM; i++) {
            int n_h, n_n, n_m;
            n_h = l.h + direction[i][0];
            n_n = l.n + direction[i][1];
            n_m = l.m + direction[i][2];

            if (!(n_h >= 0 && n_h < h && n_n >= 0 && n_n < n && n_m >= 0 && n_m < m)) {
                continue;
            }

            if (tomato_box[n_h][n_n][n_m] == NOT_YET) {
                tomato_box[n_h][n_n][n_m] = GOOD;
                remained--;
                q.push(Location(n_h, n_n, n_m));
            }
        }
    }

    if (remained == 0) {
        cout << depth << endl;
    }
    else {
        cout << -1 << endl;
    }
}
