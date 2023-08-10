import React from 'react';
import './Sidepanel.css';
import arrow from '../assets/close-arrow.png';
import logo from '../assets/logo.png';

import {
    OrderCharges,
    OrderHeader,
    OrderInfoTitle,
    OrderItems,
    DashedDivider,
    SolidDivider,
} from '.';

export class Sidepanel extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isExpanded: false,
        };
        this.showSidepanel = this.showSidepanel.bind(this);
    }

    showSidepanel() {
        this.setState({
            isExpanded: !this.state.isExpanded,
        });
    }

    render() {
        return (
            <>
                <div className="sidepanel-container">
                    <div
                        className={
                            this.state.isExpanded
                                ? 'order-container active'
                                : 'order-container'
                        }
                    >
                        <div
                            className={
                                this.state.isExpanded
                                    ? 'order-info active'
                                    : 'order-info mb-4'
                            }
                        >
                            <img src={logo} width={'50vh'} alt="Logo" />
                        </div>
                        <div>
                            <OrderInfoTitle />
                            <SolidDivider />
                            <OrderHeader />
                            <SolidDivider />
                            <OrderItems />
                            <DashedDivider />
                            <OrderCharges />
                        </div>
                    </div>
                    <div
                        className={
                            this.state.isExpanded
                                ? 'sidepanel-toggle active'
                                : 'sidepanel-toggle'
                        }
                        onClick={this.showSidepanel}
                    >
                        <img src={arrow} width={'100%'} alt="arrow" />
                    </div>
                </div>
            </>
        );
    }
}
