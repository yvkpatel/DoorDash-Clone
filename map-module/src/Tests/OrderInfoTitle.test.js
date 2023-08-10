import React from 'react';
import renderer from 'react-test-renderer';
import { OrderInfoTitle } from '../components';

it('renders Order Title component correctly', () => {
    let tree = renderer.create(<OrderInfoTitle />).toJSON();
    expect(tree).toMatchSnapshot();
});
