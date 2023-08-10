/** Driver Dashboard */
import DriverManager from "./DriverManager";
import Header from "../../Header";
import DashList from "../../DashList";
import DriverOrder from "./DriverOrder";

const DriverDash = () => {
  // The constructor parameters should be supplied via the driver's account in databases.
  let manager = new DriverManager(4, 9.24, 2);

  return (
    <div className="App">
      <Header />
      <div className="driverDashMain">
        <div className="dashInfoBox" data-testid="driver-dash">
          <h1>Account Summary</h1>
          <p>Income: {manager.getIncome()}</p>
          <p>Orders: {manager.orders}</p>
        </div>
        <DashList
          itemList={manager.getDriverOrders()}
          component={DriverOrder}
          manager={manager}
        />
      </div>
    </div>
  );
};

export default DriverDash;
