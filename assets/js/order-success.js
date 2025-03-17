window.onload = function () {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has("order_success")) {
        alert("Thank you for your order! We will get back to you soon.");
        history.replaceState({}, document.title, "/"); // Removes query param
    }
};