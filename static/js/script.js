// Get the modal
var modal = document.getElementById("insertTestCase");
var testCaseModal;

// Get the button that opens the modal
var btn = document.getElementById("insertTestCaseBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
    testCaseModal.display = "none"
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
    if (event.target === testCaseModal) {
        testCaseModal.style.display = "none";
    }
}

function openModal(modalId) {
    var modal = document.getElementById(modalId);
    testCaseModal = modal;
    modal.style.display = "block";
}

function closeModal(modalId) {
    var modal = document.getElementById(modalId);

    modal.style.display = "none";
}

