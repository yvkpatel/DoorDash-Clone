import CustomerMapsPage from "./components/customer/map/CustomerMapsPage";
import DriverMapsPage from "./components/driver/map/DriverMapsPage";
import MenuPage from "./components/customer/menu/MenuPage";
import PaymentPage from "./components/customer/payment/PaymentPage";
import CustomerDash from "./components/customer/dashboard/CustomerDashPage";
import DriverDash from "./components/driver/dashboard/DriverDashPage";
import RestaurantDash from "./components/restaurant/dashboard/RestaurantDashPage";
import Login from "./components/general/login/Login";
import RegisterRes from "./components/general/signup/RegisterRes";
import CustomerSignup from "./components/general/signup/CustomerSignup";
import DriverSignup from "./components/general/signup/DriverSignup";
import { Route, Router, BrowserRouter } from "react-router-dom";

const App = () => {
  return (
    <div className="App">
      {/* <NavigationBar/> */}
      <Route exact path="/" component={Login} />
      <Route exact path="/restaurant-regis" component={RegisterRes} />
      <Route exact path="/customermap" component={CustomerMapsPage} />
      <Route exact path="/drivermap" component={DriverMapsPage} />
      <Route exact path="/menu" component={MenuPage} />
      <Route exact path="/payment" component={PaymentPage} />
      <Route exact path="/customer-dashboard" component={CustomerDash} />
      {/* should route based on restaurant selected */}

      <Route exact path="/driver-dash" component={DriverDash} />

      <Route exact path="/restaurant-dash" component={RestaurantDash} />
      <Route exact path="/customer-signup" component={CustomerSignup} />
      <Route exact path="/driver-signup" component={DriverSignup} />
    </div>

    // <div className="App">
    //   <Header />
    //   <List itemList={items} component={TestItem} />
    // </div>
  );
};

export default App;
