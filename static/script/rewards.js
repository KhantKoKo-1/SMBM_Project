document.getElementById('rewardSubmit').addEventListener('click', () => {
    if (document.getElementById('reward').value != '') alert(`Redeemed points for: ${document.getElementById("reward").value} voucher!`)
})

// Claim Reward Algorithm
var customerPoints = parseInt(document.getElementById('custPoints').textContent.replace('Current Points: ', ''))


for (i in pointsList) {
    if (customerPoints >= pointsList[i]) document.getElementById(`${pointsList[i]}points`).style.display = 'block'
}
if (customerPoints < pointsList[0]) document.getElementById('notEnoughPoints').style.display='block'
// End of file
console.log('aa')

document
    .getElementById("reward")
    .addEventListener("change", () =>{
    var value=document.getElementById("reward").value

    if(value=="10% off for guided tour"){
        document.getElementById("point").value=15
    }
    else if (value=="20% off for guided tour"){
        document.getElementById("point").value=25
    }
    else if (value=="$1 off any dish in café "){
        document.getElementById("point").value=5
    }
    else if (value=="2 off any dish in café"){
        document.getElementById("point").value=9
    }
    else if (value=="10% off for workshop"){
        document.getElementById("point").value=17
    }
    else if (value=="20% off for workshop"){
        document.getElementById("point").value=30
    }

}
    );
