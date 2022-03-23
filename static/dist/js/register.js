const usernameField=document.querySelector("#usernameField");


usernameField.addEventListener("keyup", (e) => {
    console.log("777777", 777777);
    const usernameVal = e.target.value;

    if(usernameVal.lenght > 0){
        fetch("/authentication/register/validate-username", {
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        }).then(res => res.json()).then(data=>{
            console.log('data', data)
        });
    }

});
    
