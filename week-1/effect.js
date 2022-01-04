$(document).ready(function() {
    $('.menu').on('click',  function(e){
       e.preventDefault();
       $('body').toggleClass('menu-show');
   });
 });