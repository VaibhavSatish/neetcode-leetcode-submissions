class Solution {
public:
    bool isPalindrome(string s) {
        s.erase(remove(s.begin(), s.end(), ' '), s.end());
        s.erase(std::remove_if(s.begin(), s.end(), [](char c) {
        return !std::isalnum(c);}), s.end());
        string origin = s;
        for (char& c : origin) { 
            c = tolower(c);    
        }
        for (char& j : s) { 
            j = tolower(j);    
        }
        reverse(s.begin(), s.end());
        cout << origin << endl;
        cout << s << endl;
        return origin == s;
}
};
