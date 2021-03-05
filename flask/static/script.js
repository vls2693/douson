//document.addEventListener('DOMContentLoaded', function() {
//    console.log('it works!')
//})



function addString() {
    var app = document.querySelector('.bunch')
    var title = document.createElement('fields')
    title.innerHTML = '<input class=\"name\" name=\"name2\" placeholder=\"Name\" type=\"text\">\n                <input class=\"sum\" name=\"sum2\" placeholder=\"Sum\" type=\"number\">'
    app.appendChild(title)
}