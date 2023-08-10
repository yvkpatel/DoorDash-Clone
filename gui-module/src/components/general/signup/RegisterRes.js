/**
 * This is the page for Restaurant owners to signup to YUMI
 */
import { React, useState } from "react";
import "./RegisterRes.css";
import GenHeader from "../../GenHeader.js";
import RSignupForm from "./RSignupForm";
import { useHistory } from "react-router-dom";

const RegisterRes = () => {
  const history = useHistory();
  //temperary used for MVP since DB connection not working
  const [tempAdded, setTempAdded] = useState(false);
  const [addedRestaurant, setAddedRestaurant] = useState("");

  const submitRes = (userDetails) => {
    var obj = new Object();
    obj.username = userDetails.email;
    obj.passHash = userDetails.password;
    obj.name = userDetails.name;
    obj.category = "default";
    obj.openHour = "4:20";
    obj.closeHour = "1:23";
    obj.address = userDetails.address;
    obj.postal = userDetails.postal;

    fetchAddRestaurant(obj);
  };

  //Calls database to add the user
  //TODO: CURRENTLY NOT WORKING. ADDS USER BUT RETURNS REPLY FALSE ALWAYS - ASSUME TRUE FOR ALL CALLS FOR MVP
  const fetchAddRestaurant = (obj) => {
    const reqPar = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(obj),
    };
    fetch("/restaurant/add", reqPar)
      .then((res) => res.json())
      .then(
        (data) => setAddedRestaurant(data),
        alert("account created"),
        history.push("/")
      )
      .catch((err) => console.log(err));
  };
  return (
    <div className="App">
      <GenHeader></GenHeader>
      <RSignupForm onSignup={submitRes}></RSignupForm>
    </div>
  );
};

export default RegisterRes;
