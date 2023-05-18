const notis = document.getElementsByClassName('noti');
for (noti of notis) {
	const toast = new bootstrap.Toast(noti)
    toast.show()
}
