/* cpp coding convention 및 restriction 정리
 * 
 * 사용 언어는 C++14 로 제한한다.
 *
 * 1) stdin, stdout
 * standard input output 은 iostream library 만 이용해서 함을 규칙으로 한다.
 * 빠른 in, out 을 위해 ios_base::sync_with_stdio(false) 를 반드시 써준다.
 * 
 * 2) naming convention
 *   모든 naming 은 모두가 알아들을 수 있게 쓰고, 되도록 약어는 지양하자.
 *   하지만 
 *   - 문제 내에 명시되어 있는 약어
 *   - 변수명 지정시 규칙으로 정한 약어
 *   - 원래대로 쓰면 너무 길어지는데 약어가 누구나 알 수 있다고 확신이 드는 경우
 *   는 코드를 짜는 사람의 판단에 맡긴다.
 *
 *   1 - function naming
 *     lowerCamelCase 를 기본으로 한다.
 *     (동사 + 목적어) 를 기본 형태로 하되 목적어의 명시가 애매한 경우는 생략가능하다.
 *     
 *   2 - variable naming
 *     snake_case 를 기본으로 한다.
 *     (꾸밈말 + variable 이 저장하는 객체의 속성) 을 기본 형태로 한다.
 *     아래 사항을 원칙으로 하되, 상황에 맞게 naming 하도록 하자.
 *     
 *     - container 객체 (vector, queue, map 등 ..) 의 경우
 *       (꾸밈말 + abstract container type) 을 기본 형태로 한다. 꾸밈말이 필요없는 경우 생략 가능하다.
 *       abstract container type: list(vector, list), queue(priority_queue, queue), stack(stack) ... 처럼 
 *       graph 처럼 adjacent list, tree, 2d-array 등 여러 표현이 가능한 경우에는 사용목적이 graph 이므로
 *       snake_graph 와 같이 naming 한다.
 *       ex) priority_queue<Snake> snake_queue, vector<vector<int> > snake_graph
 *     - else
 *       (꾸밈말 + variable 에 들어가는 값의 속성) 을 기본 형태로 한다.
 *       ex) max_rect_size, snake_idx
 *     
 *     !! variable naming 약어 규칙
 *     index -> idx, count -> cnt, value -> val, temporary(temp) -> tmp, 
 *   3 - define naming
 *     SCREAMING_SNAKE_CASE 를 기본을 한다. 이외의 규칙은 variable naming 가 동일하다.
 *   4 - struct and class naming
 *     UpperCamelCase 를 기본으로 한다. 이외의 규칙은 variable naming 과 동일하다.
 *     비교연산 operator 는 class or struct 안에서 선언함을 원칙으로 한다.
 *  
 * 3) indentation and space
 *     tab 이 아닌 4 space indent 를 사용한다. 자세한 사용은 sample code 를 참고하도록 하자.
 *  
 * 4) brace rule (중괄호 규칙)
 *     int getMaxVal(vector<int> list) {
 *         ...
 *         return 0;
 *     }
 *     다음과 같이 함수의 시작 중괄호는 위에 놓자.
 * 5) etc
 *   1 - range 의 표현
 *     모든 range 의 표현은 [) (시작은 닫혀있고 끝은 열려있음) 의 표현을 기본으로 한다.
 *   2 - comment
 *     코드를 보았을 때 바로 이해가 안되는 부분은 주석을 적어놓도록 하자.
 */

#include <iostream>
// problem2
#include <queue>
#include <vector>

using namespace std;

// problem2
struct Node {
    int time;
    int degree = 0;
    vector<int> node_list;

    bool operator< (Node n) const {
        return time < n.time;
    }
}

// problem1
void sortList(int *list, int left_idx, int right_idx) {
    // 조건문 내용 안에서는 사칙연산에 대해서 띄어쓰기를 하지 않는다.
    // 조건문 진입 시 명령이 한 줄 밖에 없다면 중괄호를 사용하지 않는다.
    if (left_idx+1 >= right_idx)
        return;
    
    int middle_idx = (left + right) >> 1;
    sortList(list, left_idx, middle_idx);   // [left, middle)
    sortList(list, middle_idx, right_idx);  // [middle, right)

    int *left_list = new int[middle-left];
    int *right_list = new int[right-middle];
    
    // copy left side array and right side array
    for (int i = 0; i < middle-left; i++) {
        left_list[i] = list[left+i];
    }
    for (int i = 0; i < right-middle; i++) {
        right_list[i] = list[middle+i];
    }

    curr_left_idx = 0;
    curr_right_idx = 0;
    for (int i = left_idx; i < right_idx; i++) {
        if (curr_left_idx == middle-left)
            list[i] = left_list[curr_left_idx++];
        else if (curr_right_idx == right-middle)
            list[i] = right_list[curr_right_idx++];
        else if (left_list[curr_left_idx] <= right_list[curr_right_idx]) 
            list[i] = left_list[curr_left_idx++];
        else 
            list[i] = right_list[curr_right_idx++];
    }

    delete left_list;
    delete right_list;
}

// merge sort
void solveProblem1() {
    int n;
    cin >> n;
    int *list = new int[n];

    for (int i = 0; i < n; i++) {
        cin >> list[i];
    }

    sort(list, 0, n);
    
    for (int i = 0; i < n; i++) {
        cout << list[i];
    }
    cout << endl;
    
    delete list[];
}

// https://www.acmicpc.net/problem/1516
void solveProblem2() {
    int n;  // 문제에 명시된 변수명 n 그대로 사용
    cin >> n;

    // adjacent list for graph
    // 1 ~ n index list, 0 is not used

    // index 가 0 부터 시작하지 않을 경우
    // 1) index 를 그냥 사용하거나
    // 2) index 를 고쳐서 0 부터 시작하게 하거나
    // 두 경우 모두 허용한다. 하지만 1), 2) 의 경우 모두
    // 해당 작업을 한 부분에 대해서는 주석을 써주는 것을 원칙으로 한다.
    Node build_graph[] = new Node[n+1];

    int tmp;
    for (int i = 1; i < n+1; i++) {
        // 코딩의 일관성을 위해 do while 은 쓰지 않는다.
        // 필요한 경우는 while (true) 로 대체하도록 하자
        cin >> tmp; // first input is time
        build_graph[i].time = tmp; 
        while (true) {
            cin >> tmp; // start index 가 들어온다. i 은 현재 target index
            if (tmp == -1)
                break;
            build_graph[tmp].node_list.push_back(i);
            build_graph[i].degree++;
        }
    }

    priority_queue<Node, vector<Node>, less<Node>> node_queue;
    // 1 ~ n iteration
    for (int i = 1; i < n+1; i++) {
        if (build_graph[i].degree == 0) {
            node_queue.push(build_graph[i]);
        }
    }

    // topological sort in DAG
    while (!node_queue.empty()) {
        Node *node = &node_queue.top();
        vector<int>::iterator node_iter = node->node_list.begin();
        for (; node_iter != node->node_list.end(); node_iter++) {
            build_graph[*node_iter].degree--;
            if (build_graph[*node_iter].degree == 0) {
                build_graph[*node_iter].time += node->time;
                node_queue.push(build_graph[*node_iter]);
            } 
        }
    }

    // 1 ~ n iteration
    for (int i = 1; i < n; i++) {
        cout << build_graph[i].time << endl;
    }

    delete build_graph;
} 

int main() {
    // 빠른 iostream cin, cout 을 위해 sync_with_stdio(false) 를 해줍니다.
    ios_base::sync_with_stdio(false);
    int test_case;
    cin >> test_case;

    // test case 가 n 번 있는 경우 problem solve 는 함수에서 따로 실행한다.
    for (int i = 0; i < test_case; i++) {
        solveProblem1();
    }

    for (int i = 0; i < test_case; i++) {
        solveProblem2();
    }

    return 0;
}