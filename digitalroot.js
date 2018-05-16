function digital_root(n) {
    var total = 0;
    var splits = n.toString().split("").map(Number);
    while (splits.length > 1) {
      total = splits.reduce(function(a, b) {
        return a + b;
      });
      splits = total.toString().split("").map(Number);
    }
    return total;
}
console.log(digital_root(942));