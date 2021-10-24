//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

//function which grabs today's date and sets <select> attributes
function getTodaysDate() {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; //January is 0!
    var yyyy = today.getFullYear();
                    
    if (dd < 10) {
        dd = '0' + dd;
    }
                    
    if (mm < 10) {
        mm = '0' + mm;
    }
                        
    today = yyyy + '-' + mm + '-' + dd;

    document.getElementById("date-input").setAttribute("min", today);
    document.getElementById("date-input").setAttribute("value", today);
}

//listen for date and time dropdowns to be selected, then send fields to backend
//date:
var date = document.getElementById("date-input");

date.addEventListener("click", function() {
    var options = date.querySelectorAll("option");
    var count = options.length;
    if(typeof(count) === "undefined" || count < 2)
    {
        addDateItem();
    }
});

date.addEventListener("change", addDateItem, false);

function addDateItem() {
    console.log(date.value);

    convertToUnix();
}

// //start and end times:
// // for (var i = 1; i <= 2; i++) {
// //     var time = document.getElementById(i == 1 ? "start" : "end" + "-selection");
    var time = document.getElementById("start-selection");

    if (time != null) {
        time.addEventListener("click", function() {
            var options = time.querySelectorAll("option");
            var count = options.length;
            if(typeof(count) === "undefined" || count < 2)
            {
                addTimeItem();
            }
        });
    }

    if (time != null) {
        time.addEventListener("change", addTimeItem, false);
    }
    
    function addTimeItem() {
        // if (i == 1) {
            console.log(time.value);
        // } else {
        //     var finalEndTime = time.value;
        //     console.log(finalEndTime);
        // }

        convertToUnix();
    }
// }

// //am/pm:
// for (var i = 1; i <= 2; i++) {
//     var select = document.getElementById("am/pm" + i);

//     if (select != null) {
//         select.addEventListener("click", function() {
//             var options = select.querySelectorAll("option");
//             var count = options.length;
//             if(typeof(count) === "undefined" || count < 2)
//             {
//                 addSelectItem();
//             }
//         });
//     }

//     if (select != null) {
//         select.addEventListener("change", function() {
//             if(select.value == "addNew")
//             {
//                 addSelectItem();
//             }
//         });
//     }
    
//     function addSelectItem() {
//         if (i == 1) {
//             var finalSelection1 = select.value;
//             console.log(finalSelection1);
//         } else {
//             var finalSelection2 = select.value;
//             console.log(finalSelection2);
//         }

//         convertToUnix();
//     }
// }

//convert to Unix time, then send to backend
function convertToUnix() {
    console.log(Math.round(new Date(date.value).getTime()/1000));

    //add post request here (dhruv)
}
