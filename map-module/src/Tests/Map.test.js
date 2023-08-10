import React from 'react';
import renderer from 'react-test-renderer';
import { Map } from '../components';
import { mount } from 'enzyme';

describe('Map tests', () => {
    it('renders Map component correctly', () => {
        const tree = renderer.create(<Map />).toJSON();
        expect(tree).toMatchSnapshot();
    });

    it('triggers the google map API on component mount', () => {
        const wrapper = mount(
            <Map />
        );

        // Expect the direction result to be null when the map first loads
        expect(wrapper.state('directionResult')).toBe(null);
    });
});
