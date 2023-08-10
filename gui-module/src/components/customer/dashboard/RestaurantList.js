/**Displays a list of restaurants on the screen */

import React from "react";
const RestaurantList = ({ itemList, component, onSelect }) => {
  const Component = component;

  return (
    <div className="list2">
      <h1>Restaurants</h1>
      {itemList.map((item) => (
        <Component key={item.id} item={item} onSelect={onSelect} />
      ))}
    </div>
  );
};

export default RestaurantList;
