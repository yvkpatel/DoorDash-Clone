/**
 * Component to show items for the order summary
 */

import React from "react";
import Card from "react-bootstrap/Card";

const OrderCard = (props) => {
  return (
    <div className="orderCustomer">
      <Card>
        <Card.Body>
          <Card.Title>{props.title}</Card.Title>
          <Card.Text>${props.price}</Card.Text>
        </Card.Body>
      </Card>
    </div>
  );
};

export default OrderCard;
