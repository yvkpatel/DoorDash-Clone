// Displays Menu items in a list
import "./menu.css";

const MenuList = ({ itemList, component, cart }) => {
  const Component = component;

  return (
    <div className="menulist">
      {itemList.map((item) => (
        <Component
          key={item.id}
          id={item.id}
          title={item.title}
          image={item.image}
          price={item.price}
          details={item.details}
          cart={cart}
        />
      ))}
    </div>
  );
};

export default MenuList;
