const visited = []

const properDivisorSum = n => {
  let sum = 1;
  for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) {
        sum += i;
        sum += n/i;
      }
  }

  return sum;
}


const sumAmicableNum = n => {
  let sum = 0;
  for(let i = 10; i < n; i++) {
      const divSum = properDivisorSum(i);
      if (divSum !== i && !!!visited[i] && properDivisorSum(divSum) === i) {
          sum += divSum + i;
          visited[divSum] = true;
      }
  }
  return sum;
}

sumAmicableNum(10000); //31626
