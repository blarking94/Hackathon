var request = require('request');

var postDetails = {
  postDetails: function(query, callback){
        request.post('http://127.0.0.1:8002/test', {form:{roleTitle:query.roleTitle,roleLevel:query.roleLevel,industryExpetise:query.industryExpetise,technologyExpetise:query.technologyExpetise,gallup:query.gallup,certifications:query.certifications,education:query.education,years:query.years}}, function (error, response, body) {
          callback(body)
          return(body)
        });
      }
}

module.exports = postDetails;
