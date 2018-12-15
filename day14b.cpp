#include <vector>
#include <iostream>
#include <string>
//#include <algorithm>
using namespace std;

int partb(vector<char> s) {
  vector<char> input;
  input.push_back('3');
  input.push_back('7');
  int e1   = 0;
  int e2   = 1;
  int newr = 0;

  while (!equal(s.begin(), s.end(),
		input.end() - s.size()))
    {
     newr = (input[e1] - '0' + input[e2] - '0');
     auto newrs = to_string(newr);
     input.push_back(newrs[0]);
     
     if (newr >=10) {
       input.push_back(newrs[1]);
     }

     e1 = (1 + e1 + input[e1]-'0') % input.size();
     e2 = (1 + e2 + input[e2]-'0') % input.size();

    }

  return input.size() - s.size();
}


int main() {
   vector<char> a = {'0', '3', '0', '1', '2', '1'}; // my input ??
   //vector<char> a = {'2','6','0','3','2','1'};  // = 20319117 (should)
  //vector<char> a = {'5','9','4','1','4', '2', '9'}; // = 2018 *correct*
  //vector<char> a = {'9','2','5','1','0'}; // = 18 *correct*

  cout << partb(a) << endl;
}
