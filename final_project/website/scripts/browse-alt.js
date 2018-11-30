initHeader()
updateUser()

generateSuggestions = (shows) => {
    for (var i = 0; i < shows.length; i++) {
        var y = i + 1
        var title = document.getElementById('sid' + y + '-name')
        var desc = document.getElementById('sid' + y + '-desc')
        var rating = document.getElementById('sid' + y + '-rating')

        title.innerHTML = shows[i].name
        desc.innerHTML = shows[i].summary
        rating.innerHTML = shows[i].rating
    }
}

getSuggestionNumbers = (length) => {
    var min = 0
    var max = length - 1
    var numbers = []

    for (var i = 6; i > 0; i--) {
        var x = Math.floor(Math.random() * (+max - +min)) + +min
        var flag = false
        for (var j = 0; j < numbers.length; j++) {
            if (numbers[j] === x) {
                i++
                flag = true
                break
            }
        }
        if (flag === false) {
            numbers.push(x)
        }
    }
    return numbers
}

getLength = () => {
    var xhr = new XMLHttpRequest()
    xhr.open('GET', 'http://student04.cse.nd.edu:52048/shows/', true)
    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        // console.log(response)
        if (response['result'] == 'success') {
            var showList = []
            var showLength = response.output.length
            var output = response.output
            var numbers = getSuggestionNumbers(showLength)
            for (var i = 0; i < numbers.length; i++) {
                showList.push(output[numbers[i]])
            }
            console.log(showList)
            generateSuggestions(showList)
        } else {
            console.log('something went wrong oh no')
        }
    }
    xhr.send()
}
getLength()
