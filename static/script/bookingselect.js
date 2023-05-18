const dateinput = document.querySelector("#date");
const typeinput = document.querySelector("#type");
const timebox = document.querySelector("#time");
const myButton = document.getElementById("booknow");

typeinput.addEventListener("change", () => {
  check();
});

dateinput.addEventListener("change", () => {
  fetch("/api/")
    .then((response) => response.json())
    .then((data) => {
      const exists = data.some((obj) =>
        Object.values(obj).includes(dateinput.value)
      );
      if (exists) {
        timebox.hidden = false;
        document.querySelector("#notexit").innerHTML = "";
      } else {
        timebox.hidden = true;
        document.querySelector("#notexit").innerHTML = "Slot does not exit!";
      }
     
      
      myButton.setAttribute("aria-disabled", "true");

    })
    .catch((error) => console.log("fetch error"));
});

function check() {
  if (typeinput.value != "Select") {
    try {
      document.querySelector("#time input:checked").value;
      myButton.setAttribute("aria-disabled", "false");
    } catch (error) {
      console.log("not selected");
    }
  }
}

timebox.addEventListener("change", function () {
  check();
});
