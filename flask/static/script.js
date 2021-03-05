document.addEventListener('DOMContentLoaded', function() {
    console.log('it works!')
})

var app = document.querySelector('.bunch')
var title = document.createElement('fieldset')
title.innerHTML = '<input class=\"name\" name=\"name2\" placeholder=\"Name\" type=\"text\">\n                <input class=\"sum\" name=\"sum2\" placeholder=\"Sum\" type=\"number\">'


app.appendChild(title)

console.log('title', title)