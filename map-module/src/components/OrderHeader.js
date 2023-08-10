import React from 'react';
import { getRestaurantName, getOrderNumber } from './DummyData.js';

export function OrderHeader() {
    return (
        <div>
            <p>{getRestaurantName()}</p>
            <p>Order #{getOrderNumber()}</p>
        </div>
    );
}
