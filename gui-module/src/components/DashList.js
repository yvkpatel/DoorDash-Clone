/*  DashList.js
    Component that acts as a container for cards displayed in a veritcal list.

    === Props ===
    itemList = list of the items to be displayed in each of the cards.
        Example: const [listVar] = useState([{ id: 1, title: 'Card 1'}, { id: 2, title: 'Card 2'}]);

    component = the component that will be used for each of the cards.

    manager = class that will provide methods that may be called from the card.
*/

const List = ({ itemList, component, manager }) => {
  const Component = component;

  return (
    <div className="list" data-testid="dash-list">
      {itemList
        ? itemList.map((item) => (
            <Component key={item.id} item={item} manager={manager} />
          ))
        : "Loading:..."}
    </div>
  );
};

export default List;
