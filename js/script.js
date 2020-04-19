//alert("hey sup!")
//alert("how are you !!")


feelings = ['not good','depressed','want to kill myself','good','aweseome']

root = $("<div id='root'>");
root.appendTo($('body'))

feelings.forEach(feeling => {
    
    //make a checkbock 
    $(`<input type="radio" value ="">${feeling}</input><br>`).appendTo(root)
    //append the options to the page 
    //add a click listener to it
});


//depending on the option selected show next options



