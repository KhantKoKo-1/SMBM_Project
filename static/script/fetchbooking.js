const csrf = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
var delbuttons = document.querySelectorAll('button.delete');

if (delbuttons) {
	delbuttons.forEach(function(delbut){
	    delbut.addEventListener('click', function(){cancel(this.dataset.link)});
	});
}

const resendlink = document.getElementById('resend')

if (resendlink) {
	resendlink.addEventListener('click', function(){
		buttonloading(this);
		resend(location.href, this.parentElement)
	});
}

function resend(link, noti) {
	fetch(link, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
	        'X-CSRF-TOKEN': csrf
		},
		body: JSON.stringify({
			action: 'mail'
		})
	})
	.then(response => response.text())
	.then(msg => {
		noti.innerHTML = msg;
		const notitoast = bootstrap.Toast.getOrCreateInstance(noti);
		notitoast.show()
	})
	.catch(error => {
		console.error(error);
	});
}

function cancel(link) {
    if (confirm('Bookings are non-refundable. Do you stiil want to cancel?')) {
        fetch(link, {
		    method: 'DELETE',
		    headers: {
		        'Content-Type': 'application/json',
		        'X-CSRF-TOKEN': csrf
		    }
		})
		.then(response => response.json())
		.then(data => {
		    console.log('Success:', data);
		    location.reload();
		})
		.catch((error) => {
		    console.error('Error:', error.message);
		});
	}
}
