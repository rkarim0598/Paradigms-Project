initHeader()
updateUser()

verify = (uid, password) => {
    var xhr = new XMLHttpRequest()
    xhr.open('GET', 'http://student04.cse.nd.edu:52048/users/' + uid, true)
    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        console.log(response)
        if (response['result'] == 'success') {
            localStorage.setItem('uid', uid)
            window.location.href = '../website/browse-alt.html'
        }
    }

    xhr.send()
}

sign = () => {
    var uid = document.getElementById('sign-uid').value
    var password = document.getElementById('sign-password').value

    // don't execute if no uid or password entered
    if (uid == "" || password == "") {
        return;
    }

    verify(uid, password)

}

var signIn = document.getElementById('sign-button')
signIn.addEventListener("click", sign)