/* This component controls the payment information form
 *  Input: function from payment page to handle the submission of payment data
 */

import React from "react";
import { useState } from "react";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import { Grid, Row, Col } from "react-bootstrap";
import Button from "react-bootstrap/Button";
import { FloatingLabel } from "react-bootstrap";

const Payment = ({ onPay }) => {
  // var visaRegEx = /^(?:4[0-9]{12}(?:[0-9]{3})?)$/;
  // var expiryRegEx = /^(0[1-9]|1[0-2])\/?([0-9]{4}|[0-9]{2})$/;
  // var cVVRegEx = /^[0-9]{3,4}$/;
  //Input fields for payment form
  const [cardNumber, setCardNumber] = useState("");
  const [cardExpiry, setExpiry] = useState("");
  const [cardCVV, setCVV] = useState("");

  //handles the submission of data
  const onSubmit = (e) => {
    e.preventDefault();
    //If details are missing the user is alerted
    if (!cardNumber || !cardExpiry || !cardCVV) {
      alert(
        "Yeah probably best not to put your credit card details into this app..."
      );
      return;
    }

    /*
         if (!visaRegEx.test(cardNumber)) {
             alert('Credit Card number not valid.');
            return;
         }
         if(!expiryRegEx.test(cardExpiry)){
             alert('Credit Card expiry not valid.');
             return;
         }
         if(!cVVRegEx.test(cardCVV)){
             alert('Credit Card CVV not valid.');
             return;
        */
    onPay({ cardNumber, cardExpiry, cardCVV });
    //alert('Lolz we got ur details')
  };
  return (
    <Container className="container2">
      <h1> Payment Information </h1>
      <Form onSubmit={onSubmit}>
        <Row className="mb-3">
          <Form.Group as={Col} controlId="form.Number">
            <Col>
              <FloatingLabel controlId="floatingNum" label="Card Number">
                <Form.Control
                  type="text"
                  value={cardNumber}
                  onChange={(e) => setCardNumber(e.target.value)}
                />
              </FloatingLabel>
            </Col>
          </Form.Group>
        </Row>

        <Row>
          <Form.Group as={Col} className="mb-3" controlId="form.Expiry">
            <FloatingLabel controlId="floatingExpiry" label="Expiry (MM/YY)">
              <Form.Control
                type="text"
                value={cardExpiry}
                onChange={(e) => setExpiry(e.target.value)}
              />
            </FloatingLabel>
          </Form.Group>
          <Form.Group className="mb-3" as={Col} controlId="form.CVV">
            <FloatingLabel controlId="floatingCVV" label="CVV">
              <Form.Control
                type="text"
                value={cardCVV}
                onChange={(e) => setCVV(e.target.value)}
              />
            </FloatingLabel>
          </Form.Group>
        </Row>
        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </Container>
  );
};
export default Payment;
