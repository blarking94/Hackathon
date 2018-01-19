import axios from 'axios'

export function submitDetailsApi(action){
    return axios.post('/submitDetails?roleTitle='+action.roleTitle
    +"&roleLevel=" + action.roleLevel
    +"&industryExpetise=" + action.industryExpetise
    +"&technologyExpetise=" + action.technologyExpetise
    +"&gallup=" + action.gallup
    +"&certifications=" + action.certifications
    +"&education=" + action.education
    +"&years=" + action.years
    )
}
