import React from "react";
import Header from "../../Header";
import Alert from "react-bootstrap/Alert";
import CustomerMap from "./CustomerMap";
import "bootstrap/dist/css/bootstrap.min.css";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Ratio from "react-bootstrap/Ratio";

function CustomerMapsPage() {
  return (
    <div>
      <Header />

      <Container>
        <Row>
          <Col md={{ span: 4, offset: 4 }}>
            <br></br>
            <Alert
              variant="custom"
              style={{
                textAlign: "center",
                backgroundcolor: "#FE5757",
                color: "#fff",
                fontSize: "20px",
                fontFamily: "inherit",
                borderRadius: "5px",
              }}
            >
              Your order is on its way!
            </Alert>
          </Col>
        </Row>
        <Col md={{ span: 1, offset: 0 }}>
          <Ratio aspectRatio={100}>
            <div>
              <CustomerMap />
            </div>
          </Ratio>
        </Col>
      </Container>
    </div>
  );
}

export default CustomerMapsPage;
