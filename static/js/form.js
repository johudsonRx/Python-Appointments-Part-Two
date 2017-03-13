$(document).ready(function() {

	var queryTerm = "";



    $('form').on('submit', function(event) {

        $.ajax({
                data: {
                    date: $('#Date').val(),
                    time: $('#Time').val(),
                    description: $('#Description').val()
                },
                method: 'POST',
                url: '/process'
            })
            .done(function(data) {

                // if (data.error) {
                //     $('#errorAlert').text(data.error).show();
                //     $('#successAlert').hide();
                // } else {
                //     $('#successAlert').text(data.name).show();
                //     $('#errorAlert').hide();
                // }
                console.log(data);
              

            });

        event.preventDefault();

    });

    function runQuery(){
    	$.ajax({url: '/process', method: "GET"})
		.done(function(AppointmentData) {
         console.log(AppointmentData);

    })

	}

   $('#getappointments').on('click', function(event) {
                   
        queryTerm = $('#search').val().trim()

       runQuery();
       console.log(runQuery());
   });



});