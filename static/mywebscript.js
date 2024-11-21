let RunSentimentAnalysis = ()=>{
    debugResponse = document.getElementById("debug_response");
    textToAnalyze = document.getElementById("textToAnalyze").value;

    debugResponse.innerHTML = debugResponse.innerHTML + "<br/>" + textToAnalyze;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        debugResponse.innerHTML = debugResponse.innerHTML + "<br/>" + this.readyState + " " + this.status;
        if (this.readyState == 4 && this.status == 200) {
            debugResponse.innerHTML = debugResponse.innerHTML + "<br/>" + xhttp.responseText;
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "/emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();

    debugResponse.innerHTML = debugResponse.innerHTML + "<br/>" + "Sent";
}
