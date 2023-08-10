const type = {
    driver : "driver",
    customer : "customer",
    restaurant : "restaurant",
}

const status = {
    orderRequestT: true,
    orderRecievedT : true,
    orderRequestF: true,
    orderRecievedF : true,
    orderAccpted : true,
}

const dbObject = [
    {
        name : "Mohammad Shakeel",
        userId :  "f43d3f7b-7abc-4cc2-a09f-c5ad4a9a51b6",
        address : {
            latitude : "47.572436",
            longitude : "-52.693946",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                reciever : "",
                message : "Now is the winter of our discontent",
                timeAndDate : "2021/12/27 12:35:32"
            },
            {
                message : "Made glorious summer by this sun of York",
                timeAndDate : "2022/08/15 10:57:17"
            },
            {
        
                message : "And all the clouds that lour'd upon our house",
                timeAndDate : "2022/09/20 19:06:10"
            },
            {
                message : "In the deep bosom of the ocean buried",
                timeAndDate : "2022/06/10 04:52:33"
            },
            {
                message : "Now are our brows bound with victorious wreaths",
                timeAndDate : "2022/01/21 13:53:36"
            }
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
            }
    },
    
    {
        name: "Charles Smith",
        userId:  "8149f16d-e36c-4eea-b1a3-41688cfcef4a",
        address: {
            latitude: " 47.561584",
            longitude: "-52.708625",
            city: "St John's",
            country: "Canada"
        },
        messages: [		
            {
                message: "Our bruised arms hung up for monuments",
                timeAndDate: "2022/04/18 06:09:43"
            },
            {
                message: "Our stern alarums changed to merry meetings",
                timeAndDate: "2022/07/16 00:20:08"
            },
            {
                message: "Now is the winter of our discontent",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "Grim-visaged war hath smooth'd his wrinkled front",
                timeAndDate : "2022/04/16 04:27:19"
            },
            {
                message : "And all the clouds that lour'd upon our house",
                timeAndDate : "2022/08/10 20:31:46"
            }      
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    },
    
    {
        name : "Gerda Block",
        userId :  "953ec3c9-1d60-4d97-b59d-8c522ba206cd",
        address : {
            latitude : " 	48.958349",
            longitude : "-54.59127",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                message : "To fright the souls of fearful adversaries",
                timeAndDate : "2022/04/18 06:09:43"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/07/16 00:20:08"
            },
            {
                message : "Our stern alarums changed to merry meetings",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "To the lascivious pleasing of a lute",
                timeAndDate : "2022/04/16 04:27:19"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/08/10 20:31:46"
            }      
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    },

    {
        name : "Dr. Bailey Schowalter",
        userId :  "811e6a11-5ca2-45f5-8125-d5e3d9304c99",
        address : {
            latitude : "47.526521",
            longitude : "-52.840346",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                message : "To fright the souls of fearful adversaries",
                timeAndDate : "2022/04/18 06:09:43"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/07/16 00:20:08"
            },
            {
                message : "Our stern alarums changed to merry meetings",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "To the lascivious pleasing of a lute",
                timeAndDate : "2022/04/16 04:27:19"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/08/10 20:31:46"
            }      
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    },
    
    {
        name : "Dandre Pouros",
        userId :  "0065f341-1c4e-4e1b-8949-900df1e00f26",
        address : {
            latitude : "47.463793",
            longitude : "-52.711769",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                message : "To fright the souls of fearful adversaries",
                timeAndDate : "2022/04/18 06:09:43"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/07/16 00:20:08"
            },
            {
                message : "Our stern alarums changed to merry meetings",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "To the lascivious pleasing of a lute",
                timeAndDate : "2022/04/16 04:27:19"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/08/10 20:31:46"
            }      
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    },
    
    {
        name : "Baylee Hammes V",
        userId :  "4c2ab54c-b4ce-4ac3-a13a-a5e28cb78877",
        address : {
            latitude : "47.562147",
            longitude : "-52.709661",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                message : "To fright the souls of fearful adversaries",
                timeAndDate : "2022/04/18 06:09:43"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/07/16 00:20:08"
            },
            {
                message : "Our stern alarums changed to merry meetings",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/08/10 20:31:46"
            },
            {
                message : "To the lascivious pleasing of a lute",
                timeAndDate : "2022/04/16 04:27:19"
            }
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    },
    
    {
        name : "Jon Mills",
        userId :  "4c2ab54c-b4ce-4ac3-a13a-a5e28cb78877",
        address : {
            latitude : "47.565327",
            longitude : "-52.705967",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                message : "To fright the souls of fearful adversaries",
                timeAndDate : "2022/04/18 06:09:43"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/07/16 00:20:08"
            },
            {
                message : "Our stern alarums changed to merry meetings",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "To the lascivious pleasing of a lute",
                timeAndDate : "2022/04/16 04:27:19"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/08/10 20:31:46"
            }      
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    },

    {
        name : "Mitchel Stehr",
        userId :  "de4d03fc-2ed9-43c5-b8ed-3b8b5a6c5e32",
        address : {
            latitude : "47.562466",
            longitude : "-52.709007",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                message : "To fright the souls of fearful adversaries",
                timeAndDate : "2022/04/18 06:09:43"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/07/16 00:20:08"
            },
            {
                message : "Our stern alarums changed to merry meetings",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "To the lascivious pleasing of a lute",
                timeAndDate : "2022/04/16 04:27:19"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/08/10 20:31:46"
            }      
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    },

    {
        name : "Mr. Jan Bednar",
        userId :  "9002101c-c82a-456b-8925-a0df80bd4080",
        address : {
            latitude : "47.557394",
            longitude : "-52.738753",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                message : "To fright the souls of fearful adversaries",
                timeAndDate : "2022/04/18 06:09:43"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/07/16 00:20:08"
            },
            {
                message : "Our stern alarums changed to merry meetings",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "To the lascivious pleasing of a lute",
                timeAndDate : "2022/04/16 04:27:19"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/08/10 20:31:46"
            }      
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    },

    {
        name : "Marcel Tremblay",
        userId :  "e08ef544-2c1e-4f11-bc19-16e458e7fe61",
        address : {
            latitude : "47.518853",
            longitude : "-52.804756",
            city : "St John's",
            country : "Canada"
        },
        messages : [		
            {
                message : "To fright the souls of fearful adversaries",
                timeAndDate : "2022/04/18 06:09:43"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/07/16 00:20:08"
            },
            {
                message : "Our stern alarums changed to merry meetings",
                timeAndDate : "2022/03/01 15:08:54"
            },
            {
                message : "To the lascivious pleasing of a lute",
                timeAndDate : "2022/04/16 04:27:19"
            },
            {
                message : "Now is the winter of our discontent",
                timeAndDate : "2022/08/10 20:31:46"
            }      
        ],
    
        status : {
            orderMade : true, 
            driverSelected : false, 
            deliveryMade : false
                    
        }
    
    }
    
];


module.exports = {dbObject};