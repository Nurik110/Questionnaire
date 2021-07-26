const el = document.getElementById('registr');
const email = document.getElementById('email');
const username = document.getElementById('username');
const last_name = document.getElementById('last_name');
const password1 = document.getElementById('password1');
const password2 = document.getElementById('password2');

const emaill = document.getElementById('emaill');
const passwordd = document.getElementById('passwordd');
const regist = document.getElementById('regist')


el.addEventListener('click', async (ev) => {
    ev.preventDefault();

    let user = {
        email: email.value,
        username: username.value,
        last_name: last_name.value,
        password: password1.value,
        password2: password2.value,
    }
    let response = await fetch('/main/', {
        method: "POST",
        headers: {
            "Accept": "application/json",
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user)
    })

    console.log(csrftoken)

    if (response.ok) {
        console.log(await response.json())

        location.href = "/";
    } else {
        console.log("ERROR")
    }

})
regist.addEventListener('click', async (ev) => {
    ev.preventDefault();

    let users = {
        emaill: emaill.value,
        passwordd: passwordd.value,
    }
    let response = await fetch('/main/login/', {
        method: "POST",
        headers: {
            "Accept": "application/json",
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(users)
    })

    console.log(csrftoken)

    if (response.ok) {
        console.log(await response.json())

        location.href = "/login";
    } else {
        console.log("ERROR")
    }

})

