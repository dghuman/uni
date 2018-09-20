#include <iostream>
using namespace std;

int factorial(int x) {
  int final;
  final = 1;
  for (int i = 0; i < x; i++) {
    final = final*(i + 1);
  }
  return final;
}
int main() {
  int n;
  int r;
  int nCr;
  cout << "n: ";
  cin >> n;
  cout << "r: ";
  cin >> r;
  nCr = factorial(n)/(factorial(n-r)*factorial(r));
  cout << "nCr = " << nCr << endl;
  return 0;
}
