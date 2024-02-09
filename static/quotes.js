function showQuote(evt) {
  
    fetch('/generator')
        .then((response) => response.text())
        .then((responseTEXT)=> {
            const results = document.querySelector('#quote-text')
            results.innerText =  responseTEXT})
}
  
const quoteButton = document.querySelector('#get-quote-button');
quoteButton.addEventListener('click', showQuote);