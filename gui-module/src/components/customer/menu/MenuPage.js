/* Displays menu items available at the selected restaurant*/

import { useState } from "react";
import MenuItem from "./MenuItem";
import Header from "../../Header";
import MenuList from "./MenuList";
import Cart from "./Cart";
import Button from "../../Button";
import { Link } from "react-router-dom";

const MenuPage = (props) => {
  const cart = new Cart();

  // Retrieving data from previous page (Customer's Restaurant List)
  var restaurantId; // @JR use this id for fetching the list below.

  const st = props.location.state;
  if (st != null) {
    restaurantId = st.restaurantId;
  }

  // This list would be pulled from databases.
  const [items /*, setTasks*/] = useState([
    {
      id: 1,
      title: "Pizza",
      price: 3.55,
      image:
        "https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=300,height=300,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/f71cc006-15c5-40be-bfac-91cdfdb0adb8-retina-large-jpeg",
      details:
        "This pizza has been finely topped with chedder cheese over a 100% pulverized tomato base on our signature creamy pizza dough.",
    },
    {
      id: 2,
      title: "Pizza 2",
      price: 6.55,
      image:
        "https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=300,height=300,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/f71cc006-15c5-40be-bfac-91cdfdb0adb8-retina-large-jpeg",
      details:
        "This pizza has been finely topped with chedder cheese over a 100% pulverized tomato base on our signature creamy pizza dough.",
    },
    {
      id: 3,
      title: "Pizza 3",
      price: 5.55,
      image:
        "https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=300,height=300,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/f71cc006-15c5-40be-bfac-91cdfdb0adb8-retina-large-jpeg",
      details:
        "This pizza has been finely topped with chedder cheese over a 100% pulverized tomato base on our signature creamy pizza dough.",
    },
  ]);

  return (
    <div className="App" data-testid="menu-page">
      <Header />
      <div /*style={{ width: "75%" }}*/>
        <MenuList itemList={items} component={MenuItem} cart={cart} />
      </div>
      <Link to={{ pathname: "../payment", state: { cart: cart } }}>
        <Button text={"Checkout"} color={"#2DB6F0"} />
      </Link>
    </div>
  ); // @JR Link here, sends to payment page. Note: Currently the link doesn't care is cart is empty.
};

export default MenuPage;
