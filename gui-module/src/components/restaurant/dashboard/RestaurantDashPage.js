/** This is the file for Restaurant doordash  */
import RestaurantManager from "./RestaurantManager";
import Header from "../../Header";
import DashList from "../../DashList";
import OrderInfo from "./OrderInfo";

const RestaurantDash = () => {
  let manager = new RestaurantManager(27, 9689.25, 212);

  return (
    <div className="App" datatest-id="register-res">
      <Header />
      <div className="driverDashMain">
        <div className="dashInfoBox">
          <h1>Account Summary</h1>
          <p>Income: {manager.getIncome()}</p>
          <p>Orders: {manager.orders}</p>
        </div>
        <DashList
          itemList={manager.getRestaurantOrders()}
          component={OrderInfo}
          manager={manager}
        />
      </div>
    </div>
  );
};

export default RestaurantDash;
