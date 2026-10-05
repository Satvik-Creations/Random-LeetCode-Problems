#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int strStr(string haystack, string needle) {

        if (needle.length() > haystack.length())
            return -1;

        for (int i = 0; i <= haystack.length() - needle.length(); ++i) {
            if (haystack.substr(i, needle.length()) == needle) {
                return i;
            }
        }

        return -1;
    }
};

// int main() {
//     Solution s;

//     cout << s.strStr("Hello World", "World") << endl;
//     cout << s.strStr("Pneumonoultramicroscopicsilicovolcanoconiosis",
//                      "silicovolcanoconiosis") << endl;

//     return 0;
// }