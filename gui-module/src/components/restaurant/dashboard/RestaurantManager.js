/*  RestaurantManager.js
    Provides methods for the restaurant dashboard to interact with databases and manage the restaurant's local information.
*/
class RestaurantManager {
  constructor(id, income, orders) {
    this.id = id;
    this.income = income;
    this.orders = orders;
  }

  // =============== LOCAL MANAGEMENT METHODS ===============

  // Converts the restaurant's income from a float to a currency formatted string.
  getIncome() {
    return "$" + this.income;
  }

  updateIncome(x) {
    this.income += x;
  }

  // =============== METHODS THAT INTERACT WITH DATABASES ===============

  // PLACEHOLDER: will fetch restaurant's orders from database.
  // Current implementation simply returns a hardcoded list of imaginary orders.
  getRestaurantOrders() {
    return [
      {
        id: 1,
        title: "Presidential Pizza",
        restaurant: "Boston Pizza",
        destination: "1600 Pennsylvania Avenue",
      },
      {
        id: 2,
        title: "Famous Pizza, I guess.",
        restaurant: "Dominos",
        destination: "4059 Mt Lee Dr. Hollywood",
      },
      {
        id: 3,
        title: "Pentagram Pizza",
        restaurant: "Pizza Hut",
        destination: "6114 California Street",
      },
      {
        id: 4,
        title: "Curious Pizza",
        restaurant: "???",
        destination: "221B Baker Street",
      },
      {
        id: 5,
        title: "Pizza, dude.",
        restaurant: "Literally Anywhere",
        destination: "122 + 1/8th Bleaker Street",
      },
    ];
  }

  // PLACEHOLDER: When called it should inform database that the order status has changed.
  updateOrder(orderID) {
    console.log("Order ID: " + orderID);
  }
}

export default RestaurantManager;
