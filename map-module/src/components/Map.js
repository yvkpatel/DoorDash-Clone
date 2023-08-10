import React from 'react';
import './Map.css';

import {
    GoogleMap,
    LoadScript,
    DirectionsRenderer,
    DirectionsService,
} from '@react-google-maps/api';

import { getRestaurantName, getCustomerLocation } from './DummyData.js';

// Hardcoded options to display a route on our map
const options = {
    origin: getRestaurantName(),
    destination: getCustomerLocation(),
    travelMode: 'DRIVING',
};

// Since were using React, I added a react google maps API wrapper.
export class Map extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            directionResult: null,
        };
    }

    // This is where the map is being inserted into our module.
    // It's just the starting code from here:
    // "https://react-google-maps-api-docs.netlify.app/#section-getting-started"
    render() {
        return (
            <div className="MapDiv">
                <LoadScript googleMapsApiKey={process.env.REACT_APP_API_KEY}>
                    <GoogleMap
                        options={{
                            styles: mapStyle,
                        }}
                        mapContainerStyle={containerStyle}
                        center={myLatLng}
                        zoom={15}
                    >
                        <DirectionsService
                            options={options}
                            callback={(result) => {
                                if (!this.state.directionResult) {
                                    this.setState({
                                        directionResult: result,
                                    });
                                }
                            }}
                        />
                        <DirectionsRenderer
                            directions={this.state.directionResult}
                        />
                    </GoogleMap>
                </LoadScript>
            </div>
        );
    }
}

// Map Size
const containerStyle = {
    width: '100%',
    height: '100vh',
    position: 'relative',
};

// Map Marker
const myLatLng = {
    lat: 47.56356087536938,
    lng: -52.71567239382679,
};

//Map Styling (Retro from https://mapstyle.withgoogle.com/)
const mapStyle = [
    {
        elementType: 'geometry',
        stylers: [
            {
                color: '#ebe3cd',
            },
        ],
    },
    {
        elementType: 'labels.text.fill',
        stylers: [
            {
                color: '#523735',
            },
        ],
    },
    {
        elementType: 'labels.text.stroke',
        stylers: [
            {
                color: '#f5f1e6',
            },
        ],
    },
    {
        featureType: 'administrative',
        elementType: 'geometry.stroke',
        stylers: [
            {
                color: '#c9b2a6',
            },
        ],
    },
    {
        featureType: 'administrative.land_parcel',
        elementType: 'geometry.stroke',
        stylers: [
            {
                color: '#dcd2be',
            },
        ],
    },
    {
        featureType: 'administrative.land_parcel',
        elementType: 'labels.text.fill',
        stylers: [
            {
                color: '#ae9e90',
            },
        ],
    },
    {
        featureType: 'landscape.natural',
        elementType: 'geometry',
        stylers: [
            {
                color: '#dfd2ae',
            },
        ],
    },
    {
        featureType: 'poi',
        elementType: 'geometry',
        stylers: [
            {
                color: '#dfd2ae',
            },
        ],
    },
    {
        featureType: 'poi',
        elementType: 'labels.text.fill',
        stylers: [
            {
                color: '#93817c',
            },
        ],
    },
    {
        featureType: 'poi.park',
        elementType: 'geometry.fill',
        stylers: [
            {
                color: '#a5b076',
            },
        ],
    },
    {
        featureType: 'poi.park',
        elementType: 'labels.text.fill',
        stylers: [
            {
                color: '#447530',
            },
        ],
    },
    {
        featureType: 'road',
        elementType: 'geometry',
        stylers: [
            {
                color: '#f5f1e6',
            },
        ],
    },
    {
        featureType: 'road.arterial',
        elementType: 'geometry',
        stylers: [
            {
                color: '#fdfcf8',
            },
        ],
    },
    {
        featureType: 'road.highway',
        elementType: 'geometry',
        stylers: [
            {
                color: '#f8c967',
            },
        ],
    },
    {
        featureType: 'road.highway',
        elementType: 'geometry.stroke',
        stylers: [
            {
                color: '#e9bc62',
            },
        ],
    },
    {
        featureType: 'road.highway.controlled_access',
        elementType: 'geometry',
        stylers: [
            {
                color: '#e98d58',
            },
        ],
    },
    {
        featureType: 'road.highway.controlled_access',
        elementType: 'geometry.stroke',
        stylers: [
            {
                color: '#db8555',
            },
        ],
    },
    {
        featureType: 'road.local',
        elementType: 'labels.text.fill',
        stylers: [
            {
                color: '#806b63',
            },
        ],
    },
    {
        featureType: 'transit.line',
        elementType: 'geometry',
        stylers: [
            {
                color: '#dfd2ae',
            },
        ],
    },
    {
        featureType: 'transit.line',
        elementType: 'labels.text.fill',
        stylers: [
            {
                color: '#8f7d77',
            },
        ],
    },
    {
        featureType: 'transit.line',
        elementType: 'labels.text.stroke',
        stylers: [
            {
                color: '#ebe3cd',
            },
        ],
    },
    {
        featureType: 'transit.station',
        elementType: 'geometry',
        stylers: [
            {
                color: '#dfd2ae',
            },
        ],
    },
    {
        featureType: 'water',
        elementType: 'geometry.fill',
        stylers: [
            {
                color: '#b9d3c2',
            },
        ],
    },
    {
        featureType: 'water',
        elementType: 'labels.text.fill',
        stylers: [
            {
                color: '#92998d',
            },
        ],
    },
];
