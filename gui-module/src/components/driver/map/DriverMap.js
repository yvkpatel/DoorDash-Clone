// Displays map to driver
import React from "react";
import map from "../../resources/map_filler_image.jpeg";

const Map = () => {
  return (
    <div>
      <img
        src={map}
        alt="map"
        style={{
          height: "70vh",
          width: "75vw",
          display: "inline-flex",
        }}
      />
    </div>
  );
};

export default Map;
