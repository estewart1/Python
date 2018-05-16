/*function root(x, n) {
  var math = require('mathjs');
  let r = math.nthRoot(x, n);
  return Math.pow(r, n);
}
console.log(root(256,4));*/
//Works but Codewars won't accept mathjs
function root(x, n) {
  return Math.pow(x, 1/n);
}
console.log(root(256,4));