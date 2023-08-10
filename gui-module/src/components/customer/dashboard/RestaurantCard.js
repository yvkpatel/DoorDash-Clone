/**Displays a restauarnt details on a card for the user */
import React from "react";
import { Row, Col, Card } from "react-bootstrap";
import { Link } from "react-router-dom";

const RestaurantCard = ({ item, onSelect }) => {
  return (
    <Link to={{ pathname: "../menu", state: { restaurantId: item.id } }}>
      <div onClick={() => onSelect(item.id)}>
        <Card>
          <Row>
            <Col sm={8}>
              <Card.Body>
                <Card.Title>{item.name}</Card.Title>
                <Card.Subtitle className="mb-2 text-muted">
                  {item.address}
                </Card.Subtitle>
              </Card.Body>
            </Col>
          </Row>
        </Card>
      </div>
    </Link>
  );
};

export default RestaurantCard;
