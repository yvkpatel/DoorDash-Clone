/*  Cart.js
    Author: Jesse
    Description: Locally stores all of the menu items the customer has put in the cart.
 */

class Cart {
  constructor() {
    this.itemList = [];
    this.price = 0;
  }

  /*  Pushes an item onto the itemList.
        Example Call: 
            cart.addToCart({id:500, title:"Pizza", price:5.95});  

        Note: Use JSON objects to avoid unintended behaviour. */
  addToCart(item) {
    this.itemList.push(item);
    this.price = this.calcTotalPrice();
    // Debug Log
    console.log(this);
  }

  // Loops through all items in itemList, totals their prices and returns the total.
  calcTotalPrice() {
    var total = 0;
    this.itemList.forEach((item) => {
      total += item.price;
    });
    console.log(total);
    return total.toFixed(2);
  }
}

export default Cart;
