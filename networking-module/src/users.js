"use restrict";

const http = require("https");

const options = {
	"method": "GET",
	"hostname": "ip-geolocation-and-threat-detection.p.rapidapi.com",
	"port": null,
	"path": "/54.85.132.205",
	"headers": {
		"x-rapidapi-host": "ip-geolocation-and-threat-detection.p.rapidapi.com",
		"x-rapidapi-key": "424b3025a9msh53dcac70ad5a852p187939jsnf58c188dc487",
		"useQueryString": true
	}
};

class Users {

    latitude;
    longitude;
    location;

    constructor(user) {
        this.users = {};
        this.location = {};
        this.status = {};
        this.notification = {};
    }

    getLocation = (callback, objectString) => {

        http.request(options, function (res) {
            const chunks = [];
        
            res.on("data", function (chunk) {
                chunks.push(chunk);
            });
        
            res.on("end", function () {
                const body = Buffer.concat(chunks);
                const body2 = JSON.parse(body);
                const lat = body2.location.latitude;
                const long = body2.location.longitude;
                location = {lat, long};
                callback(location);
            });
        }).end();
    }
    
    
    openChat = () => {};
}


module.exports = Users;