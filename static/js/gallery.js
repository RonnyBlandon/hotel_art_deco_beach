document.addEventListener('DOMContentLoaded', function () {
    var imageModal = document.getElementById('imageModal');
    var carouselElement = document.getElementById('carouselExample');
    var modalTitle = document.getElementById('imageModalLabel');

    imageModal.addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        var title = button.getAttribute('data-title');
        var slideTo = button.getAttribute('data-slide-to');
        var carousel = new bootstrap.Carousel(carouselElement);

        carousel.to(slideTo);
        modalTitle.textContent = title;
    });

    carouselElement.addEventListener('slid.bs.carousel', function () {
        var activeItem = carouselElement.querySelector('.carousel-item.active');
        var title = activeItem.querySelector('img').getAttribute('alt');
        modalTitle.textContent = title;
    });
});
