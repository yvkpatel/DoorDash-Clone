/**
 * This is the page for driver's to signup to YUMI
 *
 * For MVP the password confirm does not confirm if passwords are the same
 */
import Header from "../../GenHeader";
import { React, useState } from "react";
import "./signup.css";
import SignupForm from "./SignupForm";
import { useHistory } from "react-router-dom";
const DriverSignup = () => {
  //temperary used for MVP since DB connection not working
  const [tempAdded, setTempAdded] = useState(false);
  //return from DB to establish if user created. True = successful, false = user exists
  const [addedDriver, setAddedDriver] = useState("");
  const history = useHistory();

  //controls what happens when the user presses "Create Account"
  const submitDetails = (userDetails) => {
    var obj = new Object();
    obj.username = userDetails.email;
    obj.passHash = userDetails.password;
    obj.name = userDetails.firstName + " " + userDetails.lastName;
    console.log({ obj });
    fetchAddDriver(obj);
  };

  //Calls database to get add the user
  //TODO: CURRENTLY NOT WORKING. ADDS USER BUT RETURNS REPLY FALSE ALWAYS - ASSUME TRUE FOR ALL CALLS FOR MVP
  const fetchAddDriver = (obj) => {
    const reqPar = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(obj),
    };
    console.log(reqPar.body);
    fetch("/driver/add", reqPar)
      .then((res) => res.json())
      .then(
        (data) => setAddedDriver(data),
        alert("account created"),
        history.push("/")
      )
      .catch((err) => console.log(err));
  };

  return (
    <div className="main">
      <Header></Header>
      <h1>Driver Signup</h1>
      {/*  Component for Signup form*/}
      <SignupForm onSignUp={submitDetails} />
      {/* <ChangePage/> */}
    </div>
  );
};

export default DriverSignup;
