function isPalindrome(line){
    line = line.isString();
    const pal = line.split('').reverse().join('');
    if (line == pal){
        return true;
    } else {
        return false;
    };
};