const isPrime = number => {
  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      return false;
    }
  }

  return true;
}

const nthPrime = n => {
  let noPrimes = 1;
  let lastPrime = 2;
  let index = 3;
  while(noPrimes < n) {
    if (isPrime(index)) {
      noPrimes++;
      lastPrime = index;
    }
    index++;
  }
  return lastPrime;
}

console.log(nthPrime(10001));
