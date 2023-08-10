import React from 'react';
import renderer from 'react-test-renderer';
import { OrderCharges } from '../components';

it('renders Order Charges component correctly', () => {
    let tree = renderer.create(<OrderCharges />).toJSON();
    expect(tree).toMatchSnapshot();
});
