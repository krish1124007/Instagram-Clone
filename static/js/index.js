document.addEventListener("DOMContentLoaded", function() {
    var commentButtons = document.querySelectorAll(".comment-btn");
    commentButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            var commentContainer = this.parentElement.nextElementSibling;
            commentContainer.classList.toggle("active");
        });
    });
});