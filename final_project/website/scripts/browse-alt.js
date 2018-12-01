initHeader()
updateUser()
var showList
var imageIndex
var sidList

setImage = () => {
    console.log('hi')
    var itemList = document.getElementById('show-list').getElementsByClassName('mdl-list__item')

    for (var i = 0; i < itemList.length; i++) {
        itemList[i].onclick = (event) => {
            imageIndex = parseInt(event.currentTarget.id[3]) - 1
            console.log(imageIndex)
            var image = document.getElementById('image')
            image.src = showList[imageIndex].image
            console.log(showList)
            // getEpisodes()
        }
    }

}


generateSuggestions = (shows) => {
    showList = shows
    for (var i = 0; i < shows.length; i++) {
        var y = i + 1

        var listContainer = document.getElementById('sid' + y)
        console.log(listContainer)
        // listContainer.onclick = () => {
        //     setImage()
        // }

        var title = document.getElementById('sid' + y + '-name')
        var desc = document.getElementById('sid' + y + '-desc')
        var rating = document.getElementById('sid' + y + '-rating')

        title.innerHTML = shows[i].name
        desc.innerHTML = shows[i].summary
        rating.innerHTML = shows[i].rating
        // console.log(shows[i].image)
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
            var list = []
            var showLength = response.output.length
            var output = response.output
            var numbers = getSuggestionNumbers(showLength)
            for (var i = 0; i < numbers.length; i++) {
                list.push(output[numbers[i]])
            }
            sidList = list
            console.log(sidList)
            console.log('bye')
            generateSuggestions(list)
            setImage()
        } else {
            console.log('something went wrong oh no')
        }
    }
    xhr.send()
}
getLength()
