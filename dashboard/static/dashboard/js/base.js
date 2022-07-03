$(window).on('load', function () {
    setTimeout(function () {
        $(".loading-page").hide()
        $(".extend-content").show()
        $('#loading').hide();
    }, 500);
    pageReady()
});


function pageReady() {
    // loading page js
    $(document).ready(function () {
        $("#sidebarCollapse").click(function () {
            $("#sidebar").toggleClass('active');
            $("#content").toggleClass('active');
            if ($(window).width() < 768) {
                $("#nav-menu").toggleClass('navbar-mobile-view');
                $("#sidebar").toggleClass('mobile');
                $("#nav-items").toggleClass('flex-row-reverse');
            }
        });
    });
}
