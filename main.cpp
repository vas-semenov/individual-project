//  ЫЫЫ А Я ХОЧУ ПОДНЯТЬ РЕЙТИНГ
//  main.cpp
//  main
//
//  Created by Борис Барков on 04.11.2019.
//  Copyright © 2019 Борис Барков. All rights reserved.
//
 
#include <bits/stdc++.h>
 
using namespace std;

void sort(int l, int r, vector<int> &a) {
    if (r - l == 1) {
        cout << a[0] << endl;
        return;
    }
    int mid = l + (r - l) / 2;
    vector<int> a1, a2;
    for (int i = l; i < mid; i++) {
        a1.push_back(a[i]);
    }
    for (int i = mid; i < r; i++) {
        a2.push_back(a[i]);
    }
    sort(0, mid, a1);
    sort(0, r - mid, a2);
    int i = 0, j = 0;
    while (i < a1.size() && j < a2.size()) {
        a[i + j] = min(a1[i], a2[j]);
        if (a1[i] <= a2[j]) {
            i++;
        } else {
            j++;
        }
    }
    while (i < a1.size()) {
        a[i + j] = a1[i];
        i++;
    }
    while (j < a2.size()) {
        a[i + j] = a2[j];
        j++;
    }
    for (int i = 0; i < a.size(); i++) {
        cout << a[i] << ' ';
    }
    cout << endl;
}

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(0, n, a);
}
 
signed main() {
    int n = 1;
    //cin >> n;
    for (int i = 0; i < n; i++) {
        solve();
    }
}
