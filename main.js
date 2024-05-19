// Used Jquery for animation of heading
$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn"
        },
        out:{
            effect: 'bounceOut'
        }
    })
});
