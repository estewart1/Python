function findOdd(A) { 
    var b = 0;
    for (var a = 0; a < A.length; ++a) {
      if (A[a] % 2) {
        b++;
      }
    }
    return b;
  }
  console.log(findOdd('abba'));