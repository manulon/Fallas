async function getResult() {
    genre_value       = document.querySelector('input[name="genre"]:checked').value;
    duration_value    = document.querySelector('input[name="duration"]:checked').value;
    year_value        = document.querySelector('input[name="year"]:checked').value;
    country_value     = document.querySelector('input[name="country"]:checked').value;
    body_obj = {
        genre: genre_value,   
        duration: duration_value,
        year: year_value,    
        country: country_value 
    };
    
    var request = new Request('/result', {
                    headers: {
                            'Accept': 'application/json',
                            'Content-Type': 'application/json'
                            },
                    method: 'POST',
                    body: JSON.stringify(body_obj)
                });

    const response = await fetch(request);

    var data = await response.json();
    console.log(data);

    if (data["name"] == ""){
        document.getElementById('opening-name').innerHTML = "No pudimos encontrar una apertura en base a los criterios que eligió"
    }
    else{
        document.getElementById('opening-name').innerHTML = data["name"]
        document.getElementById('opening-image').src = "static/imgs/" + data["img"]
        document.getElementById('opening-link').href = data["link"]
        document.getElementById('opening-link').target = "_blank"
    }
}

var q0 = document.getElementById("q0");
var q1 = document.getElementById("q1");
var q2 = document.getElementById("q2");
var q3 = document.getElementById("q3");
var q4 = document.getElementById("q4");
var result = document.getElementById("result");

var next0 = document.getElementById('next0')
var next1 = document.getElementById('next1')
var next2 = document.getElementById('next2')
var next3 = document.getElementById('next3')
var next4 = document.getElementById('next4')
var back2 = document.getElementById('back2')
var back3 = document.getElementById('back3')
var back4 = document.getElementById('back4')

document.addEventListener('DOMContentLoaded', function() {
    next0.onclick = function() {
        q0.style.left = "-650px";
        q1.style.left = "50px";
        console.log("aprete next0")
    }
    next1.onclick = function() {
        q1.style.left = "-650px";
        q2.style.left = "50px";
        console.log("aprete next1")
    }
    next2.onclick = function() {
        q2.style.left = "-650px";
        q3.style.left = "50px";
        console.log("aprete next2")
    }
    next3.onclick = function() {
        q3.style.left = "-650px";
        q4.style.left = "50px";
        console.log("aprete next3")
    }
    next4.onclick = function() {
        q4.style.left = "-650px";
        result.style.left = "15px";
        getResult()
    }
    back2.onclick = function() {
        q2.style.left = "-650px";
        q1.style.left = "50px";
        console.log("aprete back2")
    }
    back3.onclick = function() {
        q3.style.left = "-650px";
        q2.style.left = "50px";
        console.log("aprete back3")
    }
    back4.onclick = function() {
        q4.style.left = "-650px";
        q3.style.left = "50px";
        console.log("aprete back4")
    }
});