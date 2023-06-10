const mySwitch = document.getElementById('mySwitch');

mySwitch.addEventListener('change', function() {
    var body = document.getElementById("body");
    if(this.checked) {
        body.className = "dark-mode";
    }
    else {
        body.className = "light-mode";
    }
});