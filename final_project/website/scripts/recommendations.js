var show_rating = 1
var stars = [document.getElementById('1'),
document.getElementById('2'),
document.getElementById('3'),
document.getElementById('4'),
document.getElementById('5')
]
var sid = null
var uid

var highlight = (value) => {
    for (var i = value - 1; i >= 0; i--) {
        stars[i].className = "fa fa-star checked"
    }

    for (var j = 4; j >= value; j--) {
        stars[j].className = "fa fa-star"
    }
}

var rank = (update) => {
    show_rating = update
    console.log(update)
    highlight(update)
}

getRecked = () => {
    uid = localStorage.getItem('uid')
    var xhr = new XMLHttpRequest()
    if (uid === null) {
        uid = localStorage.getItem('uid')
    }
    xhr.open('GET', 'http://student04.cse.nd.edu:52048/recommendations/' + uid, true)
    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        if (response['result'] == 'failure')
            submitVote()
        sid = response.sid
        getShow()
    }
    xhr.send()
}

submitVote = () => {
    var xhr = new XMLHttpRequest()
    var data = {
        'rating': show_rating,
        'sid': sid
    }
    var json = JSON.stringify(data)
    xhr.open('PUT', 'http://student04.cse.nd.edu:52048/recommendations/' + uid, true)
    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        console.log(response)

        if (response['result'] == 'success') {
            sid = response.sid
            getShow()
        }
        else {
            console.log('no')
        }
    }
    xhr.send(json)
}

getShow = () => {
    var xhr = new XMLHttpRequest()
    xhr.open('GET', 'http://student04.cse.nd.edu:52048/shows/' + sid, true)
    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        console.log(response)
        console.log('getshow')
        var image = document.getElementById('rec-image')
        image.src = response.output.image
        var title = document.getElementById('rec-title')
        title.innerHTML = response.output.name
        var summary = document.getElementById('rec-summary')
        summary.innerHTML = response.output.summary
    }
    xhr.send()
}


getRecked()
document.getElementById('submit-vote').onclick = () => {
    submitVote()
}