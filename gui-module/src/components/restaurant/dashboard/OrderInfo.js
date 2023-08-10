// Displays customer's order info to restauraants
import React from "react";
import Button from "../../Button";

// TEMPORARILY USES THE SAME STYLING AS DriverOrder.js
// TODO: Renaming CSS classes to be more generic.

const OrderInfo = (props) => {
  return (
    <div className="driverTask">
      <div className="driverTaskHeader">
        <h2>{props.item.title}</h2>
        <Button
          text="Complete"
          color="#2DB6F0"
          onClick={() => props.manager.updateOrder(props.item.id)}
        />
      </div>
      <div className="driverTaskDetails">
        <p>Order Comments: {props.item.comments}</p>
      </div>
    </div>
  );
};

export default OrderInfo;
