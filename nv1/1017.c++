#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int x,y,spent;
  cin >> x;
  cin >> y; 

  spent = (x*y)/12;

  std::cout << std::fixed << std::setprecision(3);
  cout << spent;

  return 0;
}