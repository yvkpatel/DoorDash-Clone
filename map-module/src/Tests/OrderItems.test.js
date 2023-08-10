import React from 'react';
import renderer from 'react-test-renderer';
import { OrderItems } from '../components';

it('renders OrderItem component correctly', () => {
    let tree = renderer.create(<OrderItems />).toJSON();
    expect(tree).toMatchSnapshot();
});
