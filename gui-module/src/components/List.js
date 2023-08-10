/*  List.js
    Component that acts as a container for cards displayed in a veritcal list.

    === Props ===
    itemList = list of the items to be displayed in each of the cards.
        Example: const [listVar] = useState([{ id: 1, title: 'Card 1'}, { id: 2, title: 'Card 2'}]);

    component = the component that will be used for each of the cards.
        NOTE: the component is recomended to accomodate the following props.
            * String title
            * 
            * ALAN PLEASE ADD DETAILS
*/
const List = ({ itemList, component }) => {
  const Component = component;

  return (
    <div className="list">
      {itemList.map((item) => (
        <Component key={item.id} title={item.title} />
      ))}
    </div>
  );
};

export default List;
