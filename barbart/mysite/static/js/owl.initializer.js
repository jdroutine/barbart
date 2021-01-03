
$('.owl-carousel').owlCarousel({
  loop:true,
  autoplay: true,
  margin:20,
  nav:true,
  navText: ["<i class='fas fa-chevron-circle-left'></i>", 
  "<i class='fas fa-chevron-circle-right'></i>"],
  responsive:{
    0:{
        items:1
    },
    600:{
        items:3
    },
    1000:{
        items:4,
    }
}
})
