function selectCustomer(id) {
  var user_id = event.currentTarget.getAttribute("data-user-id");

  fetch("/api2/")
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      data.forEach((users) => {
        if (user_id == users.user_id) {
          document.getElementById("incoming_msg").innerHTML = `
              <div class="incoming_msg_img">
              <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil">
            </div>
            <div class="received_msg">
              <div class="received_withd_msg">
                <p>${users.message}</p><span class="time_date">an hour ago</span></div>
               </div>
              
              `;
        }

        console.log(users.user_id, users.message);
      });
    })
    .catch((error) => console.error(error));
}
