function add_cart(id, quantity){
	//$.get("/add_to_cart/1/2")
	//$.get("/add_to_cart/{1}/{2}" , id, quantity)
	var add_string = "/add_to_cart/" + id + "/"  + quantity;

	$.get(add_string)
	alert("Debug text")
}


function remove_cart(id){
	//$.get("/remove_from_cart/1")
	var del_string = "/remove_from_cart/" + id;
	$.get(del_string)
	alert('Товар успешно удален')
	location.reload()
}
