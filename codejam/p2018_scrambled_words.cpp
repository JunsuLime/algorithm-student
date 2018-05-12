#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <vector>
#include <map>

#define CHAR_NUM 26
#define SMALL_START 97

using namespace std;

struct MatchWord {
	char first;
	char last;	
	int matched[CHAR_NUM];
};

bool is_matched(int* m1, int* m2) {
    for (int i = 0; i < CHAR_NUM; i++) {
        if (m1[i] != m2[i]) {
            return false;
        }
    }
    return true;
}


int work() {

    /* read input */
	int word_num;
	cin >> word_num;

    map<int, vector<MatchWord> > word_map;
	for (int i = 0; i < word_num; i++) {
		string word;
		cin >> word;
		
        MatchWord m;
        int word_length = word.size();
		m.first = word[0];
		m.last = word[word.size()-1];
		memset(m.matched, 0x00, sizeof(int)*CHAR_NUM);
		for (int j = 0; j < word.size(); j++) {
			m.matched[((int) word[j] - SMALL_START)]++;
		}
        word_map[word_length].push_back(m);
	}

	char s1, s2;
	cin >> s1 >> s2;

	int n, a, b, c, d;
	cin >> n >> a >> b >> c >> d;

	char* paper = (char*) malloc(sizeof(char)*n);
	paper[0] = s1;
	paper[1] = s2;

	long ppx = paper[0];
	long px = paper[1];

	for (int i = 2; i < n; i++) {
		int x = (a*px + b*ppx + c) % d;
		paper[i] = (char) (SMALL_START + (x % CHAR_NUM));

		ppx = px;
		px = x;
	}
    /* read input end */

    cout << "work!!" << endl;
    /* work */
	int count = 0;
    map<int, vector<MatchWord> >::iterator iter;
    int* matcher = (int*) malloc(sizeof(int)*CHAR_NUM);

    for (iter = word_map.begin(); iter != word_map.end(); iter++) {
        int length = iter->first;
        vector<MatchWord> words = iter->second;

        // 1) make length l window
        int i = 0;
        memset(matcher, 0x00, sizeof(int)*CHAR_NUM);
        for (i = 0; i < length; i++) {
            matcher[paper[i]-SMALL_START]++;
        }

        // 2) start window sliding
        for (; i < n; i++) {
            // match with matcher
            int cur = 0;
            int swapped = words.size();
            while (cur != swapped) {
                MatchWord m = words[cur];

                if (paper[i-length] == m.first 
                    && paper[i-1] == m.last
                    && is_matched(m.matched, matcher)) {

                    count++;
                    swapped--;

                    // swap item1 and item2
                    MatchWord tmp = words[cur];
                    words[cur] = words[swapped];
                    words[swapped] = tmp;
                }
                else {
                    cur++;
                }
            }
            // remove alreay matched words
            words.erase(words.begin()+cur, words.end());

            // slide...
            matcher[paper[i-length]-SMALL_START]--;
            matcher[paper[i]-SMALL_START]++;
        }
    }

    free(matcher);
	free(paper);
	return count;
}


int main() {
	ios::sync_with_stdio(false);
	
	int test_case;
	
	cin >> test_case;
	for (int i = 0; i < test_case; i++) {
		cout << "Case #" << i+1 << ": " << work() << endl;
	}
}
