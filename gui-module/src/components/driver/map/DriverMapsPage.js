import React from "react";
import Header from "../../Header";
import Map from "./DriverMap";
import { propTypes } from "react-bootstrap/Image";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Ratio from "react-bootstrap/Ratio";
import Button from "react-bootstrap/Button";
import Stack from "react-bootstrap/Stack";
import { Link } from "react-router-dom";

const onPick = () => {
  // setPicked(true);
  //fetch("/order/status/set/001/1");
};

const onDeliver = () => {
  // setDelivered(true);
  // fetch("/order/status/set/001/2");
};

const DriverMapsPage = (props) => {
  const [disable, setDisable] = React.useState(false);
  return (
    <div data-testid="driver-map">
      <Header />

      <Container className="driverButtons" style={{ padding: "4vh" }}>
        <Row className="pickButton">
          <Col>
            <Stack gap={5}>
              <Button
                variant="custom"
                size="lg"
                style={{ backgroundColor: "#2DB6F0", color: "#FFFFFF" }}
                onClick={() => setDisable(true)}
                disabled={disable}
              >
                Pick Order
              </Button>
              <Link
                to={
                  disable
                    ? { pathname: "../driver-dash", state: {} }
                    : { pathname: propTypes.route }
                }
              >
                <Button
                  variant="custom"
                  size="lg"
                  style={{ backgroundColor: "#2DB6F0", color: "#FFFFFF" }}
                  disabled={!disable}
                >
                  Deliver Order
                </Button>
              </Link>
            </Stack>
          </Col>
          <Col>
            <Map />
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default DriverMapsPage;
