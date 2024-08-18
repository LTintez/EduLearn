function message_error(obj){
    var html = '';
    if(typeof(obj)==='object'){

        html ='<ul style="text-align: left;">';
        $.each(obj, function(key,value){
            html+='<li>'+key+ ': '+value+ '</li>';
        });
        html += '</ul>';
    }
    else{
        html = '<p>'+ obj +'</p>'
    }
   
    Swal.fire({
        title: "Error!",
        html: html,
        icon: "error",
        confirmButtonText: "Salir",
      });
}


function submit_ajax(url,parameters,title,content,callback){
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        dragable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: 'Si',
                btnClass: 'btn-primary',
           
            action: function () {
                parameters['csrfmiddlewaretoken']= $('input[name="csrfmiddlewaretoken"]').val()
                $.ajax({
                    url: url,// window.location.pathname,
                    type: "POST",
                    data: parameters,
                    dataType: "json",
                    processData: false,
                    contentType:false,
                  }).done(function (data) {

                      if(!data.hasOwnProperty('error')){
                        callback();
                        return false;
                      }
                      message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorTrhown) {
                      alert(textStatus + " : " + errorTrhown);
                    }).always(function (data) {
                        
                    });
            }
        }, 
            danger:{
                text: 'no',
                btnClass: 'btn-red',
            
            action: function () {
                $.alert('Canceled!');
            }
        },
        }
    });
         
}