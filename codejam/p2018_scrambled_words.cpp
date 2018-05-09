#include <iostream>
#include <string.h>
#include <stdlib.h>

#define CHAR_NUM 26
#define SMALL_START 97

using namespace std;

struct MatchWord {
	long length;
	char first;
	char last;	
	int matched[CHAR_NUM];

	bool passed;
};

int m_check[CHAR_NUM] = {0};

int work() {
	int word_num;

	cin >> word_num;
	MatchWord **words = (MatchWord**) malloc(sizeof(MatchWord*)*word_num);
	for (int i = 0; i < word_num; i++) {
		string word;
		cin >> word;
		MatchWord* m = (MatchWord*) malloc(sizeof(MatchWord));
		m->length = word.size();
		m->first = word[0];
		m->last = word[word.size()-1];
		m->passed = false;
		memset(m->matched, 0x00, sizeof(int)*CHAR_NUM);
		for (int j = 1; j < word.size()-1; j++) {
			m->matched[((int) word[j] - SMALL_START)]++;
		}
		words[i] = m;
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
	// input reading end !!!!!!!!!!!!!!!

	int count = 0;

	for (int i = 0; i < n; i++) {	
		for (int j = 0; j < word_num; j++) {	
			MatchWord *m = words[j];

			// already passed matcher
			if (m->passed) 
				continue;
			// length check
			if (i + m->length - 1 >= n)
				continue;
			// first check
			if (paper[i] != m->first) 
				continue;
			// last check
			if (paper[i + m->length -1] != m->last)
				continue;
			// middle check
			bool success = true;
			memset(m_check, 0x00, sizeof(int)*CHAR_NUM);
			for (int j = i+1; j < i + m->length-1; j++) {
				int s_idx = (int) paper[j] - SMALL_START;
				// failure1: no char in pattern
				if (m->matched[s_idx] == 0) {
					success = false;
					break;
				}
				m_check[s_idx]++;
			}
			for (int j = 0; j < CHAR_NUM; j++) {
				// failure2: match count not matched
				if (m_check[j] != m->matched[j]) {
					success = false;
					break;
				}
			}	

			if (success) {
				m->passed = true;
				count++;
			}
		}	
	}

	free(paper);
	for (int i = 0; i < word_num; i++) {
		free(words[i]);
	}
	free(words);

	return count;
}

int advanced() {
	int word_num;

	cin >> word_num;
	MatchWord *words = (MatchWord*) malloc(sizeof(MatchWord)*word_num);
	for (int i = 0; i < word_num; i++) {
		string word;
		cin >> word;
		words[i]->length = word.size();
		words[i]->first = word[0];
		words[i]->last = word[word.size()-1];
		memset(words[i]->matched, 0x00, sizeof(int)*CHAR_NUM);
		for (int j = 1; j < word.size()-1; j++) {
			words[i]->matched[((int) word[j] - SMALL_START)]++;
		}
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
	// input reading end !!!!!!!!!!!!!!!

	int count = 0;

	for (int i = 0; i < word_num; i++) {
		for (int idx = 0; idx < n; idx++) {
			// length check
			if (idx + words[i]->length - 1 >= n)
				continue;
			// first check
			if (paper[idx] != words[i]->first) 
				continue;
			// last check
			if (paper[idx + words[i]->length -1] != words[i]->last)
				continue;
			// middle check
			bool success = true;
			memset(m_check, 0x00, sizeof(int)*CHAR_NUM);
			for (int j = idx+1; j < idx + words[i]->length-1; j++) {
				int s_idx = (int) paper[j] - SMALL_START;
				// failure1: no char in pattern
				if (m->matched[s_idx] == 0) {
					success = false;
					break;
				}
				m_check[s_idx]++;
			}
			for (int j = 0; j < CHAR_NUM; j++) {
				// failure2: match count not matched
				if (m_check[j] != m->matched[j]) {
					success = false;
					break;
				}
			}	

			if (success) {
				m->passed = true;
				count++;
			}
		}
	}	

	for (int i = 0; i < n; i++) {	
		for (int j = 0; j < word_num; j++) {	
			
		}	
	}

	free(paper);
	for (int i = 0; i < word_num; i++) {
		free(words[i]);
	}
	free(words);

	return count;
}

int main() {
	ios::sync_with_stdio(false);
	
	int test_case;
	
	cin >> test_case;
	for (int i = 0; i < test_case; i++) {
		cout << "Case #" << i+1 << ": " << advanced() << endl;
	}
}
