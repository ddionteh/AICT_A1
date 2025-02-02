document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".sidebar li").forEach(item => {
        item.addEventListener("click", function () {
            let section = this.getAttribute("data-section");
            loadContent(section);
        });
    });
});

function loadContent(section) {
    console.log(`Fetching data for: ${section}`); // ✅ Debugging Log
    document.getElementById('content').innerHTML = `<h2>Loading ${section}...</h2>`;

    fetch(`/api/${section}/test`)
        .then(response => {
            if (!response.ok) throw new Error("API Not Found");
            return response.json();
        })
        .then(data => {
            document.getElementById("content").innerHTML = `<h2>${section}</h2><p>${data.message}</p>`;
        })
        .catch(error => {
            console.error("Error fetching data:", error);
            document.getElementById("content").innerHTML = `<h2>Error</h2><p>Could not load data.</p>`;
        });
}



// Example: Chart.js Graph for Route Planning
document.addEventListener("DOMContentLoaded", function () {
    var ctx = document.getElementById('routeGraph').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['A', 'B', 'C', 'D', 'E'],
            datasets: [{
                label: 'Example Route Path',
                data: [10, 20, 15, 30, 25],
                borderColor: 'blue',
                borderWidth: 2
            }]
        }
    });
});
