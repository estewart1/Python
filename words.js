function spinWords(str) {
  var match = str.match(/[a-z]{5,}/gi);
  var match2 = str.match(/[a-z]{1,4}/gi);
  match = match.toString().split("").reverse().join("").split(" ").reverse().join(" ");
  return (match2 + ' ' + match.replace(',',' '));
}
console.log(spinWords('Hey fellow warriors'));


function test() {
  var match = "This is a test to reverse these words";
  match = match.toString().split("").reverse().join("").split(" ").reverse().join(" ");
}
console.log(test());