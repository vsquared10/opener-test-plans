$(document).ready(function() {

  $('td').each(function () {
    switch($(this).text()) {
      case 'low':
        break;
      case 'moderate':
        $(this).parent().addClass("bg-warning");
        break;
      case 'high':
        $(this).parent().css({"background-color": "#fd7e14"});
        break;
      case 'severe':
        $(this).parent().addClass("bg-danger");
        break;
      case 'Fully Approved - In Progress':
        $(this).parent().addClass("bg-success");
        break;
      default:
        break;
    };
  });

  // $('.fas').on("click", function() {
  //   $(this).toggleClass("fa-sort-up fa-sort-down");
  //   console.log($(this).parent().text().toLowerCase());
  // });

});
