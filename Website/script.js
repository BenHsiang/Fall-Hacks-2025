
document.addEventListener('DOMContentLoaded', () => {
  const selectedItems = [];

  // Fades out the logo screen at the start
  window.addEventListener('load', () => {
    const splash = document.getElementById('splash-screen');
    setTimeout(() => {
      splash.style.opacity = '0';
      splash.addEventListener('transitionend', () => {
        splash.style.display = 'none';
      });
    }, 1000);
  });

  const menuData = {
    "Restaurant Name 1": [
      {
        title: "Cheeseburger",
        description: "Beef patty, cheddar, pickles, ketchup, sesame bun.",
        price: "$5.99"
      },
      {
        title: "Double Bacon Burger",
        description: "Double patties, crispy bacon, BBQ sauce, cheddar.",
        price: "$7.99"
      },
      {
        title: "Fries (Large)",
        description: "Golden, crispy fries seasoned to perfection.",
        price: "$2.49"
      }
    ],
    "Restaurant Name 2": [
      {
        title: "Grilled Chicken Wrap",
        description: "Grilled chicken, lettuce, tomato, ranch in a wrap.",
        price: "$6.49"
      },
      {
        title: "Caesar Salad",
        description: "Romaine, Caesar dressing, parmesan, croutons.",
        price: "$4.99"
      }
    ],
    "Restaurant Name 3": [
      {
        title: "Pepperoni Pizza",
        description: "Mozzarella, pepperoni, tomato sauce, hand-tossed crust.",
        price: "$8.99"
      },
      {
        title: "Garlic Knots",
        description: "Baked dough knots, garlic butter, parmesan.",
        price: "$3.49"
      }
    ],
    "Restaurant Name 4": [
      {
        title: "Vegan Bowl",
        description: "Quinoa, black beans, avocado, tofu, tahini.",
        price: "$9.49"
      },
      {
        title: "Green Smoothie",
        description: "Spinach, banana, kiwi, almond milk.",
        price: "$4.29"
      }
    ]
  };

  function renderMenu(restaurantName) {
    const grid = document.querySelector('.menu-grid');
    const items = menuData[restaurantName];

    if (!items || !Array.isArray(items)) {
      grid.innerHTML = `<p style="color:#fff;">No menu available for "${restaurantName}"</p>`;
      return;
    }

    grid.style.opacity = '0';

    setTimeout(() => {
      grid.innerHTML = '';

      items.forEach(item => {
        const div = document.createElement('div');
        div.classList.add('button', 'menu-item');
        div.innerHTML = `
          <div class="menu-item-title">${item.title}</div>
          <div class="menu-item-description">${item.description}</div>
          <div class="menu-item-price">${item.price}</div>
        `;

        // Use a unique identifier (like title + restaurant name)
        const itemId = `${restaurantName}__${item.title}`;

        div.addEventListener('click', () => {
          div.classList.toggle('selected');

          const index = selectedItems.findIndex(i => i.id === itemId);
          if (index > -1) {
            // Deselect
            selectedItems.splice(index, 1);
          } else {
            // Select
            selectedItems.push({
              id: itemId,
              restaurant: restaurantName,
              title: item.title,
              description: item.description,
              price: item.price
            });
          }

          console.log('Current Selection:', selectedItems); // Optional live debug
        });

        grid.appendChild(div);
      });

      grid.style.opacity = '1';
    }, 300);
  }

  // Hook up sidebar buttons
  document.querySelectorAll('.button-sidebar').forEach(button => {
    button.addEventListener('click', () => {
      document.querySelectorAll('.button-sidebar').forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
      const name = button.getAttribute('data-restaurant');
      renderMenu(name);
    });
  });

  // Hook up Submit button
  document.querySelector('.submit-button').addEventListener('click', () => {
    if (selectedItems.length === 0) {
      alert("You haven't selected any items.");
      return;
    }

    console.log("Selected Items:");
    selectedItems.forEach(item => {
      console.log(`- ${item.restaurant}: ${item.title} (${item.price})`);
    });

    alert("Check console");
  });

  // Default first button active
  const firstButton = document.querySelectorAll('.button-sidebar')[0];
  if (firstButton) {
    firstButton.classList.add('active');
    renderMenu(firstButton.getAttribute('data-restaurant'));
  }
});
