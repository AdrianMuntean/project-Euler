const largestPrimeFactor = number => {
    let largest;
    for (let primeFactor = 2;
        primeFactor <= Math.sqrt(number);
        primeFactor++) {
        if (number % primeFactor === 0) {
            number = number / primeFactor
        }
    }
    return !!largest ? largest : number;
}

largestPrimeFactor(600851475143)
