#include <iostream>
using namespace std;

void fib(int n) {
    int f1 = 0, f2 = 1;

    if (n < 1) {
        return;
    }

    cout << f1 << endl;

    for (int i = 0; i < n; i++) {
        cout << f2 << endl;
        int next = f1 + f2;
        f1 = f2;
        f2 = next;
    }
}

int main() {
    int num;
    cout << "How many numbers do you want? ";
    cin >> num;
    fib(num);
    return 0;
}