if ("serviceWorker" in navigator) {
    window.addEventListener("load", function () {
        navigator.serviceWorker
            .register("/serviceWorker.js")
            .then(res => console.log("service worker registered"))
            .catch(err => console.log("service worker not registered", err))
    })
}

var form = document.forms.namedItem("paymentForm");
form.addEventListener('submit', function (ev) {

    var oData = new FormData(document.forms.namedItem("paymentForm"));

    var oReq = new XMLHttpRequest();
    oReq.open("POST", "/payments", true);
    oReq.onload = function (oEvent) {
        if (oReq.status == 200) {
            alert('ok!')

        } else {
            alert('fail!')
        }
    };

    oReq.send(oData);
    ev.preventDefault();
}, false);
