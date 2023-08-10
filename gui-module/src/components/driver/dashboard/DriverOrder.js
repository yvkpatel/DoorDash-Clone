// Displays orders to driver to accept
import React from "react";
import Button from "../../Button";
import { Link } from "react-router-dom";

// TODO: Renaming CSS classes to be more generic.

const DriverOrder = (props) => {
  return (
    <div className="driverTask">
      <div className="driverTaskHeader">
        <h2>{props.item.title}</h2>
        <Link
          to={{ pathname: "../drivermap", state: { orderId: props.item.id } }}
        >
          <Button
            text="Accept"
            color="#2DB6F0"
            onClick={() => props.manager.driverAcceptOrder(props.item.id)}
          />
        </Link>
      </div>
      <div className="driverTaskDetails">
        <p>Pick up: {props.item.restaurant}</p>
        <p>Deliver: {props.item.destination}</p>
      </div>
    </div>
  );
};

export default DriverOrder;
