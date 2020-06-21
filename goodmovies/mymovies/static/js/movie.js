var updateBtns = document.getElementsByClassName('update-cart')

for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var movie_id = this.dataset.movie
        var action = this.dataset.action
        var user_id = this.dataset.user
        console.log('movie_id:',movie_id, 'Action:',action, 'User',user_id)

        update_movie(movie_id, action,user_id)

        })
}


function update_movie(movie_id, action,user_id){
        console.log('User is logged in, sending data..')
        var url  = '/add_movie/'
        var csrftoken = getCookie('csrftoken')

        fetch(url,
            { method: 'POST',
              headers: {
              'Content-Type':'application/json',
              'X-CSRFToken' : csrftoken,
              },
              body:JSON.stringify({'movie_id' : movie_id, 'action':action,
               'user_id': user_id})
              })
              .then((response) =>{
                return response.json()
              })
              .then((data) => {
                console.log('data:',data)
                location.reload()
              })
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}