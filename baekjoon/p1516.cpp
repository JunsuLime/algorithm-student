#include <stdio.h>
#include <queue>

#define MAX_S 501

using namespace std;

vector<int> graph[MAX_S];
int self_time[MAX_S] = {0};
int total_time[MAX_S] = {0};

struct Node {
	int time, id;
};

bool operator<(Node a, Node b) {
	return a.time < b.time;
}

priority_queue<Node> q;

int main() {
	int s_num;
	scanf("%d\n", &s_num);

	for (int i = 1; i < s_num+1; i++) {
		int e;
		scanf("%d", &e);
		self_time[i] = e;
		total_time[i] = e;

		bool only_one = true;
		while (true) {
			scanf("%d", &e);
			if (e == -1) 
				break;
			graph[e].push_back(i);
			only_one = false;
		}
		if (only_one) {
			q.push(Node{total_time[i], i});
		}
			
	}
	
	while (!q.empty()) {
		Node n = q.top();
		q.pop();
		int time = n.time;
		int cur = n.id;

		int length = graph[cur].size();
		for (int i = 0; i < length; i++) {
			int branch = graph[cur][i];
			if (time + self_time[branch] > total_time[branch]) {
				total_time[branch] = time + self_time[branch];
				q.push(Node{total_time[branch], branch});
			}
		}
	}

	for (int i = 1; i < s_num+1; i++) {
		printf("%d\n", total_time[i]);
	}

	return 0;
}

