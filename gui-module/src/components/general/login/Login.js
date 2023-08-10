/**
 * This is the login screen
 *
 * Users of all types can login here. They will be redirected based on their user details
 */
import { React, useState } from "react";
import "./Login.css";
import Button from "react-bootstrap/Button";
import GenHeader from "../../GenHeader.js";
import LoginForm from "./LoginForm";
import { useHistory } from "react-router-dom";

const Login = () => {
  const [authenticate, setAuthenticate] = useState("false"); //true when user exists in database
  const [userType, setUserType] = useState(""); //customer, driver, restuarant
  const [userID, setUserID] = useState("");
  const history = useHistory();

  //Handles the submission of login details
  const submitLogin = (details) => {
    var obj = new Object();
    obj.username = details.email;
    obj.passHash = details.password;
    //testing purposes
    console.log(details);

    fetchAuthentication(obj);
    setUserType(details.userType);

    //Determine what to do based on the user type
    if (userType == "Customer") {
      fetchCustomer(details.email);
      history.push("/customer-dashboard");
      return;
    } else if (userType == "Restaurant") {
      fetchRestauant(details.email);
      history.push("/restaurant-dash");
      return;
    } else if (userType == "Driver") {
      fetchDriver(details.email);
      history.push("/driver-dash");
      return;
    }
  };

  //Calls database to get the authenticate the user
  //TODO: CURRENTLY NOT WORKING TO AUTHENTICATE USER - ASSUME TRUE FOR ALL CALLS FOR MVP
  const fetchAuthentication = (obj) => {
    setAuthenticate("true");
    // const reqPar = {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(obj)
    // }
    // console.log(reqPar.body);
    // fetch("/", reqPar).then(res => res.json())
    //   .then(data => setAuthenticate(data.reply))
    //   .catch(err => console.log(err));
  };

  //Gets Customer Details
  const fetchCustomer = (username) => {
    const res = fetch("/customer/user/" + username)
      .then((resp) => resp.json())
      .then((data) => setUserID(data._Customer__id))
      .catch((err) => console.log(err));
  };
  //Gets Restaurant Details
  const fetchRestauant = (username) => {
    const res = fetch("/restaurant/user/" + username)
      .then((resp) => resp.json())
      .then((data) => setUserID(data._Restaurant__id))
      .catch((err) => console.log(err));
  };
  //Gets Driver Details
  const fetchDriver = (username) => {
    const res = fetch("/driver/user/" + username)
      .then((resp) => resp.json())
      .then((data) => setUserID(data._Driver__id))
      .then(history.push("/customer-dashboard", { state: userID }))

      .catch((err) => console.log(err));
  };
  return (
    <div className="app" data-testid="login-1">
      <GenHeader></GenHeader>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <LoginForm onLogin={submitLogin} />
      </div>

      <div className="or">
        <p>
          <strong>OR</strong>
        </p>
        <p className="signupText">Sign up as</p>
      </div>
      <div className="register-buttons">
        <Button
          href="/customer-signup"
          variant="primary"
          data-testid="customer-signup"
        >
          Customer
        </Button>
        &nbsp;
        <Button
          href="/driver-signup"
          variant="primary"
          data-testid="driver-signup"
        >
          Driver
        </Button>
        &nbsp;
        <Button
          href="/restaurant-regis"
          variant="primary"
          data-testid="restaurant-signup"
        >
          Restaurant
        </Button>
      </div>
    </div>
  );
};

export default Login;
