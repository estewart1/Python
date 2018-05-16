function calendar(){
    var day = prompt("What day? ", "day");
    while (day < 30){
        let activity = prompt('What are you doing on that day? ', "event");
        let time = prompt('What time is that activity?', "time");
        return time + " " + activity;
    }
}
/*function myFunction() {
    var person = prompt("Please enter your name", "Harry Potter");
    if (person != null) {
        document.getElementById("demo").innerHTML =
        "Hello " + person + "! How are you today?";
    }
}*/
console.log(calendar());