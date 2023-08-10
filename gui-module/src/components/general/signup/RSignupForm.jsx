/**
 * Form to handle restauraunt registration
 * Input: Function from restaurant register page to handle what happens once
 *        data is submitted
 */
import { React, useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import { Container, Row, Col, FloatingLabel } from "react-bootstrap";

const RSignupForm = ({ onSignup }) => {
  //inputs from form
  const [name, setName] = useState("");
  const [address, setAddress] = useState("");
  const [postal, setPostal] = useState("");
  const [telephone, setTelephone] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const onSubmit = (e) => {
    e.preventDefault();
    //If data field is missing the user will be alerted
    if (!name || !address || !postal || !telephone || !username || !password) {
      alert("Please fill out all info");
      return;
    }
    onSignup({ name, address, postal, telephone, username, password });
  };

  return (
    <Container className="register-restaurant-form">
      <h3 className="reg-text">
        <strong>REGISTER</strong>
      </h3>
      <Form onSubmit={onSubmit} className="register-restaurant-form">
        <Form.Group as={Col} controlId="form.Name" className="mb-3">
          <Col>
            <FloatingLabel controlId="floatingUName" label="Username">
              <Form.Control
                type="text"
                placeholder="Restaurant Name"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </FloatingLabel>
          </Col>
        </Form.Group>
        <Form.Group as={Col} controlId="form.Name" className="mb-3">
          <Col>
            <FloatingLabel controlId="floatingName" label="Restaurant Name">
              <Form.Control
                type="text"
                placeholder="Restaurant Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
            </FloatingLabel>
          </Col>
        </Form.Group>

        <Form.Group as={Col} controlId="form.Address" className="mb-3">
          <Col>
            <FloatingLabel controlId="floatingAddress" label="Address">
              <Form.Control
                type="text"
                placeholder="Address"
                value={address}
                onChange={(e) => setAddress(e.target.value)}
              />
            </FloatingLabel>
          </Col>
        </Form.Group>

        <Form.Group as={Col} className="mb-3" controlId="form.Postal">
          <Col>
            <FloatingLabel controlId="floatingPostal" label="Postal Code">
              <Form.Control
                type="text"
                placeholder="Postal Code"
                value={postal}
                onChange={(e) => setPostal(e.target.value)}
              />
            </FloatingLabel>
          </Col>
        </Form.Group>
        <Form.Group as={Col} className="mb-3" controlId="form.Telephone">
          {/* <Form.Label column sm={2}>
                Card Number
              </Form.Label> */}
          <Col>
            <FloatingLabel controlId="floatingPhone" label="Telephone">
              <Form.Control
                type="text"
                placeholder="Telephone"
                value={telephone}
                onChange={(e) => setTelephone(e.target.value)}
              />
            </FloatingLabel>
          </Col>
        </Form.Group>
        <Form.Group as={Col} controlId="form.Name" className="mb-3">
          <Col>
            <FloatingLabel controlId="floatingUName" label="Password">
              <Form.Control
                type="password"
                placeholder="Restaurant Name"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </FloatingLabel>
          </Col>
        </Form.Group>
        <Button type="submit" variant="primary">
          Submit Request
        </Button>
      </Form>
    </Container>
  );
};

export default RSignupForm;
