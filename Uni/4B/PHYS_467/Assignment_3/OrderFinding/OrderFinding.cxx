#include <iostream>
#include <math.h>

int main() {
  int a;
  int order;
  int N;

  std::cout << "Number to Factor: ";
  std::cin >> N;
  std::cout << "Integer of order we are finding: ";
  std::cin >> a;

  // For simplicity we assume that the two terms are coprime
  order = 1;
  while ((int)pow(a,order) % N != 1) {
    order++;
    if ((int)pow(a,order) % N == 0) {
    std::cout << "The two integers are not coprime. " << a << "^" << order << " is divisible by" << N << std::endl;
      return 0;
    }
  }
  std::cout << "Order is " << order << std::endl;
  return 0;
}
  
    
    
  
