function copyResult() {
      // Get the text field
      const copyText = document.getElementById("result").innerText;
      // console.log(copyText);

      // Copy the text inside the text field
      navigator.clipboard.writeText(copyText)
        .then(() => {
          alert('Result copied to clipboard: ' + copyText);
        })
        .catch(err => {
          console.error('Failed to copy output: ' + err);
        });
      }

function showResult(datatype) {
      const result = document.getElementById("result");
      result.innerText = result.dataset[datatype];
      console.log('Updated result: ' + result.innerText);
      }

function showAlert() {
      const alert = document.getElementById("alert");
      input.innerText = input.dataset[datatype];
      console.log('Updated input: ' + input.innerText);
      }