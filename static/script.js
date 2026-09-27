console.log("Student Registration Service Loaded Successfully.");

const recordsLink = document.getElementById("records-link");
if (recordsLink) {
    recordsLink.href = `${window.location.protocol}//${window.location.hostname}:5002/`;
}
