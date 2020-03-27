
#include <bits/stdc++.h>

using namespace std;

int main() {

    cout << "Hello!\nIt is our INDIVIDUAL PROJECT!&\Please, choose algo you need:\n";
    cout << "1) MERGE SORT\n2) DO\n3) BINARY SEARCH\n";
    string s;
    cin >> s;
    while (s != "exit") {
        if (s == "1") {
            system("python sort.py");
        }
        if (s == "2") {
            system("python do.py");
        }
        if (s == "3") {
            system("python bin.py");
        }
        cin >> s;
    }

    return 0;
}
