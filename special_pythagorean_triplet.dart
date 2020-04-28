// Brute force, no math, stupid solution

import 'dart:math';

void main() {
  print(specialPythagoreanTriplet(1000));
}

int specialPythagoreanTriplet(n) {
  for (var first = 2; first < n / 2; first++) {
    for (var second = first + 1; second < n / 2; second++) {
      for (var third = second + 1; third < n / 2; third++) {
        if (first + second + third == n) {
          if (pow(first, 2) + pow(second, 2) == pow(third, 2)) {
            return first * second * third;
          }
        }
      }
    }
  }
  return n;
}
