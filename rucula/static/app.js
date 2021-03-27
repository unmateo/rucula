if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
        navigator.serviceWorker
            .register("/serviceWorker.js")
            .then(res => console.log("service worker registered"))
            .catch(err => console.log("service worker not registered", err))
    })
}

function getFormValues(form) {
    var data = {};
    for (var i = 0, ii = form.length; i < ii; ++i) {
        var input = form[i];
        if (input.name) {
            data[input.name] = input.value;
        }
    }
    return data
}

async function submitPayment (event) {
    const form = document.getElementById("paymentForm");
    const values = getFormValues(form);
    const settings = {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
    };

    const fetchResponse = await fetch('/payments', settings);
    await handleResponse(fetchResponse);
}

async function handleResponse(response) {
    if (response.status == 201) {
        alert('¡Listo!');
    } else {
        const error = await response.text();
        alert(error);
    }
}
