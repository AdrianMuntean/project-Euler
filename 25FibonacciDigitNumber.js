const fibNums = [1, 1, 2]

const next_fib = () => {
  const fibValue = fibNums[fibNums.length - 1] + fibNums[fibNums.length - 2];
  fibNums.push(fibValue);
  return fibValue;
}

const digitFibonacci = (noDigit) => {
  let index = 3;
  while(true) {
      const fibNumber = next_fib();
      if (fibNumber.toString().length == noDigit) {
        return index + 1;
      } else {
        index++;
      }
  }
}

console.log(digitFibonacci(20));

