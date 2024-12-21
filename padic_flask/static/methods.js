function copyResult() {
      // Get the text field
      const copyText = document.getElementById("result").innerText;
      console.log(copyText);

      // Select the text field
      // copyText.select();
      // copyText.setSelectionRange(0, 99999); // For mobile devices
       
      // Copy the text inside the text field
      navigator.clipboard.writeText(copyText)
        .then(() => {
          console.log('Result copied to clipboard: ' + copyText);
        })
        .catch(err => {
          console.error('Failed to copy output: ' + err);
        });
      };