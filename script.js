const form = document.getElementById('converter-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const amount = parseFloat(document.getElementById('amount').value);
  const response = await fetch('/convert', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `amount=${amount}`
  });
  const data = await response.json();
  resultDiv.innerHTML = `<p>${amount} dollars = ${data.euro.toFixed(2)} euros</p>`;
});
