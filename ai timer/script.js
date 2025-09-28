//I do not know java but :)
//this doesnt work atm

const objectString = localStorage.getItem('order');
print(objectString);
const list= JSON.parse(objectString);
print(list);
const OrderContainer=document.getElementById('OrderContainer');
list.forEach(item => {
    const listItem = document.createElement("li");
    listItem.textContent = `${item.name} (${item.color})`;
    OrderContainer.appendChild(listItem);
});

