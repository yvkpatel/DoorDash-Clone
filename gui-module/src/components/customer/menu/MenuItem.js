import Button from "../../Button";
import "./menu.css";
const MenuItem = (props) => {
  return (
    <div className="testCard" style={{ width: "100%", display: "flex" }}>
      <img src={props.image} alt="foodItem" className="thumbnail" />
      <div className="details">
        <h1 className="md-1">{props.title}</h1>
        <hr style={{ width: "100%", marginTop: "2px", marginBottom: "2px" }} />
        <p style={{ verticalAlign: "top", margin: "0px" }}>{props.details}</p>
        <p
          style={{
            float: "right",
            verticalAlign: "top",
            marginBottom: "0px",
            marginTop: "16px",
          }}
        >
          ${props.price} CAD
        </p>
      </div>
      <div className="add-to-cart">
        <Button
          text="Add to Cart"
          color="#2DB6F0"
          label={props.title}
          style={{ float: "right", verticalAlign: "top", margin: "0px" }}
          onClick={() =>
            props.cart.addToCart({
              id: props.id,
              title: props.title,
              price: props.price,
            })
          }
        />
        <p>Quantity:</p>
        <p>1</p>
      </div>
    </div>
  );
};

export default MenuItem;
