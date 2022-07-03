$("#username").on("keyup", function () {
    let userNameREgex = /^[a-zA-Z0-9]+$/;
    handleAlert(userNameREgex.test($(this).val()) || !$(this).val(), $(this), "نام کاربری تنها باید شامل حروف و اعداد انگلیسی باشد.")
});
$("#email").on("keyup", function () {
    let emailRegEx = /^\S+@\S+\.\S+$/;
    handleAlert(emailRegEx.test($(this).val()) || !$(this).val(), $(this), "ایمیل وارد شده معتبر نمی باشد.")
});

$("#password").on("keyup", function () {
    var p = $(this).val();
    errors = [];
    if (p.length < 8) {
        errors.push("طول رمز عبور حداقل باید 8 باشد");
    }
    if (p.search(/[a-z]/) < 0) {
        errors.push("رمز عبور باید دارای حرف کوچک باشد");
    }
    if (p.search(/[A-Z]/) < 0) {
        errors.push("رمز عبور باید دارای حرف بزرگ باشد");
    }
    if (p.search(/[0-9]/) < 0) {
        errors.push("رمز عبور باید دارای عدد باشد");
    }
    handleAlert(errors.length == 0 || !$(this).val(), $(this), errors);
});


function haveAlert() {
    return $("#usernameAlert").is(":visible") ||
        $("#emailAlert").is(":visible") ||
        $("#passwordAlert").is("visible");
}

function handleAlert(bool, prop, text) {
    if (bool) {
        prop.siblings("small").hide();
        if (!haveAlert())
            $("#submit").prop("disabled", false);
    } else {
        prop.siblings("small").show();
        prop.siblings("small").text(text);
        $("#submit").prop("disabled", true);
    }
}
