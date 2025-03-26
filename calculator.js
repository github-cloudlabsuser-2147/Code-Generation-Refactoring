function add(a, b) {
    return a + b;
}

function subtract(a, b) {
    return a - b;
}

function multiply(a, b) {
    return a * b;
}

function divide(a, b) {
    if (b === 0) {
        throw new Error("Cannot divide by zero");
    }
    return a / b;
}

// Example usage:
console.log("Add: " + add(5, 3));        // Output: Add: 8
console.log("Subtract: " + subtract(5, 3));  // Output: Subtract: 2
console.log("Multiply: " + multiply(5, 3));  // Output: Multiply: 15
console.log("Divide: " + divide(5, 3));    // Output: Divide: 1.6666666666666667