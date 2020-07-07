// Dummy method

const multiplesOf3and5 = number => {
    let sum = 0;
    const n3 = (number - 1) / 3;
    const n5 = (number - 1) / 5;

    for (let i = 1; i <= n3; i++) {
        sum += i * 3;
    }

    for (let i = 1; i <= n5; i++) {
        if (i * 5 % 3 !== 0) {
            sum += i * 5;
        }
    }
    return sum;
}
