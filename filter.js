function filter_list(l) {
 var empty = [];
 for (x = 0; x < l.length; x++) {
    if (Number.isInteger(l[x]) === true) {
        empty.push(l[x]);
    }
 }  
 return empty;
    //return l.match(/(\d+)/g);
    //  return l.replace(/[a-z]|'\d+'/gi,'');
}
console.log(filter_list([1,2,'aasf','1','123',123]));