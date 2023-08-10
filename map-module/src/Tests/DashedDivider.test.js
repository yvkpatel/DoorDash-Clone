import React from 'react';
import renderer from 'react-test-renderer';
import { DashedDivider } from '../components';

it('renders Dashed Divider component correctly', () => {
    let tree = renderer.create(<DashedDivider />).toJSON();
    expect(tree).toMatchSnapshot();
});
