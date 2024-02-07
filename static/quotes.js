// const quotes_form = document.querySelector('#quote_update');

// quotes_form.addEventListener('submit', (evt) => {
//     evt.preventDefault();

//     const formAnswer = {
//         new_quote: document.querySelector('#quotes').value,
//         quote_update: document.querySelector('#quote_update').value
//     };

//     fetch('/quote_update', {
//         method: 'POST',
//         body: JSON.stringify(formAnswer),
//         headers: {
//             'Content-Type': 'application/json'
//         },
//     })

//     .then((response) => response.json())
//     .then((responseJSON) => {
//         notes_h2.innerHTML = responseJSON.notes;
//     })
// })
