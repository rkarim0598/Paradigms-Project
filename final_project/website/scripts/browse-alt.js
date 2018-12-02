initHeader()
updateUser()
var showList
var imageIndex
var sidList

getEpisodes = (sid) => {
    var xhr = new XMLHttpRequest()

    xhr.open('GET', 'http://student04.cse.nd.edu:52048/shows/' + sid, true)
    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        console.log(response)
        if (response['result'] == 'success') {
            var episodeLength = response.episodes.length
            console.log(episodeLength)

            var genre = response.output.genres 
            var summary = response.output.summary 
            var seasons = response.episodes[episodeLength - 1].season
            
            var div = document.getElementById('episodes')
            while (div.firstChild) {
                div.removeChild(div.firstChild)
            }

            var label = document.getElementById('infoLabel')
            label.innerHTML = showList[imageIndex].name
            
            var epiData = document.createElement('p')
            epiData.innerHTML = 'Seasons: ' + seasons + '<br>' +
                                'Episodes: ' + episodeLength

            var genreText = document.createElement('p')
            genreText.innerHTML = 'Genres: ' + genre

            var sum = document.createElement('p')
            sum.innerHTML = summary

            div.appendChild(epiData)
            div.append(genreText)
            div.appendChild(sum)
        } else {
            var div = document.getElementById('episodes')
            var label = document.getElementById('infoLabel')
            label.innerHTML = showList[imageIndex].name
            while (div.firstChild) {
                div.removeChild(div.firstChild)
            }
            var genre = response.output.genres 
            var summary = response.output.summary 
            var para = document.createElement('p')
            para.innerHTML = 'No episode data for ' + response.output.name
            var genreText = document.createElement('p')
            genreText.innerHTML = 'Genres: ' + genre
            var sum = document.createElement('p')
            sum.innerHTML = summary
            div.appendChild(para)  
            div.appendChild(genreText)  
            div.appendChild(sum)

        }
    }
    xhr.send()
}

setImage = () => {
    var itemList = document.getElementById('show-list').getElementsByClassName('mdl-list__item')

    for (var i = 0; i < itemList.length; i++) {
        itemList[i].onclick = (event) => {
            imageIndex = parseInt(event.currentTarget.id[3]) - 1
            var image = document.getElementById('image')
            image.src = showList[imageIndex].image

            getEpisodes(showList[imageIndex].sid)
            location.hash = 'info'
        }
    }

}


generateSuggestions = (shows) => {
    showList = shows
    for (var i = 0; i < shows.length; i++) {
        var y = i + 1

        var listContainer = document.getElementById('sid' + y)
        // listContainer.onclick = () => {
        //     setImage()
        // }

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
        if (response['result'] == 'success') {
            var list = []
            var showLength = response.output.length
            var output = response.output
            var numbers = getSuggestionNumbers(showLength)
            for (var i = 0; i < numbers.length; i++) {
                list.push(output[numbers[i]])
            }
            sidList = list
            generateSuggestions(list)
            setImage()
        } else {
            console.log('something went wrong oh no')
        }
    }
    xhr.send()
}
getLength()
