$(document).ready(function() {
  console.log('ready!');
  $(".leftHandCard").click(function() {
    let courseName = $(this).attr('data-coursename')
    clearSelectedCards();
    $(this).addClass('selectedCard');
    clearCards();
    $("#selectACourse").hide();
    $("#courseinfo_" + courseName).show();
  });
  $("#otherCoursesOption").click(function(){
    $("#myCoursesHub").hide();
    $("#otherCoursesHub").show();
  });
  $("#myCoursesOption").click(function(){
    $("#myCoursesHub").show();
    $("#otherCoursesHub").hide();
  });
});

function clearCards() {
  $('#infoContainer').children().each(function () {
    $(this).hide();
  });
}

function clearSelectedCards() {
  $('.courseListContainer').children().each(function () {
    $(this).removeClass('selectedCard');
  });
}