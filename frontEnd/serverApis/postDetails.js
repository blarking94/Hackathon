var request = require('request');

var postDetails = {
  postDetails: function(query){
    return new Promise((resolve, reject) => {
        request
            .get("127.0.0.1:8002/test")
            .set('Accept', 'text/plain')
            .end(function (err, response) {
                if(response.statusCode == 200){
                  resolve(response.body);
                } else if(response.statusCode && response.statusCode !== 200){
                  reject({statusCode: response.statusCode, text: (response.body)});
                }
            });
    });
  }
}

module.exports = postDetails;
