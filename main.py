function sumEvenNumbers(start, end) {
  let sum = 0;
  for (let i = start; i <= end; i++) {
    if (i % 2 === 0) {
      sum += i;
    }
  }
  return sum;
}

// Prompt the user to enter the range
const start = parseInt(prompt("Enter the starting number:"));
const end = parseInt(prompt("Enter the ending number:"));

// Calculate the sum of even numbers
const result = sumEvenNumbers(start, end);

// Display the result
console.log(`The sum of even numbers between ${start} and ${end} is ${result}`);

