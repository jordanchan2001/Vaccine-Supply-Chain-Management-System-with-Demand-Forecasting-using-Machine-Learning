var additemid=0;
function addtocart() {

    additemid += 1;
    var selectedVaccine = document.querySelector(".dropdown_vaccine").value;
    var selectedQuantity = document.querySelector(".input-container>input[name='quantity']").value;
    // whole container
    var selecteditem = document.createElement('div');
    selecteditem.classList.add('vaccine_content');
    
    //close btn
    var close_btn = document.createElement('button');
    close_btn.classList.add("close_btn");
    close_btn.setAttribute('type','button')
    // close_btn.setAttribute('onclick','deletefromcart()')
    var icon = document.createElement('i');
    icon.classList.add("fa-solid" ,"fa-x");
    close_btn.append(icon);

    //text
    var text_container = document.createElement('div');
    text_container.classList.add('vaccine_text');
    var p_vac_name = document.createElement('p');
    var vac_name_node = document.createTextNode("Vaccine Name: ");
    var p_quantity = document.createElement('p');
    var quantity_node = document.createTextNode("Quantity: ");

    var vac_name = document.createElement('input');
    vac_name.setAttribute('type','text');
    vac_name.setAttribute('disabled','');
    vac_name.setAttribute('name','vaccine_name');
    vac_name.setAttribute('value',selectedVaccine);
    var quantity = document.createElement('input')
    quantity.setAttribute('type','text');
    quantity.setAttribute('disabled','');
    quantity.setAttribute('name','vaccine_quantity');
    quantity.setAttribute('value',selectedQuantity);
    p_vac_name.append(vac_name_node)
    p_vac_name.append(vac_name);
    p_quantity.append(quantity_node);
    p_quantity.append(quantity);
    text_container.append(p_vac_name);
    text_container.append(p_quantity);

    var cartitems = document.querySelector('.show_vaccine_list');
    selecteditem.append(close_btn);
    selecteditem.append(text_container);
    cartitems.append(selecteditem);

    const close_btns = document.querySelectorAll(".close_btn");
    for (let i = 0; i < close_btns.length; i++) {
        close_btns[i].addEventListener("click", function() {
          close_btns[i].parentElement.remove();
        });
    }
}

