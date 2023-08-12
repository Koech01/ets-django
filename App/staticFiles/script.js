//Explore delete dropdown
function addModal() {
    var modal    = document.getElementById("addModalDiv");
    var close    = document.getElementById("modalCloseBtn");
    if (modal.style.display !== "block") {
      $(modal).transition('fade');
      window.onclick = function(event) { 
        if (event.target == modal) {    $(modal).transition('fade');    }
      }
      close.onclick = function(){closeModalPopup(modal)};
    } else {
      modal.style.display = "none";
    }
}

function closeModalPopup(modal) { $(modal).transition('fade');    }