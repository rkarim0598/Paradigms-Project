// call this function after user signs in/clicks sign out
updateUser = () => {
    var anchor = document.getElementById('sign');
    console.log(anchor);
    var user = localStorage.getItem('uid');
    console.log(anchor)
    if (user != null) {
        anchor.innerHTML = 'Sign out ' + user + '?'
        anchor.onclick = () => {
            localStorage.clear()
        }
        anchor.href = "../website/index.html"
    }
}