/**
 * This is the form on the login page that users can submit their login detial
 *
 * @param: onLogin -> function that handles the submission of form data
 */
import { React, useState } from "react";
import Button from "react-bootstrap/Button";
import { Form } from "react-bootstrap";
import "./Login.css";

const LoginForm = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [userType, setUserType] = useState("");

  const onSubmit = (e) => {
    e.preventDefault();
    if (!email || !password || !userType) {
      alert("Please input all details");
      return;
    }
    //console.log({ email });
    onLogin({ email, password, userType });
  };

  return (
    <div data-testid="loginForm">
      <h3 className="login-text">
        <strong>SIGN IN</strong>
      </h3>
      <Form onSubmit={onSubmit}>
        <Form.Group className="details" data-testid="textfields">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="text"
            placeholder="pizza@gmail.com"
            value={email}
            data-testid="emailfield"
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>

        <Form.Group className="details">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Password"
            value={password}
            data-testid="passwordfield"
            onChange={(e) => setPassword(e.target.value)}
          />
        </Form.Group>

        <Form.Group className="details" data-testid="signinfield">
          <Form.Label>Sign in as:</Form.Label>
          {/* <Form.Control type="user type" placeholder="User Type" value={userType} onChange={(e) => setUserType(e.target.value)} /> */}
          <Form.Select
            aria-label="Default select example"
            data-testid="select"
            type="user type"
            placeholder="User Type"
            value={userType}
            onChange={(e) => setUserType(e.target.value)}
          >
            <option>Choose User Type</option>
            <option value="Customer">Customer</option>
            <option value="Driver">Driver</option>
            <option value="Restaurant">Restaurant</option>
          </Form.Select>
        </Form.Group>
        <Button
          variant="primary"
          type="submit"
          className="btn-primary"
          data-testid="goButton"
        >
          {" "}
          Go{" "}
        </Button>
      </Form>
    </div>
  );
};

export default LoginForm;

//test selection of drop down
