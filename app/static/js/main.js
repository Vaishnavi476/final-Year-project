console.log('loaded main js')

fetch('/config/')
.then((result) =>{
    return result.json();
})
.then((data)=>{
    const stripe = Stripe(data.publicKey)
    
    document.querySelector('#purchasebtn').addEventListener('click',()=>{
        
        fetch('/create-checkout-session/')
        .then((result)=>{return result.json();})
        .then((data)=>{
            console.log(data);
            return stripe.redirectToCheckout({sessionId:data.sessionId})
        }).
        then((res)=>{
            console.log(res)
        })
    });
});