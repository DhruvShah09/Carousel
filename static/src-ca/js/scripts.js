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
var time1 = document.getElementById("start-selection");
var timeadd;
var timeadd1;
var frontend = "";

var startTime = time1.value.substring(0, 2);
var backend = time1.value.substring(2);
if (startTime.charAt(1) == ':') {
    startTime = startTime.substring(0, 1);
    backend = time1.value.substring(1);
}


var useStartTime = parseInt(startTime);

var ap1 = document.getElementById("am/pm1");
if(ap1.value == "p.m.") {
    timeadd = " p.m.";
    timeadd1 = 12;
}
else {
    timeadd = " a.m."
    timeadd1 = 0;
}
if (time1.value == 12) {
    useStartTime = 0;
}
var timeComp = useStartTime + timeadd1;

if(timeComp < 10 && timeadd == " a.m.") {
    frontend = "0";
}
else { 
    frontend = "";
}


if (time1 != null) {
    time1.addEventListener("click", function() {
        var options = time1.querySelectorAll("option");
        var count = options.length;
        if(typeof(count) === "undefined" || count < 2)
        {
            addTimeItem();
        }
    });
}

if (time1 != null) {
    time1.addEventListener("change", addTimeItem2, false);
 }

 if(ap1 != null) {
     ap1.addEventListener("change", addTimeItem2, false);
 }

function addTimeItem2() {
//     if (i == 1) {
//         console.log(time1.value);
//     } else {
//         var finalEndTime = time1.value;
//         console.log(finalEndTime);
//     }

//convertToUnix();}
startTime = time1.value.substring(0, 2);

backend = time1.value.substring(2);

if (startTime.charAt(1) == ':') {
    startTime = startTime.substring(0, 1);
    backend = time1.value.substring(1);
}


useStartTime = parseInt(startTime);



ap1 = document.getElementById("am/pm1");
if(ap1.value == "p.m.") {
    timeadd = " p.m.";
    timeadd1 = 12;
}
else {
    timeadd = " a.m."
    timeadd1 = 0;
}

timeComp = useStartTime + timeadd1;



if (useStartTime==12) {
    useStartTime = 0;
}




if(ap1.value == "p.m.") {
timeadd = " p.m.";
}
else {
timeadd = " a.m.";
}


if(timeComp < 10 && timeadd == " a.m.") {
    frontend = "0";
}
else {
    frontend = "";
}


var startTimeFinal = (frontend + (useStartTime + timeadd1) + backend);
if (useStartTime == 0 && timeadd == " a.m.") {
    startTimeFinal = "00" + backend;
}
else if (useStartTime == 0 && timeadd == " p.m.") {
    startTimeFinal = "12" + backend;
}
console.log(startTimeFinal);
}
    // }

    var time2 = document.getElementById("end-selection");
    var timeadd2;
    var timeadd3;
    var frontend2 = "";

    var endTime = time2.value.substring(0, 2);
    var backend2 = time2.value.substring(2);
    if (endTime.charAt(1) == ':') {
        endTime = endTime.substring(0, 1);
        backend2 = time2.value.substring(1);
    }


    var useEndTime = parseInt(endTime);
    
    var ap2 = document.getElementById("am/pm2");
    if(ap2.value == "p.m.") {
        timeadd2 = " p.m.";
        timeadd3 = 12;
    }
    else {
        timeadd2 = " a.m."
        timeadd3 = 0;
    }
    if (time2.value == 12) {
        useEndTime = 0;
    }
 var timeComp2 = useEndTime + timeadd3;

    if(timeComp2 < 10 && timeadd2 == " a.m.") {
        frontend2 = "0";
    }
    else { 
        frontend2 = "";
    }


    if (time2 != null) {
        time2.addEventListener("click", function() {
            var options = time2.querySelectorAll("option");
            var count = options.length;
            if(typeof(count) === "undefined" || count < 2)
            {
                addTimeItem();
            }
        });
    }

    if (time2 != null) {
        time2.addEventListener("change", addTimeItem, false);
     }

     if(ap2 != null) {
         ap2.addEventListener("change", addTimeItem, false);
     }
    
    function addTimeItem() {
    //     if (i == 1) {
    //         console.log(time1.value);
    //     } else {
    //         var finalEndTime = time1.value;
    //         console.log(finalEndTime);
    //     }

//convertToUnix();}
    endTime = time2.value.substring(0, 2);

    backend2 = time2.value.substring(2);

    if (endTime.charAt(1) == ':') {
        endTime = endTime.substring(0, 1);
        backend2 = time2.value.substring(1);
    }


    useEndTime = parseInt(endTime);


    
    ap2 = document.getElementById("am/pm2");
    if(ap2.value == "p.m.") {
        timeadd2 = " p.m.";
        timeadd3 = 12;
    }
    else {
        timeadd2 = " a.m."
        timeadd3 = 0;
    }

    timeComp2 = useEndTime + timeadd3;



    if (useEndTime==12) {
        useEndTime = 0;
    }




if(ap2.value == "p.m.") {
    timeadd2 = " p.m.";
}
else {
    timeadd2 = " a.m.";
}


    if(timeComp2 < 10 && timeadd2 == " a.m.") {
        frontend2 = "0";
    }
    else {
        frontend2 = "";
    }


    var endTimeFinal = (frontend2 + (useEndTime + timeadd3) + backend2);
    if (useEndTime == 0 && timeadd2 == " a.m.") {
        endTimeFinal = "00" + backend2;
    }
    else if (useEndTime == 0 && timeadd2 == " p.m.") {
        endTimeFinal = "12" + backend2;
    }
    console.log(endTimeFinal);
}

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

//convert to Unix time
function convertToUnix() {
    console.log(Math.round(new Date(date.value).getTime()/1000));

    //if ()

}

//called when button "Find a Group" is pressed
function sendPostRequest() {
    if (date != null && date.value != "mm/dd/yyyy" && time1 != null) { //check that all fields aren't null
        //add post request here (dhruv)
        //send unix value 
    } else {
        alert("Please fill out all required fields (Date, Start Time, End Time, a.m./p.m.) and try again.");
    }
}
