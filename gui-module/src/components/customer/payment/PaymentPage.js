/**
 * This is the payment page where a customer can see the finished order and submit payment details
 */
import { React, useState, useEffect } from "react";
import Header from "../../Header";
import { Row, Col } from "react-bootstrap";
import Payment from "./Payment";
import OrderSummary from "./OrderSummary";
import Container from "react-bootstrap/Container";
// import PaymentForm from "../components/PaymentForm";
import { useHistory } from "react-router-dom";

const PaymentPage = (props) => {
  //Will pull Order Item List from Database
  const [paydetails, setPayDetails] = useState({});
  const [customerDetails, setCustomer] = useState({});
  const st = props.location.state;
  console.log(props);
  const history = useHistory();

  //Gets order items on page and gets customer details => FAKE SERVER FOR NOW :)
  useEffect(() => {
    // const getItems = async () => {
    //   const itemsFromServer = await fetchItems()
    //   setItems(itemsFromServer)
    // }
    const getCustomer = async () => {
      const custFromServer = await fetchCustomer("C235771756");
    };
    // getItems()
    getCustomer();
  }, []);

  //Deletes object from database after payment. Temporary to reduce frontend database
  // useEffect(()=>{
  //   deletePayment();
  // },[paydetails])

  //Fetch Order Items
  // const fetchItems = async () => {
  //   const res = await fetch('http://localhost:5000/items')
  //   const data = await res.json()

  //   return data
  // }

  //Fetch Customer Details
  const fetchCustomer = (id) => {
    const res = fetch("/customer/id/" + id)
      .then((resp) => resp.json())
      .then((data) => setCustomer(data))
      .catch((err) => console.log(err));
  };

  //This creates a JSON file as requested by the payment team
  const makePayJson = (props) => {
    var obj = new Object();
    //TODO change obj items to all required things
    obj.ccv = props.cardCVV;
    obj.card_number = props.cardNumber;
    obj.expiry = props.cardExpiry;

    obj.name = customerDetails.name;
    obj.postal_code = customerDetails.postal_code;
    //TODO: fill with real info from backend
    obj.total = "$420.69";
    var JSONstring = JSON.stringify(obj, null, 2);

    //print (just for testing) - REMOVE LATER
    alert(JSONstring);
    return JSONstring;
  };

  // const sendPayment = async (props) => {
  //   const payJson = makePayJson(props);
  //   // const res = await fetch('http://localhost:5000/payment', {
  //   //   method: 'POST',
  //   //   headers: {
  //   //     'Content-type': 'application/json'
  //   //   },
  //   //   body: payJson,
  //   // })
  //   // const data = await res.json();
  //   //setPayDetails(data);
  //   console.log(paydetails);
  //   return data;
  // }

  // const deletePayment = async () => {
  //   await fetch('http://localhost:5000/payment/1', {
  //     method: 'DELETE',
  //   })
  // }

  //TODO: pull from the backend
  var cost = 0;
  var items = [];
  if (st != null) {
    cost = st.cart.price;
    items = st.cart.itemList;
  }

  //This function will handle how payment of the order is handled
  const submitPayment = (cardDetails) => {
    console.log(customerDetails._Customer__name);
    history.push("../customermap");
    // const data = sendPayment(cardDetails);
  };

  return (
    <div className="App" data-testid="payment-page">
      <Header />
      <Container>
        <Row>
          <Col xs={12} md={8}>
            {" "}
            {/*  Component to display order summary */}
            <OrderSummary itemList={items} cost={cost} />
          </Col>
          <Col xs={6} md={4}>
            {" "}
            {/*  Component to display payment form */}
            {/* <PaymentForm/> */}
            <Payment onPay={submitPayment} />
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default PaymentPage;
