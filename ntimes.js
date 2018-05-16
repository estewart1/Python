function deleteNth(arr,n){
    var number = 0;
    for (var i; i < arr.length; i++){
        if (arr[i] === n) {
            number++;
        }
    }
    return number;
}