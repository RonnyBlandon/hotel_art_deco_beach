/* switch For menu buttons */
// We use regular expressions to compare the pathnames
const start = /^(\/es)?\/$/;
const rooms = /^(\/es)?\/rooms\/$/;
const introduction = /^(\/es)?\/introduction\/$/;
const gallery = /^(\/es)?\/gallery\/$/;
const contact = /^(\/es)?\/contact\/$/;

let pathname = window.location.pathname;
let linkMenuPage = "";
switch (true) {
    case start.test(pathname):
        linkMenuPage = document.getElementById("home")
        linkMenuPage.classList.add("active");
        break;
    case rooms.test(pathname):
        linkMenuPage = document.getElementById("rooms")
        linkMenuPage.classList.add("active");
        break;
    case introduction.test(pathname):
        linkMenuPage = document.getElementById("introduction")
        linkMenuPage.classList.add("active");
        break;
    case gallery.test(pathname):
        linkMenuPage = document.getElementById("gallery")
        linkMenuPage.classList.add("active");
        break;
    case contact.test(pathname):
        linkMenuPage = document.getElementById("contact")
        linkMenuPage.classList.add("active");
        break;
};
