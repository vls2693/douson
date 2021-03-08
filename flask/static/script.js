//document.addEventListener('DOMContentLoaded', function() {
//    console.log('it works!')
//})



function addString() {
    var app = document.querySelector('.bunch')
    var title = document.createElement('fieldset')
    title.innerHTML = '<input class=\"name\" name=\"name\" required placeholder=\"Name\" type=\"text\">\n                <input class=\"sum\" name=\"sum\" required placeholder=\"Sum\" type=\"number\">'
    app.appendChild(title)
}

function removeString() {
    var parent = document.querySelector('.bunch')
    var elem = document.querySelector('fieldset')
    parent.removeChild(elem)
//    elem.remove()
}