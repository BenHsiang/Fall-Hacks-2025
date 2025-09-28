//I do not know java but :)

const objectString = localStorage.getItem('order');
const list= JSON.parse(objectString);
const OrderContainer=document.getElementById('OrderContainer');
list.forEach(item => {
    const listItem = document.createElement("li");
    listItem.textContent = `${item.name} (${item.color})`;
    OrderContainer.appendChild(listItem);
});

