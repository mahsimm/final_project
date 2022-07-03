let firstParameter = new URL(window.location.href).search.slice(1);
let searchParameter;

if (firstParameter) {
    searchParameter = new URLSearchParams(firstParameter)
} else {
    searchParameter = new URLSearchParams()
}

let getShoppingURL = "/dashboard/shopping/?";
$(function () {

    // set menu active
    $("#shoppingMenu").addClass("active-menu");

    pagination(urlMaker())
});


// function for get Request.GET variable
function getUrlParameter(url, param) {
    urlArray = url.split("/");
    paramets = urlArray[urlArray.length - 1];
    const urlParams = new URLSearchParams(paramets);
    return urlParams.get(param)
}

function urlMaker() {
    return getShoppingURL + searchParameter
}

function loading() {
    $(".card-group").show();
}

window.onpopstate = function (event) {
    pagination(event.state.url)
};

function pagination(url) {
    // get JSON and Response Header
    $.ajax({
        url: url,
        type: "GET",
        dataType: "json",
        success: function (shoppingCards, textStatus, request) {
            $(".card-group").empty();
            $(".pagination").empty();
            renderShoppingCards(shoppingCards);
            // check if page number is not 0 show pagination
            if (shoppingCards == 0) {
                let notFoundCourseTemplate = `
                <div class="container w-100 p-1 text-center vazir-bold">
                    <div class="col-md-12">
                        <p class="text-center" style="font-size: 25px;">محصول با این ویژگی ها یافت نشد !</p>
                        <p class="text-center vazir-light" style="font-size: 20px;">با ویژگی های دیگر امتحان کنید</p>
                    </div>
                </div>
                `;
                $(".card-group").append(notFoundCourseTemplate);
            }
        },
        error: function () {
            alert("خطا در بارگزاری محصولات ... لطفا دوباره امتحان کنید!")
        },
    });
}

function renderShoppingCards(shopCards) {
    $.each(shopCards, function (index, card) {
        try {
            let shoppingCardTemplate = `
            <div class="col-md-4 mb-3">
               <div class="card course-card h-100">
                  <!-- Course poster -->
                  <img class="card-img-top" src="${card.image}">
                  <!-- Course content -->
                  <div class="card-body">
                     <h4 class="title ">${card.title}</h4>
                                         <div class="course-price">
                        <p style="text-align: center ; color: #e8505b">
                           قیمت:
                           <span class="price">  ${card.amount}
                <span class="currency">تومان</span>
                        </p>
                     </div>

                  </div>
               </div>
            </div>
        `;
            $(".card-group").append(shoppingCardTemplate);

        } catch (error) {
            console.log("failed to add shopping card", error);
        }


    });
    loading()
}


$("select[id^='search']").change(function (event) {
    if ($(this).val() != "none") {
        searchParameter.set($(this).data("search"), $(this).val());
    } else {
        searchParameter.delete($(this).data("search"));
    }
    history.pushState({url: urlMaker()}, null, "?" + searchParameter);
    pagination(urlMaker())
});
$("input[id^='search']").on('keyup', function (e) {
    if ($(this).val() != "none") {
        searchParameter.set($(this).data("search"), $(this).val());
    } else {
        searchParameter.delete($(this).data("search"));
    }
    history.pushState({url: urlMaker()}, null, "?" + searchParameter);
    pagination(urlMaker())
});


