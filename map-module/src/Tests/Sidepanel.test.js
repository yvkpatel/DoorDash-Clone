import React from 'react';
import renderer from 'react-test-renderer';
import { Sidepanel } from '../components';
import { mount } from 'enzyme';

describe('Sidepanel tests', () => {
    it('renders Sidepanel component correctly', () => {
        const tree = renderer.create(<Sidepanel />).toJSON();
        expect(tree).toMatchSnapshot();
    });

    it('closes and opens the side panel when the arrow button is pressed', () => {
        const wrapper = mount(
            <Sidepanel />
        );

        // Retrieve the button from our component using it's CSS class name 
        const p = wrapper.find('.sidepanel-toggle');

        // Expect it to be open
        p.simulate('click');
        expect(wrapper).toMatchSnapshot();
        expect(wrapper.state('isExpanded')).toBe(true);

        // Expect it to be closed
        p.simulate('click');
        expect(wrapper).toMatchSnapshot();
        expect(wrapper.state('isExpanded')).toBe(false);
    });
});
