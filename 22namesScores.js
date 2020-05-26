const alphabeticalValue = text => {
  let sum = 0;
  for(let index = 0; index < text.length; index++) {
    sum += text.charCodeAt(index) - 64;
  }

  return sum;
}

const namesScores = arr => {
  arr.sort();
  let sum = 0;
  for(let index = 0; index < arr.length; index++) {
    sum += alphabeticalValue(arr[index]) * (index + 1);
  }
  return sum;
}

// Only change code above this line
const test1 = ['THIS', 'IS', 'ONLY', 'A', 'TEST']; // 791

console.log(namesScores(dataset)); //871198282
