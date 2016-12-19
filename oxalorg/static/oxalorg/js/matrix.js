// Canvas

var c = document.getElementById("c");
var ctx = c.getContext("2d");

window.onresize = function onresize() {
	width = c.width = window.innerWidth;
	height = c.height = window.innerHeight;
}

window.onresize();

var matrix_char = "0123456789@#$%^&*aBcCoOqsStuVwXzZ田由甲申甴电甶男甸甹町画甼甽甾甿畀畁畂畃畄畅畆畇畈畉畊畋界畍畎畏畐畑";
matrix_char = matrix_char.split("");


var font_size = 20;
var columns = c.width/font_size;
var drops = [];

for(var x = 0; x < columns; x++)
    drops[x] = c.height + 10;

var colors = ["#00bbff", "#0F0", "#a8a0ff", "#ffa73d"];
var currentColor = "#00bbff"; // Default Color value

var drawTime = 50;
var drawTimeValues = [40, 60, 80];

// these 3 lines control terminal view
var terminal = document.getElementById("terminal");
terminal.style["border-color"] = currentColor;
arkControl.setTextColor(currentColor);

function draw()
{
    ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
    ctx.fillRect(0, 0, c.width, c.height);

    ctx.font = font_size + "px arial";

    for(var i = 0; i < drops.length; i++)
    {
        ctx.fillStyle = currentColor;
        var text = matrix_char[Math.floor(Math.random()*matrix_char.length)];
        ctx.fillText(text, i*font_size, drops[i]*font_size);

        if(drops[i]*font_size > c.height && Math.random() > 0.975)
            drops[i] = 0;

        drops[i]++;
    }
}

var anim = setInterval(draw, drawTime);

function randomize_matrix()
{
    var tempColor = currentColor;
    while(currentColor == tempColor){
        currentColor = colors[Math.floor(Math.random()*colors.length)];
    }
    // these two lines control terminal view
    terminal.style["border-color"] = currentColor;
    arkControl.setTextColor(currentColor);

    var tempTime = drawTime;
    while(drawTime == tempTime){
        drawTime = drawTimeValues[Math.floor(Math.random()*drawTimeValues.length)];
    }

    clearInterval(anim);
    anim = setInterval(draw, drawTime);
}
