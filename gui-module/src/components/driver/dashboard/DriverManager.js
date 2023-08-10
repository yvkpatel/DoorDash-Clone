/*  DriverManager.js
    Provides methods for the driver dashboard to interact with databases and manage the driver's local information.
*/
class DriverManager {
  constructor(id, income, orders) {
    this.id = id;
    this.income = income;
    this.orders = orders;
  }

  // =============== LOCAL MANAGEMENT METHODS ===============

  // Converts the driver's income from a float to a currency formatted string.
  getIncome() {
    return this.income + "$";
  }

  updateIncome(x) {
    this.income += x;
  }

  // =============== METHODS THAT INTERACT WITH DATABASES ===============

  // PLACEHOLDER: will fetch driver tasks from database.
  // Current implementation simply returns a hardcoded list of imaginary tasks.
  getDriverOrders() {
    // @JR Note: some hefty refactoring might have to take place on DriverDash.js
    // depends on how the database fetches.
    return [
      {
        id: 1,
        title: "John Doe",
        restaurant: "Boston Pizza",
        destination: "1600 Pennsylvania Avenue",
      },
      // {
      //     id: 2,
      //     title: "Famous Pizza, I guess.",
      //     restaurant: "Dominos",
      //     destination: "4059 Mt Lee Dr. Hollywood"
      // },
      // {
      //     id: 3,
      //     title: "Pentagram Pizza",
      //     restaurant: "Pizza Hut",
      //     destination: "6114 California Street"
      // },
      // {
      //     id: 4,
      //     title: "Curious Pizza",
      //     restaurant: "???",
      //     destination: "221B Baker Street"
      // },
      // {
      //     id: 5,
      //     title: "Pizza, dude.",
      //     restaurant: "Literally Anywhere",
      //     destination: "122 + 1/8th Bleaker Street"
      // },
    ];
  }

  // PLACEHOLDER: When called it should inform database that the order is now taken.
  driverAcceptOrder(orderID) {
    console.log("Order ID: " + orderID);
  }
}

export default DriverManager;
