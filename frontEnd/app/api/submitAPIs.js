import axios from 'axios'

export function submitDetailsApi(action){
    console.log("HITTING API")
    console.log(action)
    axios.post('/submitDetails?roleTitle='+action.roleTitle
    +"&roleLevel=" + action.roleLevel
    +"&industryExpetise=" + action.industryExpetise
    +"&technologyExpetise=" + action.technologyExpetise
    +"&gallup=" + action.gallup
    +"&certifications=" + action.certifications
    ).then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
}
