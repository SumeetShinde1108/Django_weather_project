document.addEventListener('DOMContentLoaded', function () {
    console.log('Document loaded, attempting to fetch weather data...');

    fetch('/weather/')
        .then(response => {
            console.log('Received response from API');
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json();
        })
        .then(data => {
            debugger
            console.log('Data fetched from API:', data);
            const tableBody = document.getElementById('weather-table').querySelector('tbody');
            tableBody.innerHTML = '';  // Clear any existing content
            data.forEach(item => {
                console.log('Data fetched from API:', item);
                const row = document.createElement('tr');
                const dateCell = document.createElement('td');
                const valueCell = document.createElement('td');
                dateCell.textContent = item.date;
                valueCell.textContent = item.value;
                row.appendChild(dateCell);
                row.appendChild(valueCell);
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            document.getElementById('weather-table').querySelector('tbody').innerHTML = '<tr><td colspan="2">Error loading data</td></tr>';
        });
});
