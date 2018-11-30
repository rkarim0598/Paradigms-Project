initHeader()
updateUser()

/* Sign in tab code */
// process user check
process = (result) => {
    if (result == 'success') {
        window.location.href = '../website/browse-alt.html'
    } else {
        alert('Invalid user name or password!')
    }
}

// check if user exists
verify = (uid, password) => {
    var xhr = new XMLHttpRequest()
    xhr.open('GET', 'http://student04.cse.nd.edu:52048/users/' + uid, true)
    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        if (response['result'] == 'success') {
            localStorage.setItem('uid', uid)
            process('success')
        }
        else {
            process('failure')
        }
    }

    xhr.send()
}

// grab uid and password from textboxes and check if user exists
sign = () => {
    var uid = document.getElementById('sign-uid').value
    var password = document.getElementById('sign-password').value

    // don't execute if no uid or password entered
    if (uid == "" || password == "") {
        return;
    }

    verify(uid, password)
}
/* end sign in tab code */

/* create account tab code */
createUser = (uid, password) => {
    var data = {
        "uname" : uid,
        "pname" : uid,
        "password" : password
    }
    var json = JSON.stringify(data)
    var xhr = new XMLHttpRequest()
    xhr.open('POST', 'http://student04.cse.nd.edu:52048/users/', true)

    xhr.onload = () => {
        var response = JSON.parse(xhr.responseText)
        if (response['result'] != 'success') {
            alert('Error occured, please try again')
        } else {
            window.href.location = '../website/sign-or-create.html#sign-in'
        }
    }

    xhr.send()
}

create = () => {
    var uid = document.getElementById('create-uid').value
    var password = document.getElementById('create-password').value
    var check = document.getElementById('create-check').value

    // don't execute if no uid, password, or check entered
    // or if password and check don't equal
    if (uid == "" || password == "" || check == "" || password != check) {
        return;
    }

    createUser(uid, password)

}