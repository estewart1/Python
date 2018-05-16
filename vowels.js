/*function getCount(str) {
    return str.match(/[aeiou]/gi).length;
}*/
function getCount(str) {
    if (str.match(/[aeiou]/gi)) {
        return str.match(/[aeiou]/gi).length;
    } else {
        return 0;
    }
}
console.log(getCount('mnzl'));