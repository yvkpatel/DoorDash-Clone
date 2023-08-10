/**
 * No longer used
 */

/** MVP you are not allowed to remove items from cart */
const OrderItem = (props) => {
  return (
    <div className="testCard" style={{ width: "100%" }}>
      <tr style={{ width: "100%" }}>
        <td
          style={{
            float: "left",
            paddingLeft: "10px",
            verticalAlign: "top",
            width: "100%",
          }}
        >
          <h1 style={{ margin: "2px", verticalAlign: "text-top" }}>
            {props.title}
          </h1>
          <hr style={{ width: "100%" }} />

          <td>${props.price}</td>

          {/* <td>
              <Button text="REMOVE" color="#2DB6F0" style={{ float: "Left" }} />
            </td> */}
        </td>
      </tr>
    </div>
  );
};

export default OrderItem;
