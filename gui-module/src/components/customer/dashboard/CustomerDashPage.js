/* This is Customer Dashboard. Displays list of available restaurants
 */

import { React, useState, useEffect } from "react";
import Header from "../../Header";
import RestaurantCard from "./RestaurantCard";
import RestaurantList from "./RestaurantList";

const CustomerDash = () => {
  const [items /*, setItems*/] = useState([
    {
      id: 1,
      name: "Boston Pizza",
      address: "271 Blackmarsh Rd",
    },
  ]);

  // useEffect(() => {
  //     const getList = async () => {
  //         const listFromServer = await fetchList('R763567026')
  //         //setItems(listFromServer)
  //     }
  //     getList()
  // }, [])

  // const fetchList = async (id) => {
  //     try {
  //         const resp = await fetch("/restaurant/id/" + id)

  //         // setItems giving errors
  //         // .then((resp) => resp.json())
  //         // .then(data => this.setItems(data)).catch(err => console.log(err));

  //        const data = await resp.json()
  //         console.log(data)
  //     }
  //     catch (err) {
  //         throw err;
  //         console.log(err);
  //     }
  //     //return data;
  // }
  //Controls what happens when a restaurant is selected.
  const selectRestaurant = async (id) => {
    console.log(id);
  };

  return (
    <div>
      <Header />
      <RestaurantList
        itemList={items}
        component={RestaurantCard}
        onSelect={selectRestaurant}
      >
        {" "}
      </RestaurantList>
    </div>
  );
};

export default CustomerDash;
