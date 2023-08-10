import React from 'react';
import { getOrderItems } from './DummyData';
import './OrderItems.css';

// This function might change depending on the format of the list returned
export function OrderItems() {
    const orderItems = getOrderItems();
    return (
        <div className="order-details">
            {orderItems.map((items, key) => (
                <p className="order-items" key={key}>
                    {items.quantity}
                    <span>{items.name}</span>
                    <span>{items.price}</span>
                </p>
            ))}
        </div>
    );
}
