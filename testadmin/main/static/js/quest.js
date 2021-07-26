const nickname = document.getElementById('nickname');
const radios = document.getElementsByName('dzen');
const buttsubmit = document.getElementById('buttsubmit');


buttsubmit.addEventListener('click', async (ev) => {
    ev.preventDefault();
    // let yesno;
    // for (let i = 0, length = radios.length; i < length; i++) {
    //     if (radios[i].checked) {
    //         yesno = radios[i].checked;
    //         // alert(radios[i].value);
    //         break;
    //     }
    // }
    let butt =document.querySelector('input[name="dzen"]:checked').value;
    let user = {
        nickname: nickname.value,
        butt: butt
    }

    let response = await fetch('/main/questionnaire/', {
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

        location.href = "/questionnaire";
    } else {
        console.log("ERROR")
    }

})