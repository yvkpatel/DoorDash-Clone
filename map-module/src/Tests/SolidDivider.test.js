import React from 'react';
import renderer from 'react-test-renderer';
import { SolidDivider } from '../components';

it('renders Solid Divider component correctly', () => {
    let tree = renderer.create(<SolidDivider />).toJSON();
    expect(tree).toMatchSnapshot();
});
