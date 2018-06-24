#include <stdio.h>
#include <set>
#include <algorithm>

#define REMOVED -1

using namespace std;

void solve() {
    int n, k;
    scanf("%d", &n);
    scanf("%d", &k);
   
    set<int> player_set;
    for (int i = 0; i < n; i++) {
        int tmp;
        scanf("%d", &tmp);
        player_set.insert(tmp);
    }

    int bus_cnt = 0;
    int remove_cnt = 0;

    while(!player_set.empty()) {
        ++bus_cnt;

        set<int>::iterator p_iter = player_set.begin();
        int base_player = *p_iter;
        player_set.erase(p_iter);
        
        while (true) {
            p_iter = player_set.lower_bound(base_player + k + 1);
            if (p_iter != player_set.end()) {
                base_player = *p_iter;
                player_set.erase(p_iter);
            }
            else {
                break;
            }
        }
    }
    
    printf("%d\n", bus_cnt);
}

int main(int argc, char** argv)
{
    setbuf(stdout, NULL);

	int test_case;
    scanf("%d", &test_case);

    for(int i = 0; i < test_case; i++)
	{
		// Print the answer to standard output(screen).
        printf("Case #%d\n", i+1);
		solve();
	}

	return 0;//Your program should return 0 on normal termination.
}
