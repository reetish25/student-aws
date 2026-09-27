console.log("Student Records Service Loaded Successfully.");

const registrationLink = document.getElementById("registration-link");
if (registrationLink) {
    registrationLink.href = `${window.location.protocol}//${window.location.hostname}:5001/`;
}

function filterTable() {
    const input = document.getElementById("search");
    if (!input) return;
    const filter = input.value.toLowerCase();
    const rows = document.querySelectorAll("#records-table tbody tr");
    rows.forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(filter) ? "" : "none";
    });
}
