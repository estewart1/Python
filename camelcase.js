function toCamelCase(str) {
    var first = str[0];
    var str = str.substr(1);
    var up = str.replace(/(^\w|\b\w)/gi, function(letter, index) {
        return index == 0 ? letter.toLowerCase() : letter.toUpperCase();
      }).replace(/\s+|-|_/g, '');
    return first + up;
}
  
console.log(toCamelCase('the-stealth-warrior'));

//function toCamelCase(str) {
//    return str.replace(/(^\w|\b\w)/gi, function(letter, index) {
//        return index == 0 ? letter.toLowerCase() : letter.toUpperCase();
//      }).replace(/\s+|-|_/g, '');
//  }