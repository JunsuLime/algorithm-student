#include <iostream>

#define M 1234567891
#define R 31
#define OFFSET 96   

using namespace std;

unsigned long long pow(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result = (result * base) % M;
    }
    return result;
}

int main() {
    ios_base::sync_with_stdio(false);
    int l;
    cin >> l;
    string str;
    cin >> str;

    unsigned long long hash_val = 0;
    for (int i = 0; i < l; i++) {
        hash_val = (hash_val + ((static_cast<char>(str[i])-OFFSET) * pow(R, i))) % M;
    }
    cout << hash_val << endl;
}
