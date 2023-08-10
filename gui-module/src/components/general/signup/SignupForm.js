/**
 * This form is used by both the Driver and Customer Signup pages
 * to collect user details upon signing up
 *
 * Input: Function from page to handle submission of data
 */

import { React, useState } from "react";
import Form from "react-bootstrap/form";
import Button from "react-bootstrap/button";
import { Container, Row, Col, Alert } from "react-bootstrap";
import "./signup.css";

const SignupForm = ({ onSignUp }) => {
  //Fields that the are inputed.
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [address, setAddress] = useState("");
  const [postalCode, setPostalCode] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPass, setConfirmPass] = useState("");

  //Determines what happens when submit button is pressed
  const onSubmit = (e) => {
    if (
      !firstName ||
      !lastName ||
      !phoneNumber ||
      !address ||
      !postalCode ||
      !password
    ) {
      alert("Please fill out all form boxes");
      return;
    }
    e.preventDefault();
    onSignUp({
      firstName,
      lastName,
      email,
      phoneNumber,
      address,
      postalCode,
      password,
    });
  };
  return (
    <div>
      <div className="form">
        <Container>
          <Form onSubmit={onSubmit}>
            <Row>
              <Col>
                <Form.Group className="details">
                  <Form.Label>First Name</Form.Label>
                  <Form.Control
                    type="firstName"
                    placeholder="John"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                  />
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="details">
                  <Form.Label>Last Name</Form.Label>
                  <Form.Control
                    type="lastName"
                    placeholder="Doe"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                  />
                </Form.Group>
              </Col>
            </Row>
            <Form.Group className="details">
              <Form.Label>Email Address</Form.Label>
              <Form.Control
                type="email"
                placeholder="JohnDoe@gmail.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
            </Form.Group>

            <Row>
              {/* //commenting out for now. Just assuming local person for MVP and both options are the same anyway. */}
              {/* <Col xs={4}>
                                <Form.Group className="details">
                                <Form.Label>Country</Form.Label>
                                <Form.Select type="country">
                                    <option value="+1">+1 (CA)</option>
                                    <option value="+1">+1 (US)</option>
                                </Form.Select>
                                </Form.Group>
                            </Col> */}
              <Col>
                <Form.Group className="details">
                  <Form.Label>Phone Number</Form.Label>
                  <Form.Control
                    type="phone"
                    placeholder="709-111-1111"
                    value={phoneNumber}
                    onChange={(e) => setPhoneNumber(e.target.value)}
                  />
                </Form.Group>
              </Col>
            </Row>
            <Row>
              <Col>
                <Form.Group className="details">
                  <Form.Label>Address</Form.Label>
                  <Form.Control
                    type="address"
                    placeholder="42 Pizza St., Flavour Town"
                    value={address}
                    onChange={(e) => setAddress(e.target.value)}
                  />
                </Form.Group>
              </Col>
              <Col>
                <Form.Group className="details">
                  <Form.Label>Postal Code</Form.Label>
                  <Form.Control
                    type="postal"
                    placeholder="A1K 3E9"
                    value={postalCode}
                    onChange={(e) => setPostalCode(e.target.value)}
                  />
                </Form.Group>
              </Col>
            </Row>
            <Form.Group className="details">
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </Form.Group>

            <Form.Group className="details">
              <Form.Label>Confirm Password</Form.Label>
              <Form.Control type="password" placeholder="Password" />
            </Form.Group>

            <div className="sub">
              <Button variant="primary" type="submit">
                Create Account
              </Button>
              <a href="/login">Click here if you already have an account.</a>
            </div>
          </Form>
        </Container>
      </div>
    </div>
  );
};

export default SignupForm;
