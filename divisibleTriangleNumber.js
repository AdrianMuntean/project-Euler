const noDivisors = n => {
  let noDivs = 2;
  for (let index = 2; index <= Math.sqrt(n); index++) {
    if (n % index === 0) {
      noDivs += 2;
    }
  }

  return noDivs;
}

const divisibleTriangleNumber = n => {
  let i = 1;
  let lastTriangleNumber = 1; 
  while (noDivisors(lastTriangleNumber) <= n) {
    i++;
    lastTriangleNumber += i;

  }
  return lastTriangleNumber;
}

console.log(divisibleTriangleNumber(500));
