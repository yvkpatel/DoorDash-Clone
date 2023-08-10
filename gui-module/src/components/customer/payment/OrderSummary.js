/**
 * Component to display order summary at checkout
 */
import React from "react";
import OrderList from "./OrderList";
import OrderCard from "./OrderCard";

const OrderSummary = (props) => {
  return (
    <div>
      <h1>Order Summary</h1>
      <OrderList itemList={props.itemList} component={OrderCard} />
      <h2>Total: ${props.cost}</h2>
    </div>
  );
};

export default OrderSummary;
