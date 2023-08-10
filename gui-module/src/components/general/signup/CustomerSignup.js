/* Sign up page for a customer */
import Header from "../../GenHeader";
import { React } from "react";
import "./signup.css";
import { Container } from "react-bootstrap";
import SignupForm from "./SignupForm";
import { useHistory } from "react-router-dom";
const CustomerSignup = () => {
  const history = useHistory();

  const submitDetails = (userDetails) => {
    console.log({ userDetails });
    history.push("/");
  };

  return (
    <div className="main">
      <Header></Header>
      <div className="form">
        <Container>
          <h1> Customer Signup </h1>
          {/*  Component for Signup form*/}
          <SignupForm onSignUp={submitDetails} />
        </Container>
      </div>
    </div>
  );
};

export default CustomerSignup;
