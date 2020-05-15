var numberToWord = {
  0: '',
  1: 'one',
  2: 'two',
  3: 'three',
  4: 'four',
  5: 'five',
  6: 'six',
  7: 'seven',
  8: 'eight',
  9: 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
};
var letterSum = {5: 19};

void main() {
//   print(numberLetterCounts(1000));
  print(numberLetterCountsRecursive(1000));
}

int numberLetterCounts(n) {
  var index = 6;
  while (index <= n) {
    final letterCount = spellAndCount(index);
    letterSum[index] = letterCount + letterSum[index - 1];
    index++;
  }

  return letterSum[n];
}

int numberLetterCountsRecursive(n) {
  if (n <= 5) {
    return 19;
  }
  return spellAndCount(n) + numberLetterCountsRecursive(n - 1);
}

int spellAndCount(n) {
  final spelledLetter = numberToWord[n];
  if (spelledLetter == null) {
    final length = n.toString().length;
    switch (length) {
      case 2:
        switch (n ~/ 10) {
          case 2:
            return 'twenty'.length + numberToWord[n % 10].length;
          case 3:
            return 'thirty'.length + numberToWord[n % 10].length;
          case 4:
            return 'forty'.length + numberToWord[n % 10].length;
          case 5:
            return 'fifty'.length + numberToWord[n % 10].length;
          case 8:
            return 'eighty'.length + numberToWord[n % 10].length;
          default:
            return numberToWord[n ~/ 10].length +
                'ty'.length +
                numberToWord[n % 10].length;
        }
        break;
      case 3:
        final last2Count = spellAndCount(n % 100);
        final andCount = last2Count > 0 ? 'and'.length : 0;
        return numberToWord[n ~/ 100].length +
            'hundred'.length +
            last2Count +
            andCount;
      case 4:
        return 'onethousand'.length;
    }
  } else {
    return spelledLetter.length;
  }
}
