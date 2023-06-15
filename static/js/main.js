function openFunction() {
  var overlay = document.querySelector('.overlay');
  var popup = document.querySelector('.popup');

  overlay.style.display = 'block';
  popup.style.display = 'block';
}


function closeFunction() {
  var overlay = document.querySelector('.overlay');
  var popup = document.querySelector('.popup');

  overlay.style.display = 'none';
  popup.style.display = 'none';
}

function submitFunction(row) {
  const kursus = {
    nama: document.getElementById('nama').value,
    alamat: document.getElementById('alamat').value,
    telpon: document.getElementById('telpon').value,
    gender: document.getElementById('gender').value,
    kursus: document.getElementById('kursus').value,
    tanggal: document.getElementById('tanggal').value,
    id: row[0] // Add the ID from the row object to update the specific entry
  };

  console.log('Kursus data:', kursus);

  // Perform any further actions with the kursus data, such as sending it to the server or performing client-side processing.

  // For example, you can send the kursus data to a server using fetch:
  const url = 'http://127.0.0.1:5000/update'; // Change the URL to the endpoint for updating data
  fetch(url, {
    method: 'POST',
    body: new URLSearchParams(Object.entries(kursus)),
  })
    .then(response => {
      if (response.ok) {
        console.log('Kursus updated successfully');
      } else {
        console.error('Error updating kursus:', response.statusText);
        // Handle error case, such as showing an error message to the user.
      }
    })
    .catch(error => {
      console.error('Error updating kursus:', error);
      // Handle error case, such as showing an error message to the user.
    });

  var overlay = document.querySelector('.overlay');
  var popup = document.querySelector('.popup');
  overlay.style.display = 'none';
  popup.style.display = 'none';
}
