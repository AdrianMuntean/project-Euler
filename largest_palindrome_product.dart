import 'dart:math';

void main() {
  print(largestPalindromeProduct(3));
}

int largestPalindromeProduct(int n) {
  var largestPalindrom = n;
  for (var firstNumber = pow(10, n - 1); firstNumber < pow(10, n); firstNumber++) {
    for (var secondNumber = pow(10, n - 1); secondNumber < pow(10, n); secondNumber++){
      var product = firstNumber * secondNumber;
      if (isPalindrome(product) && largestPalindrom < product) {
        largestPalindrom = product;
      }
    }
  }
  
  return largestPalindrom;
}

bool isPalindrome(int number) {
  String noString = number.toString();
  if (noString.length < 2) {
    return true;
  }
  
  for (var charIndex = 0; charIndex < noString.length; charIndex++) {
    if (noString[charIndex] != noString[noString.length - charIndex - 1]) {
      return false;
    }
  }
  return true;
}


