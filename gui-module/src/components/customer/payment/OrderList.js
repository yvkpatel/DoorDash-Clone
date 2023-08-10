/** This component displays the order to the payment screen  */

import React from "react";

const OrderList = ({ itemList, component }) => {
  const Component = component;
  return (
    <div className="list">
      {itemList.map((item) => (
        <Component key={item.id} title={item.title} price={item.price} />
      ))}
    </div>
  );
};

export default OrderList;
