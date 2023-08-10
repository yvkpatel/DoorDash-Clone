import React from 'react';
import './OrderItems.css';

import { SolidDivider, DashedDivider } from '.';

import {
    getSubTotal,
    getDeliveryFee,
    getTax,
    getTip,
    getTotal,
} from './DummyData.js';

export function OrderCharges() {
    return (
        <div>
            <p className="order-items">
                Subtotal <span>{getSubTotal()}</span>
            </p>
            <SolidDivider />
            <p className="order-items">
                Delivery Fee <span>{getDeliveryFee()}</span>
            </p>
            <p className="order-items">
                Tax <span>{getTax()}</span>
            </p>
            <p className="order-items">
                Tip <span>{getTip()}</span>
            </p>
            <DashedDivider />
            <p className="order-items">
                Total <span>{getTotal()}</span>
            </p>
            <DashedDivider />
        </div>
    );
}
