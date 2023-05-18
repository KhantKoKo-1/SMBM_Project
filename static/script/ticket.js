document.getElementById("adult").value = 0;
document.getElementById("concession").value = 0;
document.getElementById("child").value = 0;


const cart = document.getElementById("cart");
const cartable = cart.getElementsByTagName("tbody")[0];
const cartmeta = cart.getElementsByTagName("tfoot")[0];
const paybutton = document.getElementById("checkout");
const whydisabled = new bootstrap.Tooltip(paybutton);
const totaltd = document.getElementById("pricetotal");
const paxtd = document.getElementById("pax");
const ticketcount = document.getElementById("ticketsleft");
const soldoutmsg = document.getElementById("soldout");
const carterror = document.getElementById("cart-error");
const form = document.getElementById("bookingtickets");

var notifyerror = true;

Array.prototype.remove = function (value) {
  return this.splice(this.indexOf(value), 1);
};

function addticket(ticketype, price) {
  console.log(ticketype);

  const typecount = document.getElementById(ticketype + "count");
  typecount.innerText = Number(typecount.innerText) + 1;
  const quantityin = document.getElementById(ticketype);
  if (quantityin) {
    console.log(quantityin);
    quantityin.value = String(Number(quantityin.value) + 1);
    const pricetd = document.getElementById(ticketype + "price");
    console.log(pricetd);
    pricetd.innerHTML = Number(pricetd.innerHTML) + price;
    updateTotal();
  } else {
    addtocart(1, ticketype, price);
  }

  if (ticketype == "Adult") {
      
      document.getElementById("adult").value =document.getElementById("Adult").value;
      document.getElementById("Adult-down").addEventListener("click", () => {
        
      document.getElementById("adult").value =document.getElementById("Adult").value;
      });
      document.getElementById("Adult-up").addEventListener("click", () => {
      document.getElementById("adult").value =document.getElementById("Adult").value;
      });
    
  } else if (ticketype == "Concession") {
    document.getElementById("concession").value =document.getElementById("Concession").value;
    
    document.getElementById("Concession-down").addEventListener("click", () => {
    document.getElementById("concession").value =document.getElementById("Concession").value;
    });
    document.getElementById("Concession-up").addEventListener("click", () => {
      document.getElementById("concession").value =
        document.getElementById("Concession").value;
    });
  } else if (ticketype == "Child") {
    document.getElementById("child").value =document.getElementById("Child").value;
    document.getElementById("Child-down").addEventListener("click", () => {
      document.getElementById("child").value =
        document.getElementById("Child").value;
    });
    document.getElementById("Child-up").addEventListener("click", () => {
      document.getElementById("child").value =
        document.getElementById("Child").value;
    });
  }
  
  
}

function addtocart(quantity, name, price) {
  const row = document.createElement("tr");

  const quantitytd = document.createElement("td");
  const nametd = document.createElement("td");

  if (quantity) {
    const quantin = document.createElement("input");
    quantin.type = "number";
    quantin.id = name;
    quantin.name = name;
    quantin.min = 0;
    quantin.value = quantity;
    quantin.setAttribute("form", "bookingtickets");
    quantin.classList.add("form-control", "form-control-sm", "quantity");
    // .ariaDescribedBy or .ariaDescribedby does not work
    quantin.setAttribute("aria-describedby", name + "-up " + name + "-down");
    quantin.addEventListener("change", function () {
      if (Number(this.value) <= 0) {
        // quantity not natural number
        var rubbish = this.parentElement.parentElement.parentElement;
        rubbish.parentNode.removeChild(rubbish);
      }
      // update add ticket button badge
      const typecount = document.getElementById(name + "count");
      typecount.innerText = this.value;

      updateTotal();
    });

    const inputgroup = document.createElement("div");
    inputgroup.className = "input-group";
    inputgroup.appendChild(stepbutt("-", -1, name + "-down"));
    inputgroup.appendChild(quantin);
    inputgroup.appendChild(stepbutt("+", 1, name + "-up"));
    quantitytd.appendChild(inputgroup);

    const label = document.createElement("label");
    label.setAttribute("for", name);
    label.innerHTML = name;
    nametd.appendChild(label);
  } else {
    nametd.innerHTML = name;
  }
  const pricetd = document.createElement("td");
  pricetd.innerHTML = price;
  pricetd.id = (name + "price").replace(/\s/g, "");

  const deltd = document.createElement("td");
  const delbut = document.createElement("button");
  delbut.type = "button";
  delbut.classList.add("btn", "btn-outline-danger", "btn-sm");
  delbut.addEventListener("click", function () {
    console.log(quantity, name);
    if (name == "Concession") {
      document.getElementById("concession").value = 0;
    } else if (name == "Adult") {
      document.getElementById("adult").value = 0;
    } else {
      document.getElementById("child").value = 0;
    }

    if (quantity) {
      // ticketype
      // update add ticket button badge
      const typecount = document.getElementById(name + "count");
      typecount.innerText = "0";
    } else {
      // reward
      delreward(name);
    }
    // delete row
    var rubbish = this.parentElement.parentElement;
    rubbish.parentNode.removeChild(rubbish);

    updateTotal();
  });
  var i = document.createElement("i");
  i.classList.add("fa", "fa-trash-o");
  delbut.appendChild(i);
  deltd.appendChild(delbut);

  row.appendChild(quantitytd);
  row.appendChild(nametd);
  row.appendChild(pricetd);
  row.appendChild(deltd);

  if (quantity) {
    cartable.prepend(row);
  } else {
    cartmeta.prepend(row);
  }
  updateTotal();
}

function updateTotal() {
  const cartrows = cartable.rows;
  var total = 0;
  var pax = 0;
  const cartickets = [];
  for (row of cartrows) {
    ticketinput = row.cells[0].getElementsByTagName("input")[0];
    cartickets.push(ticketinput.name);
    quantity = Number(ticketinput.value);
    pax += quantity;
    total += Number(row.cells[2].innerText) * quantity;
  }

  const metarows = cartmeta.rows;
  for (row of metarows) {
    let name = row.cells[1].innerText;
    // hardcode reward mechanisms here
    if (name === "15% off for guided tour") {
      price = -(total * 0.15);
      row.cells[2].innerText = price.toFixed(2);
      total += price;
    }
  }

  totaltd.innerText = total.toFixed(2);
  paxtd.innerText = pax;

  var tcount = ticketsleft - pax;
  ticketcount.innerText = tcount;
  if (tcount < 0 && notifyerror) {
    ticketcount.style.color = "red";
    soldoutmsg.style.display = "initial";
    soldoutmsg.scrollIntoView(false);
    notifyerror = false;
  } else if (tcount >= 0) {
    ticketcount.style.color = "";
    soldoutmsg.style.display = "";
    notifyerror = true;
  }

  const ofage =
    cartickets.includes("Adult") || cartickets.includes("Concession");
  if (ofage && tcount >= 0) {
    subuttenable(paybutton, whydisabled);
  } else {
    subuttdisable(paybutton, whydisabled);
  }

  if (ofage && carterror) {
    carterror.removeAttribute("style");
  }
}

function stepbutt(symbol, step, id) {
  const butt = document.createElement("button");
  butt.type = "button";
  butt.innerText = symbol;
  butt.classList.add("btn", "btn-secondary", "btn-sm");
  butt.id = id;
  butt.addEventListener("click", function () {
    const input = this.parentElement.querySelector("input[type='number']");
    input.value = Number(input.value) + step;
    input.dispatchEvent(new Event("change"));
  });
  return butt;
}

form.addEventListener("submit", () => buttonloading(paybutton));
