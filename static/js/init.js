$(document).ready(function () {
  console.log('Patrick Copp 1007602');

  $('#register').on('click',function () {
    $.ajax({
      type: "POST",
      url: "/register",
      data: $('#myForm').serialize(),
      success: function(data)
      {
        if(data)
          $("#XD").text("Registered!");
        else
          $("#XD").text("Registration failed!");
      },
      dataType: 'json'
    });
  });
  $('#login').on('click',function () {
    $.ajax({
      type: "POST",
      url: "/login",
      data: $('#myForm').serialize(),
      success: function (data) {
        location.reload();
      }
    });
  });
  $('#logout').on('click',function () {
    $.ajax({
      type: "POST",
      url: "/logout",
      data: $('#myForm').serialize(),
      success: function (data) {
        location.reload();
      }
    });
  });
});