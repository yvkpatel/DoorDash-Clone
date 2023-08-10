import React from 'react';
import renderer from 'react-test-renderer';
import { OrderHeader } from '../components';

it('renders Order Header component correctly', () => {
    let tree = renderer.create(<OrderHeader />).toJSON();
    expect(tree).toMatchSnapshot();
});
