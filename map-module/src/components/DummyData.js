export const getRestaurantName = () => {
    const name = 'Resto Beirut';
    return name;
};

export const getOrderNumber = () => {
    const orderNum = '16899';
    return orderNum;
};

export const getOrderItems = () => {
    const orderItems = [
        {
            quantity: '2',
            name: 'Chicken Shawerma',
            price: '$9.87',
        },
        {
            quantity: '3',
            name: 'Chicken Shawerma Poutine',
            price: '$16.87',
        },
    ];
    return orderItems;
};

export const getSubTotal = () => {
    const subTotal = '$26.74';
    return subTotal;
};

export const getDeliveryFee = () => {
    const deliveryFee = '$3.99';
    return deliveryFee;
};

export const getTax = () => {
    const tax = '$5.64';
    return tax;
};

export const getTip = () => {
    const tip = '$5.00';
    return tip;
};

export const getTotal = () => {
    const total = '$41.37';
    return total;
};

export const getCustomerLocation = () => {
    const customerLocation = "Memorial University St. John's NL";
    return customerLocation;
};
