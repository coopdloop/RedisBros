function search() {

    v = document.getElementById('searchsubmit').value.value;

    var url = "/search" + "?value=" + v;
    var req = new XMLHttpRequest();
    req.open("GET", url, false);
    req.send();

    console.log(req.responseText);
    document.getElementById('status').innerHTML = "Status : " + req.responseText;

}