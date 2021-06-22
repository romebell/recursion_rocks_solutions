function flattenArray(array, result=[]) {
  // take in an array
  // output should be the flattened array result 
  // We can expect our original, and subsequent params to be an array, so we can iterate using a for loop
  for (let a = 0; a < array.length; a+) {
    // conditional - test if item at position 'a' is an object (an array) or not   
    if (typeof array[a] === "object") {
      // if it is an array, call the flatten function again, passing in the sub array and the current val of result  
      flattenArray(array[a], result)
    } else {
      // if it is not an array, passing current object to the end of result 
      console.log("current state",result)
      result.push(array[a])
    }
  }
  console.log('before return', result)
  return result;
}