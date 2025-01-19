# include <iostream>
# include <cctype>
# include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;

    int total_up = 0;
    int total_low = 0;

    for (int i = 0; i<s.length(); i++){
        if (islower(s[i])){
            total_low++;
        }
        else{
            total_up++;
        }
    }
    if ((total_low >= total_up)){
        for (int i = 0; i<s.length(); i++){
            char c = tolower(s[i]);
            cout<<c;
        }   
    }
    else{
        for (int i = 0; i<s.length(); i++){
            char c = toupper(s[i]);
            cout<<c; 
        }   
    }

    return 0;
}