
var north_state = Array(true, true, true);

var ui_clock = Array("#second", "#minute", "#hour");
var clock_laps = Array(60, 60, 24);

var next_gap = function(idx) {
    var el = ui_clock[idx];
    var max_val = parseInt($(el + "_lap").text());
        

    if (north_state[idx]) { 
        if (idx != 1) {
            var next = (parseInt($(".south", el).text()) + 2) % max_val;
            $(".south", el).text(next);
        } else {
            var next = (parseInt($(".south .left", el).text()) * 10 +
                        parseInt($(".south .right", el).text()) + 2) % max_val;
            $(".south .left", el).text(Math.floor(next/10));
            $(".south .right", el).text(next % 10);
        }
        $(".north", el).addClass("north_step_one");
        $(".south", el).addClass("south_step_one");
        $(".north", el).removeClass("north_step_two");
        $(".south", el).removeClass("south_step_two");
    } else {
        if (idx != 1) {
            var next = (parseInt($(".north", el).text()) + 2) % max_val;
            $(".north", el).text(next);
        } else {
            var next = (parseInt($(".north .left", el).text()) * 10 +
                        parseInt($(".north .right", el).text()) + 2) % max_val;
            $(".north .left", el).text(Math.floor(next/10));
            $(".north .right", el).text(next % 10);
        }
        $(".north", el).addClass("north_step_two");
        $(".south", el).addClass("south_step_two");
        $(".north", el).removeClass("north_step_one");
        $(".south", el).removeClass("south_step_one");
    }
    
    if (next == 0) {
        if (idx < 2)
            next_gap(idx + 1)
    }

    north_state[idx] = !north_state[idx];

    return;
}

$(document).ready(function() {
    /* Binding hover functions to each old prime */
    /* Function when mouse is over */
    $("#trigger").click(function() {
        next_gap(0);
        next_gap(1);
        next_gap(2);
    });
    setInterval(function() {
        next_gap(0);
    }, 1000);
});
