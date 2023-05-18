const addrewardbut = document.getElementById('addrewardbut')
const rewardselect = document.getElementById('rewardselect')
const claimed = document.getElementById('claimed')
const claims = [];

function validate_reward(func, args) {
	console.log(func);
	validate(rewardselect, availrewards.includes(rewardselect.value), func, args);
}

rewardselect.addEventListener("input", () => validate_reward() );

addrewardbut.addEventListener("click", () => validate_reward(addreward, [rewardselect.value]));

function addreward(name) {
	// add reward to cart
	addtocart(false, name, '')
	claims.push(name)
	claimed.value = JSON.stringify(claims)
	// remove reward from select
	rewardselect.removeChild(document.getElementById(name.replace(/\s/g,'')));
	rewardselect.classList.remove('is-valid');
	availrewards.remove(name);
}

function delreward(name) {
	// add reward back
    availrewards.push(name)
    rewardopt = document.createElement('option')
    rewardopt.innerText = name
    rewardopt.id = name.replace(/\s/g,'');
    rewardselect.appendChild(rewardopt)
    // remove from hidden field claimed
    claims.remove(name);
	claimed.value = JSON.stringify(claims);
}

function discount(subtotal, multiplier) {
	return subtotal * multiplier
}
