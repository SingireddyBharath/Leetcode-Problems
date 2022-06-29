#include<bits/stdc++.h>
using namespace std;
int characterReplacement(string s, int k) {
    int res = 0;
    unordered_map<char, int> count;
    int maxF = 0;

    int l = 0;

    for (int i = 0; i < s.length(); i++) {
        if(count.find(s[i]) != count.end()) 
            count[s[i]]+=1;
            
        else
            count[s[i]] = 1;
            

        maxF = max(maxF, count[s[i]]);
       
            if (((i - l + 1) - maxF) > k)
            {
                count[s[l]] -= 1;
                l++;
            }
        res = max(res, (i - l + 1));
    }
    
    return res;
}
int main(){

    string str;cin >> str;
    int k;cin>>k;
    cout<<characterReplacement(str, k)<<endl;
}
