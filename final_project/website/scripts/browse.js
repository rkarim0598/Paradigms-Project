initHeader()
updateUser()

var show_rating
var stars = [ document.getElementById('1'),
              document.getElementById('2'),
              document.getElementById('3'),
              document.getElementById('4'),
              document.getElementById('5')
            ]

var rank = (update) => {
    show_rating = update
    console.log(update)
    
    for (var i = update-1; i >= 0; i--) {
        stars[i].className = "fa fa-star checked"
    }

    for (var j = 4; j >= update; j--) {
        stars[j].className = "fa fa-star"
    }
}